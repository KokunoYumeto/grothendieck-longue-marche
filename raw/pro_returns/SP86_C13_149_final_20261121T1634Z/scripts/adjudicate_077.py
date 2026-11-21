"""Root's visual decisions for all seventeen fixed blind differences on scan 077."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1]; page='149_scan077'
rp=B/'reviews'/f'{page}.json'; r=json.loads(rp.read_text()); assert not r.get('audit')
p=B/'pages'/f'{page}.tex'; t=p.read_text()
dest=r'\unsure{T|\mathbb T|\deleted{\unsure{Z}}T}_\ell^I/T_\ell'
sup=r"\unsure{\bullet|0|1|'}"
ker=r'\deleted{\unsure{\operatorname{Ker}}}\operatorname{Ker}(\mathcal J^{'+sup+r'}_{U/S}\longrightarrow\mathcal J^{'+sup+r'}_{X/S})\simeq G_m^I/G_m'
sh=r'\unsure{=|\overline m}'
state=r'\unsure{\deleted{=}|\neq}'
repls=[(r'\unsure{T|\mathbb T}_\ell^I/T_\ell',dest),(r'\unsure{envisagé|envisage}','envisage'),(r'\deleted{[On va faire des calculs intrinsèques, en}',r'\deleted{\unsure{[}On va faire des calculs intrinsèques, \unsure{en|car}}'),(r'\unsure{\operatorname{Ker}}(\mathcal J^\bullet_{U/S}\longrightarrow\mathcal J^\bullet_{X/S})\simeq G_m^I/G_m',ker),(r'\underset{\substack{\text{isom}\\\text{de Kummer}}}{\simeq}',r'\underset{\substack{\text{isom}\\\text{de Kummer}}}{=}'),(r'\deleted{\unsure{q}}',r'\deleted{\unsure{q|g}}'),(r'$A=\underline O_{X,x}$,',r'$A=\underline O_{X,x}$\unsure{)|,}'),(r'$\overline m$',r'$'+sh+'$'),(r'considérons $g_{i_0}^*(\mathcal J_f)$',r'considérons $g_{i_0}^{\unsure{*}}(\mathcal J_f)$'),(r'\operatorname{long}V/',r'\operatorname{long}\unsure{V|A}/'),(r'\deleted{\unsure{=}}',state),('cet entier','est entier')]
for a,b in repls:
 assert t.count(a)==1,(a,t.count(a)); t=t.replace(a,b)
p.write_text(t)
ev04='The destination has a broad dark top bar, a long upright and an additional rising oblique crossing them. A doubled-letter contour and a locally revised Z-to-T contour both remain possible: the oblique can supply the Z diagonal, but its separate lower bar and the chronology are obscured. Preserve T, double-struck T and tentative canceled-Z/T as local alternatives. The source T, parenthesized similarity and H_1, eta arch, double-stroked Z, single rightward arrow, high barred I, quotient slash and final T/ell remain unchanged.'
ev05='The final e after the deep looped g is a low compressed return. The dark detached point earlier in the word belongs over i; there is no separate stroke above the final e. Read envisage without a supplied acute. The following comma, nu comparison and physical séparé- / ment division remain. The upper angle and slanted lower bar map to the existing geqslant at the same coordinate.'
ev07='At the left of On, the independent long upright has a dark short upper cap and a lower rightward hook. It can be an opening square bracket, while its continuation into the larger cancellation leaves that punctuation role open. Retain a tentative opening bracket inside the canceled text. The horizontal strike crosses On va faire des; its letters, including the tall looped f and dotted i, remain readable. No closing bracket is supplied.'
ev08='The final short group lies on the horizontal cancellation, beside the descending bracket/block stroke. Its low entry and flattened following return support en, while the small central swelling can also admit car. The c/a/r bodies cannot be separated securely there. Preserve en/car within the cancellation rather than resolving the compressed group. The two l stems, dotted i forms, q descender and accent in the preceding words remain visible.'
ev09='Before the readable Ker is a separate densely hatched group with a K-like angled body and short low returns, retained as a tentative locally canceled Ker. The following taller K and low e/r run remain part of the larger canceled display. Each J has a short dark raised mark; the first is slightly upright and the second wedge-like. Their tiny solid bodies leave point/filled-zero/short-one/prime readings open, so C’s point/zero doubts are reopened and the blind one/prime possibilities retained. The clear raised 1 and hollow 0 in B10 provide the comparison without assigning a degree by mathematical expectation. Both low U/S and X/S, the single right arrow, closing parenthesis, wavy relation and G quotient are retained.'
ev10='The first relation has a wave over an unheaded lower bar. The second has two horizontal bars with no wavy upper component: restore equals there. The two-line isom / de Kummer annotation remains directly underneath that equality; its placement is already encoded by the underset, without asserting a separate revision chronology. After lim the heavier local hatch exposes a tall loop and short high bodies; the tentative ell^n reading remains, with the blind H-like trace recorded as unresolved evidence. The separate lower ell with raised n before the final parenthesis is retained. The original U’s closed entry, the J superscripts 1 and hollow 0, and the leftward limit arrow remain.'
ev14='The canceled group after Soit has a small upper body, a long lower descending return and an additional short upright obscured by its broad strike. Its rounded body and lower return admit q/g; retain those tentative letter readings rather than replacing the whole visible group by an illegibility token. The adjacent live x, two equality bars, g with dotted i and lower closed zero, (s) and comma remain unchanged.'
ev15='The oval O has a separate short underline; the low X has two dark crossing diagonals with lighter retracing, followed by the small comma and x. The detached final curve is tall enough for a closing parenthesis and also admits an elongated comma. Keep both local punctuation readings, with no opening parenthesis supplied. The underline bracing choices refer to the same single O and its separate low stroke.'
ev17='The shorthand has a short upper bar and a lower stroke beginning with a shallow cup before a long smooth plateau. Beside the pronounced cup/cusp/return at 070 P03 and 071 P04, this flattened contour does not securely expose an m cusp. It matches the unresolved flattened form at 055 P09. Reopen M1214 as equals/barred m, with equals first from this contour; no full même is written. The following broad-cap, descending-stem, left-return J and low looped f are retained at the same coordinates under the mathcal rendering.'
ev19='Mu has its long left descender and two upper branches, followed by two equality bars and long without a point. A descending stroke from the preceding line overlaps the next capital; its V-like arms are preferred but A remains possible locally. The quotient slash, g index, raised star and J_f parentheses remain. After them two short horizontal components are crossed by compact oblique strokes. Keep canceled equals versus a literal crossed inequality as a state alternative, with the local hatch favoring canceled equals. The separate dark point and later descending comma remain in that order.'
ev20='The first letter has a closed small e loop; the next has the short double-bend body of s, before the tall t and its lower return. These positive bodies give est. Entier has a low en run, tall t, separate i dot and e/r return. No point follows the final word. The source wording est entier is retained despite the preceding punctuation sequence.'
ev25='The raised mark above g has several dark crossing strokes and small loops; qualify the star locally because the retracing conceals its components. Inside the parentheses the J cap and hook are followed by the low f loop and long descender. The f’s rising return runs diagonally into the left side of the tall angular closing curve; the following detached lower curve is the comma. Mapping those connected strokes to the f return and closing parenthesis accounts for the apparent Lambda/A shape in the blind reading without adding another independent letter. Keep J_f followed by its closing parenthesis and the existing comma.'
c={x['id']:x for x in r['changes']}
c['P07a'].update(final=r'\unsure{en|car}',evidence=ev08,confidence='low')
for key in ['P08a','P08b']:
 x=c[key];x.update(final=sup,evidence=ev09,confidence='low',against_C=False,against_H=False)
 x['accounting_note']='C’s bullet/zero and H’s 1 remain explicit unresolved alternatives at this same superscript; no resolved witness correction is counted.'
 r['changes'].remove(x);r.setdefault('nonmaterial_observations',[]).append(x)
c['P09b'].update(final=r'\underset{\substack{\text{isom}\\\text{de Kummer}}}{=}',evidence=ev10,against_C=True,consequential=True)
c['P09c']['evidence']=ev10
c['P13a'].update(final=r'\deleted{\unsure{q|g}}',evidence=ev14)
c['P16a'].update(final=sh,evidence=ev17,against_C=False,confidence='medium')
c['P16a']['accounting_note']='C’s barred-m candidate remains unresolved beside equals; added or reordered alternatives alone are excluded against C. H’s expansion remains a material difference.'
c['P18b'].update(final=state+'. ,',evidence=ev19)
c['P19a'].update(final='est entier',evidence=ev20,against_C=True,against_H=False)
def add(cid,place,C,H,final,ev,crop,box,kind,cat,consequential=False):
 r['changes'].append(dict(id=cid,place=place,C=C,H=H,final=final,evidence=ev,crop=crop,box=box,confidence='high',against_C=True,against_H=True,kind=kind,error_category=cat,marked_in_H=False,consequential=consequential))
add('P04c','main line 5, final accent','envisagé','envisagé','envisage',ev05,'crops/149_scan077_B05_second.png',[280,550,1665,705],'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
add('P08c','first canceled display, local canceled group before Ker',r'\unsure{\operatorname{Ker}}',r'\operatorname{Ker}',r'\deleted{\unsure{\operatorname{Ker}}}\operatorname{Ker}',ev09,'crops/149_scan077_B09_second.png',[275,868,1550,1048],'omission','Omissions')
r['changes'][-1]['confidence']='low'
d=r['decisions'][0];d.update(decision='undecided',reading=sh,evidence=ev17,confidence='medium')
r['doubts']=[x for x in r['doubts'] if 'final-e accent' not in x['place']]
for x in r['doubts']:
 if 'numerator T' in x['place']:x.update(reading=dest,alternatives='T; double-struck T; tentative canceled Z before T',reason=ev04)
 if x['place']=='first canceled display, operator':x.update(reading=r'\deleted{\unsure{\operatorname{Ker}}}',alternatives='tentative Ker under the separate local hatch',reason=ev09)
 if 'internal canceled fragment after lim' in x['place']:x.update(reason=ev10,alternatives='tentative ell^n; H-like upright traces under the hatch remain unresolved')
 if 'fragment after Soit' in x['place']:x.update(reading=r'\deleted{\unsure{q|g}}',alternatives='q; g',reason=ev14)
 if 'sign after length' in x['place']:x.update(reading=state,alternatives='canceled equality; literal crossed inequality',reason=ev19)
for place,reading,alts,ev in [('B07, start of canceled block',r'\unsure{[}','opening bracket; block/cancellation contour',ev07),('P07, canceled final word',r'\unsure{en|car}','en; car',ev08),('P08, first raised J mark',sup,'solid point; 0; 1; prime',ev09),('P08, second raised J mark',sup,'solid point; 0; 1; prime',ev09),('P14, terminal punctuation',r'\unsure{)|,}','closing parenthesis; long comma',ev15),('P16 / M1214, prose shorthand',sh,'equals; barred m',ev17),('P18, capital after long',r'\unsure{V|A}','V; A',ev19),('B25, raised mark on g',r'\unsure{*}','tentative star under retracing',ev25)]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium' if place.startswith('P16') else 'low',reason=ev))
for x in r['inventory']:
 for a,b in repls:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
 if x['element']=='E07':x['first_words_or_objects']=r'\unsure{[}On va faire des calculs intrinsèques, \unsure{en|car}'
 if x['element']=='E08':x['first_words_or_objects']=ker
 if x['element']=='E10':x['position']=x['position'].replace('second similarity sign','second equality sign')
 if x['element']=='E15':x['position']='possible local cancellation versus literal inequality after the final length expression; P18 / B19'
r['inventory'].append(dict(element='E08a',kind='deletion',position='separate dense local hatch before the readable Ker inside the larger canceled first display; B09',first_words_or_objects=r'\deleted{\unsure{\operatorname{Ker}}}',sheet_kind='text',hand='his hand',transcribed='yes'))
r['inventory'].append(dict(element='E05a',kind='deletion',position='possible earlier Z layer among the unresolved destination-T contours in display (11); B04',first_words_or_objects=r'\unsure{T|\mathbb T|\deleted{\unsure{Z}}T}',sheet_kind='text',hand='his hand',transcribed='yes'))
for x in r['notation']:
 for a,b in repls:x['form']=x['form'].replace(a,b)
 if x['places']=='first canceled display, P08':x.update(form=r'\mathcal J^{'+sup+r'}_{U/S};\ \mathcal J^{'+sup+r'}_{X/S}',meaning='The two tiny raised J marks remain locally unresolved; the clear 1 and hollow 0 in the later expression are recorded as comparisons.')
 if 'M1214' in x['places']:x.update(form=sh,meaning='The unexpanded two-component prose shorthand, reopened as equals/barred m from the flattened lower contour.')
 if x['places']=='main line19, P18':x['meaning']='The final written length expression; its capital and the following crossed sign remain locally uncertain, and the separate point/comma sequence is retained.'
for x in r['hand']:
 if x['form']=='solid raised point / hollow0 / numeral1':x.update(observation=ev09,scope='The two ambiguous marks in P08 are compared with the visible 1/0 forms in P09 and P11.',witness_errors='C’s bullet/zero and H’s one readings remain unresolved at P08; these are excluded from material correction counts.')
 if x['form']=='numerator T with extra oblique':x.update(observation=ev04,witness_errors='The two witness readings remain candidates, with a further tentative local revision-layer alternative from the blind crop.')
 if x['form']=='compressed m and barred m':x.update(form=sh,observation=ev17,scope='P16 / M1214, compared explicitly with 055 P09, 070 P03 and 071 P04.',witness_errors='C’s candidate remains unresolved; H expands the shorthand to même.')
 if x['form']=='similarity and arrow endpoints':x['observation']+=' The second relation of P09 has two horizontal bars and now reads equals; its separate lower annotation keeps its position.'
 if x['form']=='accents and cancellation overlap':x.update(observation='The apostrophe and accent in s’avère are detached. The final e of envisage has no detached accent; the visible earlier dot belongs to i. The crossed accent in canceled isogénies remains. '+ev05,witness_errors='Both witnesses supply an acute on envisage. The physical séparé- hyphen is also retained.')
r['hand'].append(dict(form='f return beside an angular closing parenthesis',observation=ev25,places='B25',scope='This one connected contour; the neighboring f forms are not silently changed.',witness_errors='The blind reader proposed an extra Lambda/A; the continuous f return and closing curve account for the same ink in the retained expression.'))
for x in r.get('abbreviations',[]):
 if x.get('written')==r'\overline m':x['written']=sh
r['notes'][1]='[S077.2; canceled source] The large canceled passage begins with a tentative opening bracket and On va faire des calculs intrinsèques, followed by an unresolved en/car. It contains two displays, a separately hatched group before Ker and the below-equality annotation isom / de Kummer. It ends with On considère donc l’image inverse par and des isogénies. These are attributed source contents; no theorem is added.'
r['notes'][3]=r'[S077.4; source lower paragraph] The author writes x=g_{i_0}(s), A=\underline O_{X,x}, names V and the ideal expressions, and writes the final length expression beginning with mu. The capital after long remains V/A and the final crossed sign remains a state doubt. The closing words read est entier. This reports the page without supplying a continuation.'
r['notes'][8]='The larger bend before composé continues into the cancellation stroke. The source’s final closing parenthesis remains. The opening square bracket at the canceled block’s start is now tentative; no closing mate is supplied.'
r['notes'][10]=ev19
r['notes'].append('The independent audit changes twelve of twenty-five boxes after root inspection of all seventeen differences. It restores the second equality, unaccented envisage, est entier and a separate locally canceled Ker group; several compact signs and correction layers remain uncertain. M1214 is reopened by the cross-page contour comparison. This audit performs no additional mathematical check.')
r['deletion_insertion_review'][1]=ev07+' The whole block through des isogénies remains canceled; Je vais deviner and the later Soit paragraph remain live.'
r['deletion_insertion_review'][2]=ev09
r['deletion_insertion_review'][3]=ev10
r['deletion_insertion_review'][6]=ev14
r['deletion_insertion_review'][7]=ev19
r['open_issues']=['Thirteen local doubt entries remain explicitly listed, including both raised J marks, the flattened shorthand M1214, the numerator revision state, and the crowded canceled groups. Every blind difference has a root crop decision.']
for x in r['diff_coverage']:
 if x['row']==9:x['reason']='The final canceled group remains en/car; the horizontal strike obscures its joined bodies.'
 if x['row'] in [10,11]:x.update(status='unresolved alternatives; uncounted P08a/P08b',reason='C’s point/zero and H’s one remain explicit alternatives at the same raised mark; no resolved correction is counted. The separate earlier local hatch is recorded at P08c.')
 if x['row'] in [13,15]:x['reason']='The two-line annotation remains below the second relation, which has two horizontal equality bars. Its placement, absence of independent surrounding parentheses/points, and relation are recorded at P09b.'
 if x['row']==18:x['reason']='The partly visible canceled bowl and descending return are retained as tentative q/g.'
 if x['row']==21:x['reason']='M1214 is reopened as equals/barred m after explicit cross-page contour comparison; only H’s expansion remains counted.'
 if x['row']==23:x['reason']='A closed e loop, small s body and tall t support est, agreeing with H and changing C. The detached point is separately recorded at P18b.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,e):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=e)
def change(b,f,title,e):D[b]=dict(final=f,changed=True,decision=title,evidence=e)
change('B04',r'(11)\qquad T_\ell(\simeq H_1(\eta,\mathbb Z_\ell))\longrightarrow'+dest,'Keep the destination contour and possible revision layer open',ev04)
change('B05',r'cas envisage, $\nu\geqslant2$ (et traiter séparé-','Retain the unaccented final e',ev05)
change('B07',r'\deleted{\unsure{[}On va faire des}','Qualify the opening bracket',ev07)
change('B08',r'\deleted{calculs intrinsèques, \unsure{en|car}}','Keep the canceled final group open',ev08)
change('B09',r'\deleted{'+ker+'}','Restore the separate local hatch and reopen both raised marks',ev09)
formula=t[t.index(r'\deleted{H_1('):t.index('\n\\]',t.index(r'\deleted{H_1('))]
change('B10',formula,'Restore the second equality and retain the lower annotation',ev10)
keep('B12','Retain the same canceled map sequence','Both J/mathcal J spellings map to each visible broad cap, long stem and leftward lower turn, with a raised 1 and low U/S. Each eta has an upper arch and descending return; the two rightward maps through U and the later closing parenthesis agree. The long curve before composé joins the cancellation shaft; no independent opening parenthesis is added.')
change('B14',r'Soit \deleted{\unsure{q|g}} $x=g_{i_0}(s)$,','Preserve tentative canceled letter bodies',ev14)
change('B15',r'A=\underline O_{X,x}\unsure{)|,}','Keep the terminal punctuation alternatives',ev15)
change('B17',r'de $'+sh+r'$ $\mathcal J_f$','Reopen the flattened shorthand by cross-page comparison',ev17)
keep('B18','Retain the same crossed relation','The two short horizontal bars crossed by a near-vertical stroke are the one relation encoded by both ne and neq. The g bowl/descender, dotted low i, closed low 0, long looped f and detached comma occupy the same positions in both readings.')
change('B19',r'Soit $\mu=\operatorname{long}\unsure{V|A}/g_{i_0}^*(\mathcal J_f)\ '+state+r'$. ,','Keep the overlapped capital and crossed-sign state open',ev19)
change('B20','est entier','Read the visible e-s-t bodies',ev20)
keep('B22','Retain the same J and complete index','Plain J and mathcal J refer here to one broad cap, sloping right stem and looped leftward foot. The low i has a separate upper dot and lower stem, and the closed 0 is lower-right. These same glyph components and positions occur in both readings; no independent prime is supplied.')
keep('B23','Retain both objects and the labeled arrow','Both readings map A to the left crossbarred capital, V to the right two arms meeting below, and the arrow to the one rightward shaft/head. Above it the same g bowl/descender, dotted i, low 0 and raised crossed star give the label. Braces around the star and enclosing dollars add no glyph.')
keep('B24','Retain the same g and low index','The large g has an open upper bowl and connected long descender with its lower return; the adjoining i has a distinct dot and low stem, followed by a closed low zero. Both readings refer to these three source components. The enclosing dollar delimiters account for the token difference.')
change('B25',r'$g_{i_0}^{\unsure{*}}(\mathcal J_f)$,','Qualify the raised star and trace the connected f return',ev25)
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D))
record(page);assign('reader_c')
