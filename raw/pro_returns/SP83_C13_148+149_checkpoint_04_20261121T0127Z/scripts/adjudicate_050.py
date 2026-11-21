from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]; p='148_scan050'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B02':'The heading ends with a single e turn; neither a separate plural s nor a point follows. The continuous underline belongs to Remarque.',
'B03':'Three distinct word levels are visible: current remplacée above, crossed complétée in the middle, and another crossed remplacée below. The two older word bodies are not fully recoverable through their strokes. The lower cancelled word was omitted in the first reading and is restored; the current replacement has a separate accented ending and terminal e.',
'B04':'The upper une is left of the short cancellation and remains live. The upper cancelled word has a tall initial t-like stroke, a compact r/i region, a descending p-like stroke and a final tall loop, favouring triple; famille remains an alternative because the lower application strokes overlap it. The later large famille is uncrossed. The first placement of that final word is retained; the cropped geometry does not establish that the entire later word is an interlinear insertion.',
'B05':'The initial A has an apex, two legs and bar; p/rho remains uncertain. Two short parallel strokes join the right target to the lower vector A/sigma. The rightward mark over the lower A is its vector accent. The main strike traverses the tuple, beginning after the initial A; cancellation of the entire abandoned unit, including initial A and lower continuation, is not certain. The first diagram is retained with its deletion scope explicitly doubtful.',
'B06':'In the rotated marginal crop, au has a low oval followed by the u turn. Both small a accents have right-pointed shafts, and the separator is an oblique slash. There are no hyphens between au dessus de. Wrapper and uncertainty differences do not justify changing the first reading.',
'B07':'The live text has d’ensembles and the inverted-A quantifier. The double quotation strokes bracket orientations, not de a. The heavily struck intervening wording retains visible p/t fragments but cannot be read with a secure word count. The small lower-left de-like group lies near the next baseline; its attachment as cancelled de versus a live deux-like group remains doubtful and is marked in place. Ens versus un also remains open.',
'B08':'R, et, the stem-and-bowl map label, une application, R and A survive the strike. The faint final group has a c-like start and descending joined strokes; conj. à remains provisional. The strike does not support a secure qui plus a count of two unreadable words.',
'B09':'The omega map, colon, rightward arrow and Circ(R_a) agree. The gloss clearly begins ens des and continues circulaires sur R_a. The highly compressed end of the permutation word does not securely distinguish the full form from permutat.; both are now shown. Its trailing curve is not securely separate comma punctuation.',
'B10':'The first cancelled words remain crossed through their centres; d’autre versus relie à and the first une-like group are uncertain. An additional small residual group precedes the second une; bi. is a possible reading, not a resolved abbreviation. Application is readable. The final word has the j descender, t, dotted i and on ending of injection, with a separate underline; it is not injective. The old map has a left hook and a pointed right arrowhead.',
'B11':'Que si is visible context already present before the first selected reading in the page. Both omega entries, the inequality and the live inverse relation agree. The little loop at the end of the cancelled identity subscript can be a small a or part of the R leg; that uncertainty remains. There is no terminal point after the live exponent.',
'B12':'The first word has the two p descenders and tall l of suppléments, not the longer simplification outline. The following joined group begins with a small r shoulder and continues evient. The upper boundary trims the later baseline, so this crop does not support replacing the first à la donnée de with a conjectural colon or plural ending.',
'B13':'The map letter has a low stem and upward right shoulder. Its local form agrees with the clearer r in the NB and the denominator r(a), so the established r is retained, not nu. The initial C of Card is tall and open. Two separate vertical strokes between the rows form equality; p/rho remains explicitly uncertain.',
'B15':'The family and its a-in-A index are visible. The following heavily overwritten short unit has curved end fragments compatible with omega(a); it is a formula, so it is not replaced by an illegible-word count. The earlier uncertainty is retained.',
'B16':'The omega(a) is visibly raised to the upper right of the wedge, with the brace-enclosed plus/minus 1 below it. The denominator has the same low r form as the NB. On associe follows without a separating point; the first superscript placement is retained.',
'B17':'The article after Sigma_a is a looped l with a compact terminal that does not securely distinguish a/e. The old crossed word has a long run of low arches, a p-like descender and tall final strokes, favouring correspondant over marquée but not resolving every letter. The raised qui correspond à is live. The cancelled la donnée de Sigma is present on the underlying line and must not be omitted. The surrounding parenthesis is not given an additional insertion wrapper solely from the compressed layout.',
'B18':'The cancelled left equation has a looped single-stem ell after the equality, not a capital R or pi_0. The first sign inside its parentheses is rounded and crossed at its top, admitting partial or alpha before C. The square has one upper R-to-S arrow and two vertical equalities. Its lower-left upright has a top stroke merged with the cancellation, so Gamma/I remains open. The lower horizontal relation lacks a securely separable arrowhead, and the tilde over its lower-right Sigma is obscured; both are explicitly doubtful.',
'B19':'Under the strike, the d ascender and following éduit, the apostrophe and ordre, and the c/i/r/c/l sequence of circulaire remain visible. These words are not replaced by a count of unreadables. The map label and dans/sur remain uncertain; no point is added after the final R_a.',
'B20':'The first r has a straight short stem with a right shoulder; the second repeats the same notation. Both arguments are omega, not silently changed to a. Disposer has a p descender and no following g descender or internal t bar of distinguer. NB has an underline and no point.',
'B21':'The corner number has the open 4 followed by a rounded 9 and long curved descending tail. The mspage wrapper is the established representation of the same 49.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
for b in ('B06','B07','B08','B09','B10'): D[b]['crop']=f'second/{p}_second_{b}_rotated.png'
new={
'B03':r'\deleted{\unsure{complétée}} \deleted{\unsure{remplacée}} \inserted{remplacée}',
'B04':C['B04']['first'].replace(r'\unsure{famille}',r'\unsure{triple|famille}'),
'B05':r'\unsure{'+C['B05']['first']+'}',
'B07':C['B07']['first'].replace(r'\deleted{\unsure{donné d\'une permutation de}}',r'\deleted{\unsure{donné d\'une permutation}} \unsure{\deleted{de}|deux}'),
'B09':C['B09']['first'].replace('ens des permutations','ens des '+r'\unsure{permutations|permutat.}'),
'B10':r"\deleted{et \unsure{d'autre|relie à} \unsure{une} \unsure{\illegible{1}|bi.} une application \uline{injection}} $\deleted{R/\alpha\lhook\joinrel\longrightarrow\vec A}$",
'B17':C['B17']['first'].replace('$ la comp.',r'$ \unsure{la|le} comp.').replace(r'\unsure{marquée}',r'\unsure{correspondant|marquée}'),
'B18':r'''\deleted{$R=\ell(\unsure{\partial C|\alpha C})$,} \deleted{\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small]
R\arrow[rr]\arrow[d,equal]\&\&S\arrow[d,equal]\\
\unsure{\Gamma|I}\&\unsure{\longrightarrow|\relbar}\&\pi_0(\unsure{\widetilde\Sigma|\Sigma})
\end{tikzcd}}}'''}
# Explicit apostrophe strings, avoiding accidental literal backslashes.
new['B07']=C['B07']['first'].replace("\\deleted{\\unsure{donné d'une permutation de}}", "\\deleted{\\unsure{donné d'une permutation}} \\unsure{\\deleted{de}|deux}")
pp=R/'pages'/f'{p}.tex';page=pp.read_text()
# Match selected boxes that appear as exact fragments or have display whitespace.
for b in ('B03','B04'):
 assert C[b]['first'] in page,b
 page=page.replace(C[b]['first'],new[b]);D[b].update(choice='reading',reading=new[b])
