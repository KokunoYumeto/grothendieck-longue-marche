"""Root's visual decisions for every fixed blind difference on scan 078."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign

B=Path(__file__).resolve().parents[1]; page='149_scan078'
rp=B/'reviews'/f'{page}.json'; r=json.loads(rp.read_text()); assert not r.get('audit')
p=B/'pages'/f'{page}.tex'; t=p.read_text()
display=r'V/g_{i_0}^{\unsure{*}}(\mathcal J_f)\simeq\unsure{A|\mathbb A}/(\mathcal J_{g_{i_0}}+\mathcal J_f)'
connector=r'T_\ell\unsure{-|\longrightarrow}T_\ell^I'
punct=r'premie\uline{rs}\margin{\deleted{\unsure{?!}}\\\unsure{?!|2!}}'
letter=r'\unsure{k|\kappa|K}'
margin=r'Ceci doit \unsure{être|etre} \unsure{indépendant|independant} de la valeur de $\nu$ !'
repls=[(r'V/g_{i_0}^*(\mathcal J_f)\simeq A/(\mathcal J_{g_{i_0}}+\mathcal J_f)',display),(r'T_\ell-T_\ell^I',connector),(r'premi\unsure{e\uline{rs}|\uline{ers}}\margin{\deleted{\unsure{?!}}\\?!}',punct),(r'\unsure{k|\kappa}',letter),(r'Ceci doit être indépendant de la valeur de $\nu$ !',margin)]
for old,new in repls:
 assert t.count(old)==(2 if old==r'\unsure{k|\kappa}' else 1),(old,t.count(old))
 t=t.replace(old,new)
p.write_text(t)
ev01='The first word has a shallow n entry and compressed e return. The next begins with a separate open c and tall looped h, followed by low a/n, a deep g loop near the end and a short e return. These visible c/h and g components retain ne change; the blind degree reading would assign the separate c/h contours to one initial d.'
ev02='The initial q has a small bowl and deep descending loop. Its joined low u/a/n run ends at a separate tall d. After a gap, two low dark components form the compressed o/n. The shallow closed o and following return are retained as letters. No accent is supplied to the q opening.'
ev03='The initial short i has its detached upper mark beside a low n entry. Three tall t stems occur through the word, with low e/r/v/e/r returns between them and a short dotted i before the last stem. Those particular stems and joins retain intervertit; the spaces and separate capital O of the blind reading are not independently present.'
ev04='After les, the next word has a low r, a compact closed o, a tall looped l and low e/s. Its last hooked return matches the s ending of les. No separate preterminal dotted i is visible. The area above o has no detached circumflex, so retain les roles.'
ev06='The raised mark on the first g has several crowded crossing strokes; star remains tentative because their components are retraced. The right capital has two dark legs and a crossbar together with a pale inner loop/extra contour, leaving ordinary A and a doubled A rendering open. All three J forms have the same upper strokes and hooked lower ends in both readings; the mathcal/plain-J wrappers map to those same three ink bodies. The V, quotient slashes, subscripts, parentheses, plus and wavy-upper/straight-lower relation remain.'
ev07='After the dash an open c joins a small closed a bowl and a low extended r return. The two separate bodies and final return retain car. The following nu has a short left branch, low valley and rising curved right arm, as in B15; no prose accent is added.'
ev08='The raised prefix has two short s bodies followed by a hyphen; the separate o/u bodies needed for the full sous are not visible. The long curve beneath the raised schémas runs continuously to the gap after des and before f(S). Its right end supplies the comma-like contour proposed in the blind return, so no independent comma is added. The baseline et remains visible at the right of the crop. The raised phrase remains attached after des.'
ev13='The left capital has a broad cap extending to both sides of its descending stem, with the stem toward the left third and a short lower hook: retain T. The neighboring J forms have a right-side stem and broad lower leftward turn. The connector has one shaft and a tiny dark downturned right end. A separate second arrowhead wing is not secure, leaving a headless stroke and a right arrow as local alternatives. Both lower ell forms and the raised barred I remain.'
ev16='The current L has its tall stem and low return into e; extra ink under the e can still be retracing or an unreadable older layer. Before and beneath fait is a separate small looped older group. The current f has long upper/lower loops and a crossing return, followed by a, a dotted short i and a tall t. The live i/t lie beyond the heavy overlap, without a strike traversing the complete word. Retain the separate unreadable canceled fragment and the existing local state alternative beneath Le.'
ev17='The low e cup ends before the short underline begins; the line lies below r and s, so read premie with only rs underlined. The upper blackened punctuation still exposes a curved remnant and a narrow right stroke under the hatch, retaining tentative canceled ?!. In the lighter lower pair, the first character has a curved top and long foot admitting either question mark or 2; a separate question dot is not secure. The right upright and low point support the exclamation. Reopen M1215 as ?!/2! rather than claiming the lower pair resolved.'
ev18='The tall l ends in a small e-like low loop, while a distinct upper apostrophe-like stroke lies before h. The low loop can supply an e or the return of l; preserve le/l-apostrophe. The h ascender, closed o, low m and separate abbreviation stop remain visible. Syntax is not used to settle the local boundary.'
ev20='The canceled initial body retains its long left descender and partly visible upper arms under the strike, supporting tentative mu. In both this crop and B21 the live indexed letter has a long stem and two right branches below its top. Their height and joined fork admit k, kappa and K, with k first. The repeated fork supplies two right arms; neither occurrence supplies the upper/lower loop sequence proposed by the blind f alternative. The composition circle, parentheses, mu with two arms and left descender, following baseline point, dotted i, looped d, lowered T and comma remain. Operatorname/mathrm map here to the same written i and d at the same coordinates.'
ev22='The word bodies etre and independant remain readable, but no detached circumflex above the first or secure acute above the second can be isolated from their joined upper contours; keep both accent choices open. The complete original and the overlapping B16 crop locate the terminal exclamation: its slanting stem continues into the upper edge of B16, with a separate dark point around original (384,1895). B22 ends at x=357 and clips that final punctuation. The longer stroke lower on the right edge of B22, around x=346 and y=1930–1977, instead maps continuously to the L and its lower return in Le shown completely in B16. Thus retain the actual terminal exclamation from the original/B16, without counting the clipped L a second time. The low nu valley and rising right branch remain at the end of the note.'

c={x['id']:x for x in r['changes']}
for key,ev in [('P01',ev01),('P02',ev02),('P03',ev03),('P04',ev04),('P06',ev07),('P07',ev08),('P13',ev16)]:c[key]['evidence']=ev
x=c['P11'];x.update(final=connector,evidence=ev13,confidence='medium',against_C=False,against_H=False,status='Both witness connectors remain unresolved; excluded from material counts.',accounting_note='C’s headless stroke and H’s arrow both remain explicit alternatives. The T letter is retained from its cap/stem contour; adding connector doubt alone is uncounted.')
r['changes'].remove(x);r['nonmaterial_observations'].append(x)
c['P14'].update(final=punct,evidence=ev17,confidence='medium',components=['Underline confined to rs.','Older blackened punctuation retained tentatively.','M1215 remains undecided between ?! and 2!.'],lower_confidence_component='The older canceled punctuation remains tentative; the lower pair also remains unresolved.')
c['P17'].update(final=r'\deleted{\unsure{\mu}}'+letter+r'_{i_0}\circ(\mu.\operatorname{id}_T)',evidence=ev20,lower_confidence_component='Canceled initial mu remains low confidence; both live indexed letters retain k/kappa/K alternatives.')
c['P19'].update(final=margin,evidence=ev22,confidence='medium')
r['decisions'][0].update(decision='undecided',reading=r'\unsure{?!|2!}',evidence=ev17,crop='crops/149_scan078_B17_second.png (888,1985,1210,2116)',confidence='medium')
r['doubts']=[x for x in r['doubts'] if x['place']!='P14, left endpoint of the short underline']
for x in r['doubts']:
 if x['place'].startswith(('P17, live','P18,')):x.update(reading=letter+r'_{i_0}',alternatives='k; kappa; K',reason=ev20)
 if x['place']=='P14, older blackened punctuation':x.update(reason='A curved remnant and narrow right stroke remain under the dark hatch above the lighter unresolved ?!/2! pair.')
for place,reading,alts,ev in [('B06, raised mark on first g',r'\unsure{*}','tentative star under retracing',ev06),('B06, right capital',r'\unsure{A|\mathbb A}','A; doubled A',ev06),('P11 / B13, inline connector',r'\unsure{-|\longrightarrow}','headless stroke; right arrow',ev13),('P14 / M1215, lower punctuation',r'\unsure{?!|2!}','?!; 2!',ev17),('P19 / B22, first accent',r'\unsure{être|etre}','être; etre',ev22),('P19 / B22, second accent',r'\unsure{indépendant|independant}','indépendant; independant',ev22)]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=ev))
for x in r['nonmaterial_observations']:
 if x['id']=='P14_underline_boundary':x.update(final=r'premie\uline{rs}',evidence=ev17,status='The boundary is now resolved to rs; the shorter underline is already counted at P14, with no duplicate row.')
 if x['id'] in ['P17_alphabet','P18_alphabet']:x.update(final=letter+r'_{i_0}',evidence=ev20,status='Unresolved local alphabet/case choice, retaining both witnesses; uncounted.')
 if x['id']=='P15_word':x['evidence']=ev18
 if x['id']=='P05_J_wrapper':x['evidence']=ev06
 if x['id']=='P16_U_wrapper':x['evidence']='At each of the two U positions the long left downstroke joins a rounded lower turn and rising right limb; the final one has a separate low s. Plain U and mathcal U designate those same respective bodies and positions. The actual differing eta argument is counted at P16.'
for x in r['inventory']:
 for old,new in repls:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
 if x['element']=='E12':x['first_words_or_objects']=r'\unsure{?!|2!}'
 if x['element']=='E14':x['first_words_or_objects']=margin
for x in r['notation']:
 for old,new in repls:x['form']=x['form'].replace(old,new)
 if x['places']=='Main line 11, P11':x['meaning']='The inline expression called injection canonique; the tiny connector endpoint leaves headless stroke/right arrow open.'
 if x['places']=='Main line 20, P17':x['meaning']='The source product expression, including a canceled tentative mu and the unresolved k/kappa/K letter.'
for x in r['hand']:
 if x['form']=='Tall k-like stem':x.update(observation=ev20,witness_errors='C’s kappa and H’s k both remain among the unresolved k/kappa/K alternatives.')
 if x['form']=='Short underline and revised punctuation':x.update(observation=ev17,witness_errors='C extends the underline to the whole word; H omits underline and punctuation. The lower supplied mark remains unresolved.')
 if x['form']=='Open U and hooked J':x['observation']+=' The exact same-ink correspondence is recorded in the P05_J_wrapper and P16_U_wrapper observations.'
r['hand'].append(dict(form='Clipped marginal boundary and accent strokes',observation=ev22,places='P19 / B22, compared with B16 and the original page',scope='This margin note only.',witness_errors='Both witnesses’ accents remain tentative. Their terminal exclamation is retained from its actual source position beyond the frozen B22 right edge.'))
r['notes'][1]=r'N078_02 — Author’s doubt. The source writes Je présume que before the displayed hom expression, then calls the inline expression an injection canonique. Its connector is now locally \unsure{-|\longrightarrow}. The following words are Il faudrait que je demande à Carlos de me le confirmer. Carlos is retained as written; no external identification is made.'
r['notes'][2]=r'N078_03 — Author’s qualification: Reste le cas $\nu=1$, qui semble demander un traitement séparé. The final paragraph begins Le fait à vérifier and gives a hom. ext. expression and a product, ending at où the indexed \unsure{k|\kappa|K} est. No continuation is supplied.'
r['notes'][3]='N078_04 — Author’s marginal statement, with its unresolved accents: '+margin+'. The lower punctuation beneath premiers remains ?!/2!; the older blackened pair remains tentative canceled ?!. The underline itself is now confined to rs.'
r['notes'].append('N078_06 — The independent audit changed six of twenty-three boxes after root inspection of all nineteen differences. It reopened M1215, retained local star/capital/connector/accent doubts, enlarged the repeated indexed-letter alternatives, and settled the underline to rs. The clipped margin boundary was checked against the original page and overlapping B16; the actual exclamation lies beyond the B22 right edge. No additional mathematical check was performed during this audit.')
r['deletion_insertion_review'][3]=ev17
r['deletion_insertion_review'][4]='Older blackened punctuation retains tentative canceled ?!, while the separate lighter lower pair remains unresolved ?!/2!. M1215 is undecided.'
r['open_issues']=[x['place']+': '+x['reading'] for x in r['doubts']]
for x in r['diff_coverage']:
 if x['row']==8:x.update(status='unresolved alternatives; uncounted P11',reason=ev13)
 if x['row'] in [12,14]:x['reason']=x['reason'].replace('k/kappa','k/kappa/K')
 if x['row']==15:x['reason']='The note has doit, with d/o/i/t, followed by the etre body. The accents remain open; the actual terminal exclamation is retained from the original and overlapping B16.'
 if x['row']==16:x['reason']='The lower ?!/2! pair remains unresolved; the older blackened punctuation and folio 77 are present. The underline is confined to rs. H’s descriptive metadata adds no source word.'
r['counts'].update(material_place_rows=len(r['changes']),against_C=sum(bool(x['against_C']) for x in r['changes']),against_H=sum(bool(x['against_H']) for x in r['changes']),resolved_supplied_marks=0,unresolved_supplied_marks=1,local_doubt_entries=len(r['doubts']),nonmaterial_observations=len(r['nonmaterial_observations']),actual_mathematical_check_events=len(r['check_events']))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

D={}
def keep(b,title,ev):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=ev)
def change(b,final,title,ev):D[b]=dict(final=final,changed=True,decision=title,evidence=ev)
for b,title,ev in [('B01','Retain the separate c/h and descending g',ev01),('B02','Retain q, terminal d and the two following letters',ev02),('B03','Retain the three t stems and dotted i forms',ev03),('B04','Retain the closed o and terminal e/s',ev04),('B07','Retain the c/a bodies and final r',ev07),('B08','Retain the abbreviation and trace its insertion leader',ev08),('B16','Retain the local revision layers and live fait',ev16),('B18','Keep the article boundary open',ev18)]:keep(b,title,ev)
keep('B05','Retain the same g and full low index','The g bowl and long descending return, the short dotted low i and the lower closed 0 occupy the same positions in both readings. Enclosing dollar delimiters supply no additional glyph.')
change('B06',display,'Keep the retraced star and capital open',ev06)
keep('B09','Retain the same indexed g and S argument','The g upper bowl and descending loop, dotted low i, lower closed 0, two enclosing curves and two-lobed capital S map one for one to both readings. Only enclosing dollar delimiters differ.')
change('B13',connector,'Keep the connector endpoint open and retain T',ev13)
keep('B14','Retain the complete index and detached period','The separate dot over the short i, the lower closed zero and the detached following dark point give i_0 and its period. Both strings refer to these same components; the dollars add no source stroke.')
keep('B15','Retain the same nu equality','The short left branch and curved rising right branch give nu; the two equality bars and the 1 with its upper entry and lower foot occupy the same positions in both readings. Only enclosing dollars differ.')
change('B17',punct,'Resolve the underline and reopen the lower punctuation',ev17)
keep('B19','Retain the complete pi expression','Each pi has its broad upper bar and shorter lower right return; the first is especially clear beside the short low left stroke. Each low 1, the eta arch and descending right limb, rightward arrow, U contours, wavy-upper/straight-lower similarity and final low s map one for one to both readings. Enclosing dollars are the sole token difference. The pi bodies are also compared with the listed cross-page occurrences; no letter is changed here.')
change('B20',r'\deleted{\unsure{\mu}}'+letter+r'_{i_0}\circ(\mu.\operatorname{id}_T),','Keep the repeated forked letter open',ev20)
change('B21',letter+r'_{i_0}\text{ est}','Apply the same alternatives to the repeated fork',ev20)
change('B22',margin,'Keep the accent choices and identify the clipped boundary',ev22)
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D))
record(page);assign('reader_a')