start=page.index(r'\deleted{\diagram{');end=page.index(r'\end{tikzcd}}}',start)+len(r'\end{tikzcd}}}');page=page[:start]+r'\unsure{'+page[start:end]+'}'+page[end:];D['B05'].update(choice='reading',reading=new['B05'])
repls=[("\\deleted{\\unsure{donné d'une permutation de}}","\\deleted{\\unsure{donné d'une permutation}} \\unsure{\\deleted{de}|deux}"),('ens des permutations',r'ens des \unsure{permutations|permutat.}'),(r"\deleted{et \unsure{d'autre} \unsure{une} \unsure{\illegible{1} une application injective|application injective}}",r"\deleted{et \unsure{d'autre|relie à} \unsure{une} \unsure{\illegible{1}|bi.} une application \uline{injection}}"),(r'$ la comp. connexe',r'$ \unsure{la|le} comp. connexe'),(r'\unsure{marquée}',r'\unsure{correspondant|marquée}')]
for a,z in repls:assert a in page,a;page=page.replace(a,z)
oldstart=r'\deleted{$\unsure{R=R(\Sigma C)|R=\pi_0(\widetilde\Sigma)}$,}'
start=page.index(oldstart);end=page.index(r'\end{tikzcd}}}',start)+len(r'\end{tikzcd}}}')
page=page[:start]+new['B18']+page[end:]
for b in ('B07','B09','B10','B17','B18'):assert new[b]!=C[b]['first'],b;D[b].update(choice='reading',reading=new[b])
pp.write_text(page)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def upd(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02}'); x.update(evidence=E[b],crop=D[b].get('crop',f'crops/{p}_second_{b}.png'),box=boxes[b],**kw)
upd(2,'B03',final=new['B03'])
upd(4,'B04',final=r'\inserted{une \deleted{\unsure{triple|famille}}} famille',confidence='medium')
upd(11,'B07',final="\\deleted{\\unsure{donné d'une permutation}} \\unsure{\\deleted{de}|deux}")
upd(14,'B09',final=r'ens des \unsure{permutations|permutat.} circulaires sur $R_a$',confidence='medium')
upd(15,'B10',final=new['B10'].split(' $')[0])
upd(25,'B17',final=r'\deleted{\unsure{correspondant|marquée}}',diff_c=True)
upd(26,'B18',final=new['B18']+r' followed by \deleted{\unsure{la donnée de} $\widetilde\Sigma$}',confidence='low')
r['changes'].append(dict(id=p+'-34',place='Opening revisions, second cancelled word below complétée',c='absent',h='absent',final=r'\deleted{\unsure{remplacée}}',diff_c=True,diff_h=True,kind='omission',error_kind='Omissions',evidence=E['B03'],crop=f'crops/{p}_second_B03.png',box=boxes['B03'],confidence='medium',marked_in_h=False,consequential=False))
# Update all remaining-doubt entries that were refined by the independent comparison.
updates={
'Cancelled upper famille':('Cancelled upper word after une',r'\unsure{triple|famille}','triple; famille','B04'),
'Cancelled phrase between des and orientations':('Cancelled phrase and lower-left attachment',r"\deleted{\unsure{donné d'une permutation}} \unsure{\deleted{de}|deux}",'cancelled de; live deux; phrase otherwise uncertain','B07'),
'Cancelled word after et before injection':(None,r"\unsure{d'autre|relie à}",'d’autre; relie à','B10'),
'Remaining cancelled injection phrase and segmentation':(None,r'\unsure{\illegible{1}|bi.} une application \uline{injection}','one unreadable group; bi.','B10'),
'Cancelled adjective before qui correspond à':(None,r'\unsure{correspondant|marquée}','correspondant; marquée','B17'),
'Cancelled equation below R_a definition':(None,r'R=\ell(\unsure{\partial C|\alpha C})','partial C; alpha C','B18'),
'Lower-left object in cancelled square':(None,r'\unsure{\Gamma|I}','Gamma; I','B18')}
for x in r['doubts']:
 if x['place'] in updates:
  place,reading,alternatives,b=updates[x['place']];x.update(reading=reading,alternatives=alternatives,reason=E[b]);
  if place:x['place']=place
for place,reading,alts,b in [
 ('Second old word in opening revisions',r'\deleted{\unsure{remplacée}}','cancelled letters obscured','B03'),
 ('Cancellation extent of first abandoned diagram',new['B05'],'whole unit cancelled; strike limited to tuple and part of lower continuation','B05'),
 ('Compressed permutation word in Circ gloss',r'\unsure{permutations|permutat.}','full word; abbreviation','B09'),
 ('Article before comp. connexe',r'\unsure{la|le}','la; le','B17'),
 ('Lower relation in cancelled square',r'\unsure{\longrightarrow|\relbar}','rightward arrow; horizontal line without a head','B18'),
 ('Lower-right Sigma accent in cancelled square',r'\pi_0(\unsure{\widetilde\Sigma|\Sigma})','tilde Sigma; Sigma','B18')]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=E[b]))
for x in r['inventory']:
 if x['element']=='E06':x['first_words_or_objects']='une; cancelled triple/famille'
 if x['element']=='E08':x['position']+='; extent of cancellation uncertain'
 if x['element']=='E12':x['first_words_or_objects']='donné d’une permutation; lower de/deux attachment uncertain'
 if x['element']=='E16':x['first_words_or_objects']='et d’autre/relie à ... une application; underlined injection'
 if x['element']=='E28':x['first_words_or_objects']=x['first_words_or_objects'].replace('la comp.','la/le comp.')
 if x['element']=='E29':x['first_words_or_objects']='correspondant/marquée'
 if x['element']=='E31':x['first_words_or_objects']='R = ell(partial C / alpha C)'
 if x['element']=='E32':x['first_words_or_objects']='R to S; Gamma/I horizontal relation to pi_0(Sigma, tilde uncertain); vertical equalities'
r['inventory'].insert(3,dict(element='E38',sheet_kind='text',hand='his hand',kind='deletion',position='Opening revisions, lower old word',first_words_or_objects='remplacée (uncertain under strike)',transcribed='yes'))
r['notes'].append(dict(id=p+'-N-audit',text='Independent second reading restores an additional cancelled remplacée; favours triple and correspondant in two crossed replacements while retaining alternatives; and reads the underlined cancelled noun injection literally after application. The lower old equation has ell and a partial/alpha-C argument, not the first draft R/π₀ alternatives. No mathematical repair is made to these cancelled fragments. The local r notation is confirmed from the clearer NB occurrences; r(omega) is retained literally. Cancellation extent, a lower de/deux attachment, a compressed abbreviation, and the bottom square’s arrowhead/accent remain explicit uncertainties.'))
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json'}
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
