"""Root crop adjudication of every fixed blind scan 076 difference."""
from pathlib import Path
import json
from write_audit_decisions import main
from record_audit import record
from assign_audit import assign
B=Path(__file__).resolve().parents[1];page='149_scan076';rp=B/'reviews'/f'{page}.json';r=json.loads(rp.read_text());assert not r.get('audit');p=B/'pages'/f'{page}.tex';t=p.read_text()
fgroup=r'\deleted{\unsure{$f_0$|$f$ un|$f$ une}}'
upper=r'\deleted{\unsure{et|est} le \unsure{groupe|point image|point générique} de}'
lower=r"\deleted{par l'homomorphisme\unsure{,}}"
repls=[('schéma,',r'schém\unsure{a|.},'),(r'\deleted{$\unsure{f_0}$}',fgroup),(r'f\vert K(s)',r'f\unsure{\vert|(}K(s)'),(r'\deleted{Considérons}',r'\deleted{\unsure{Considérons}}'),(r'\inserted{\deleted{Donc}}',r'\inserted{\deleted{\unsure{Donc|Dans}}}'),(r'\deleted{et le groupe de}',upper),(r"\deleted{par l'homomorphisme}",lower),(r'\pi_1(\eta)\longrightarrow\pi_1(U)',r'\Pi_1(\eta)\longrightarrow\Pi_1(U)'),(r'\deleted{\unsure{donc}}',r'\deleted{\unsure{donc|(donc}}'),(r'\inserted{si $\nu\geq2$,}',r'\inserted{\uline{si $\nu\geq2$},}'),(r'\& H_1(\eta,\mathbb Z_\ell) \arrow[r]',r'\& H_1\unsure{(}\eta,\mathbb Z_\ell) \arrow[r]'),(r'\arrow[ur,"\sim"]',r'\arrow[ur,"\unsure{\sim}"]'),(r'\inserted{[H_1(U_s,\mathbb Z_\ell)]}',r'\inserted{[H_1(U_s,\mathbb Z_\ell\unsure{)}]}'),(r'\deleted{tout}',r'\deleted{\unsure{tout}}'),(r'$\ell=$ nb',r'$\ell\unsure{=|:=}$ nb'),('caracteris-',r'caract\unsure{eris|is}-')]
for a,b in repls:
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
p.write_text(t)
ev01='The word has s/c, a tall h, the compressed e/m run and a separate dark accent. Its last compact oval-like blob admits a collapsed a or an abbreviation stop; retain a/point locally. The later detached mark has a dark descending curved tail. The faint spot above that tail is much paler than the writing and does not secure a semicolon. Keep the comma.'
ev03='The tall looped f, its short crossbar and the long cancellation are clear. To the right, a shallow cup, low shoulder/line and terminal dark oval lie under the strike. They admit the original low 0 reading or the short un/une sequence supplied by the blind reader; preserve all at the same canceled extent. The live dotted i, low 0, membership sign and capital I with its two bars remain outside the strike.'
ev05='The separate upright between f and K is heavily retraced and bends at its lower foot; its straight-bar versus opening-parenthesis form remains open. K has a tall stem and two angled right arms at the same level as (s), rather than an index below f. The g has a rounded upper bowl and long descender; a small separate i stroke/dot and low closed zero follow it. Preserve that full g_i0 index and the two equality bars beneath the cancellation.'
ev06='The two canceled rows have independent horizontal strikes. The baseline begins with a large C, a low compressed on/s run, a dotted upright and a tall d loop; its crowded remaining bodies leave Considérons tentative. The raised word has a large D and a short low ending whose o/a and n/c/s joins remain masked, so Donc/Dans stays open. Its higher placement is preserved as an insertion that was canceled. The later live Si eta=S minus {s} has a large two-loop S, dotted i, eta arch/descender, two equality bars and both braces. The detached curved tail below/right of the closing brace is the existing comma.'
ev07='Two canceled baselines survive separately. At the upper left the low e loop and tall terminal peak admit et/est where the strike merges the middle; le has its own tall loop. The following long crossed group contains an upper loop with a deep descending return, several flattened short bodies and a second descender; the first groupe reading and the blind point image/point générique alternatives cannot all be separated confidently under this strike. Keep those alternatives before the clear d/e ending. The lower row reads par l’homomorphisme from its tall l/h stems, o loops, low m shoulders, p descender and dotted i; a short downward terminal hook may include a comma, kept tentative within cancellation.'
ev09='Both symbols have a broad nearly flat top bar extending across two long essentially straight legs; neither has the upturned right foot seen in the small pi comparison at 060 P01. Their positive broad-top/straight-leg contour matches the capital Pi forms at 054 P10. Retain capital Pi twice, with the same separate low 1s, eta/U arguments, parentheses, single rightward arrow and final point. This is a glyph-case decision, without identifying or changing the source’s groups.'
ev10='The large initial open curve can be the leading part of the tentative word or a separate opening parenthesis before it. Thick cancellation hides its junction with the low medial bodies. Retain donc/(donc at this one canceled extent; no closing parenthesis is supplied.'
ev11='The baseline abbreviation has one distinct upper bar and a lower cup/cusp body with a long return; preserve barred m without expanding it to même. Beneath the raised si nu>=2 there is a separate wavy underline ending before its comma. A second, longer leader begins at the right, descends diagonally left and then vertically to the gap before que. Restore the underline while preserving that independent attachment and the raised comma.'
ev13='All four objects and all three connectors were inspected. The main shaft points right; the lower-left short oblique shaft meets a two-sided head directed toward the first H_1; its tiny separate bent/looped label remains tentative sim. The lower-right shaft has an upward head with a separate bent label on its right, retaining the resolved sim of M1213. The opening curve before the first eta merges with eta’s entry and is now tentative. At the lower-right term, overlapping round/square returns leave the inner closing parenthesis uncertain; the square bracket is retained. The two lower objects remain inserted at their visible positions, and bar/hat above K stays unresolved.'
ev14='The opening parenthesis and pour are live. The detached slanting mark below its end has a dark head and descending tail in the gap before the next word; retain the comma. In canceled tout, both tall t strokes survive, while the o/u joins are covered by several heavy horizontal strokes. Qualify the canceled word.'
ev15='The looped ell is followed by two short horizontal equality components and a small detached low mark to their left. That low mark leaves an equals/colon-equals reading open; a complete separate colon cannot be secured. Preserve the alternatives. The following low n and tall b have no separate terminal stop. Premier continues on the same baseline and was already present in the full transcription.'
ev16='The c/a/r/a/c and tall t are followed by a very compressed low return before the clearly dotted i and angular s. The er bodies cannot be separated securely from the t return, so eris/is remains open. No separate acute is visible there; the detached high dark point sits over i. The terminal s and detached line-end hyphen remain, followed by tique on the next physical line.'
c={x['id']:x for x in r['changes']}
c['P01'].update(final=r'schém\unsure{a|.},',evidence=ev01,confidence='medium')
c['P03'].update(final=fgroup,evidence=ev03)
c['P05'].update(final=r'\deleted{$f\unsure{\vert|(}K(s)=g_{i_0}$}',evidence=ev05,confidence='medium')
c['P06a'].update(final=r'\inserted{\deleted{\unsure{Donc|Dans}}}',evidence=ev06,confidence='medium')
c['P07'].update(final=upper+' '+lower,evidence=ev07,against_C=False,confidence='low')
c['P07']['accounting_note']='C’s groupe-de uncertainty is reopened; added alternatives and certainty changes alone are excluded against C. The recovered canceled lower clause still differs materially from H’s illegible span.'
c['P09'].update(final=r'$\Pi_1(\eta)\longrightarrow\Pi_1(U)$.',evidence=ev09,against_C=True)
c['P10'].update(final=r'\deleted{\unsure{donc|(donc}}',evidence=ev10)
c['P11b'].update(final=r'$\overline m$, \inserted{\uline{si $\nu\geq2$},} que pour',evidence=ev11,against_C=True)
c['P13a'].update(final=r'H_1\unsure{(}\eta,\mathbb Z_\ell)',evidence=c['P13a']['evidence']+' The opening parenthesis merges with eta’s entry in the independent crop and is retained tentatively.',confidence='medium')
diag=t[t.index(r'\diagram{'):t.index("n'est pas trivial (pour")].strip()
c['P13b'].update(final=diag,evidence=ev13)
c['P14b'].update(final=r'\deleted{\unsure{tout}}',evidence=ev14,confidence='low')
c['P15'].update(final=r'$\ell\unsure{=|:=}$ nb',evidence=ev15,confidence='medium')
c['P16'].update(final='caract'+r'\unsure{eris|is}-\newline'+'\ntique',evidence=ev16)
for x in r['doubts']:
 if x['place'].startswith('P03,'):x.update(reading=fgroup,alternatives='f_0; f un; f une under the strike',reason=ev03)
 if x['place'].startswith('P10,'):x.update(reading=r'\deleted{\unsure{donc|(donc}}',alternatives='donc; (donc',reason=ev10)
newd=[('P01, terminal a/stop',r'schém\unsure{a|.}','a; abbreviation point',ev01),('P05, upright before K',r'\unsure{\vert|(}','upright bar; opening parenthesis',ev05),('P06, canceled baseline word',r'\deleted{\unsure{Considérons}}','tentative Considérons',ev06),('P06, raised canceled word',r'\inserted{\deleted{\unsure{Donc|Dans}}}','Donc; Dans',ev06),('P07, canceled opening',r'\unsure{et|est}','et; est',ev07),('P07, canceled medial group',r'\unsure{groupe|point image|point générique}','groupe; point image; point générique',ev07),('P07, terminal canceled punctuation',r'\deleted{\unsure{,}}','comma; terminal pen return',ev07),('P13, first opening parenthesis',r'H_1\unsure{(}\eta','opening parenthesis; merged eta entry',ev13),('P13, lower-right inner closing parenthesis',r'\mathbb Z_\ell\unsure{)}]','inner closing parenthesis; square-bracket return only',ev13),('P13, diagonal-arrow label',r'\unsure{\sim}','tentative similarity label',ev13),('P14, canceled tout',r'\deleted{\unsure{tout}}','tentative tout',ev14),('P15, equality and detached low mark',r'\ell\unsure{=|:=}','equals; colon-equals',ev15),('P16, compressed medial letters',r'caract\unsure{eris|is}-','caracteris-; caractis-',ev16)]
for place,reading,alts,ev in newd:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=ev))
for x in r['inventory']:
 for a,b in repls:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,b)
 if x['element']=='E03':x['first_words_or_objects']=fgroup
 if x['element']=='E07':x['first_words_or_objects']=r'\unsure{Considérons}'
 if x['element']=='E08':x['first_words_or_objects']=r'\deleted{\unsure{Donc|Dans}}'
 if x['element']=='E10':x['first_words_or_objects']=upper
 if x['element']=='E11':x['first_words_or_objects']=lower
 if x['element']=='E12':x['first_words_or_objects']=r'\unsure{donc|(donc}'
 if x['element']=='E13':x['first_words_or_objects']=r'\uline{si $\nu\geq2$},'
 if x['element']=='E15':x['first_words_or_objects']=r'H_1\unsure{(}\eta,\mathbb Z_\ell)\longrightarrow H_1(U,\mathbb Z_\ell)'
 if x['element']=='E17':x['first_words_or_objects']=r'[H_1(U_s,\mathbb Z_\ell\unsure{)}]'
 if x['element']=='E18':x['first_words_or_objects']=r'\unsure{tout}'
for x in r['notation']:
 for a,b in repls:x['form']=x['form'].replace(a,b)
 if x['places']=='P15–P16 and following main line':x['meaning']='The source description of ell retains nb and the physical word break; equality punctuation and compressed medial letters remain locally uncertain.'
r['notation'].append(dict(form=r'\Pi_1(\eta)\longrightarrow\Pi_1(U)',meaning='The two broad-top, straight-leg capital Pi forms in this written relation, with their low 1s and local arguments.',places='P09, both objects'))
for x in r['hand']:
 if x['form']==r'\pi_1':x.update(form=r'\Pi_1',observation=ev09,scope='Both P09 occurrences; explicit comparison to 054 P10 and 060 P01.',witness_errors='Both C and H render these two broad-top symbols as small pi; the capital case is retained from the crop.')
 if x['form']=='Insertion leaders':x['observation']+=' '+ev11
 if x['form']=='caracteris-':x.update(form=r'caract\unsure{eris|is}-',observation=ev16)
r['notes'][6]='Graphical review: all four diagram objects and three arrow directions are retained. The diagonal-arrow label, first opening parenthesis and lower-right inner closing parenthesis remain tentative. The separate label beside the upward arrow retains sim. These observations record visible layout, without an additional mathematical check.'
r['notes'][7]='The physical line-end hyphen remains before tique; compressed eris/is and the local equality mark are now doubtful. The source has no secure acute over that compressed run. No point is supplied after the raised (0,1), and the comma after the added S minus {s} remains.'
r['notes'].append('The independent audit changes twelve boxes, including several qualifications of obscured canceled letters. It restores the raised underline and capital Pi twice. Fixed blind files preserve both readings, and all twenty-three differences have root crop decisions. C’s canceled groupe-de doubt is reopened and its earlier resolved-doubt count is removed. The existing singleton quotient computation is unchanged; no further mathematical check was performed.')
for i,ev in [(1,ev03),(3,ev05),(4,ev06),(5,ev07),(6,ev10),(7,ev11),(9,ev13),(10,ev14)]:r['deletion_insertion_review'][i]=ev
r['open_issues']=['Sixteen local doubt entries are enumerated in doubts, including canceled-word alternatives, two diagram parentheses and its tiny diagonal label, terminal a/stop, a retraced upright, equality punctuation and compressed er/is letters. M1212 remains undecided; M1210, M1211 and M1213 retain their resolved readings.']
for x in r['diff_coverage']:
 if x['row']==4:x['reason']='The fragment is canceled, with clear f and unresolved low 0/un/une ink. The candidate alternatives remain explicit.'
 if x['row']==7:x['reason']='The tall stroke before baseline capital K is retained as bar/open-parenthesis uncertainty. K(s) is at the main level; the relation remains canceled.'
 if x['row']==8:x['reason']='The raised canceled Donc/Dans and baseline Considérons are locally tentative. The later Si eta formula and its comma remain live.'
 if x['row']==9:x['reason']='The two canceled baselines remain separate. The upper medial word is reopened as groupe/point image/point générique; its previous resolved-C-doubt count is removed. The lower homomorphisme clause remains readable.'
 if x['row']==12:x['reason']='Both broad-top straight-leg glyphs are capital Pi; low 1s, eta/U arguments, arrow and terminal point remain.'
 if x['row']==14:x['reason']='The raised condition is underlined with a separate low stroke; its distinct longer leader attaches after the shorthand comma before que.'
 if x['row']==15:x['reason']='The canceled extent remains tentative donc/(donc; no closing parenthesis is supplied.'
 if x['row']==24:x['reason']='The tiny diagonal-arrow label is retained as tentative sim; the arrow and its inserted object remain in the diagram. H’s placement prose is editorial.'
 if x['row']==27:x['reason']='Pour comma, tentative canceled tout, ell equals/colon-equals nb and the physical line break in caract-eris/is remain recorded from the crops.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
D={}
def keep(b,title,e):D[b]=dict(keep_first=True,changed=False,decision=title,evidence=e)
def change(b,final,title,e):D[b]=dict(final=final,changed=True,decision=title,evidence=e)
change('B01',r'schém\unsure{a|.},','Qualify the terminal word body and keep the comma',ev01)
keep('B02','Retain the same raised qualification','The single raised sentence, genus letter g, nu=card I and paired (g,nu) versus (0,1) are the same in both readings. Ne and neq map to the same two horizontal bars traversed by one oblique stroke. Dollar and parenthesis math delimiters encode identical glyph positions; the source has no added terminal point.')
change('B03',fgroup+r' $i_0\in I$,','Broaden the low canceled fragment alternatives',ev03)
keep('B04','Retain the same canceled word and raised replacement','The lower disjointe is crossed by one long stroke. Above it de X/S distincte remains live, with its leader returning to the section phrase. The two math delimiter choices enclose the identical X, slash and S at the same location.')
change('B05',c['P05']['final'],'Qualify the retraced upright and retain the full index',ev05)
change('B06',r'\deleted{\unsure{Considérons}} \inserted{\deleted{\unsure{Donc|Dans}}} \inserted{Si $\eta=S\setminus\{s\}$,}','Qualify both canceled words and preserve the live comma',ev06)
change('B07',upper+' '+lower,'Reopen the crowded canceled clause',ev07)
keep('B08','Retain the same eta-to-U map','The eta has a short entry and arch with a long descending return. The open-entry U follows a single rightward shaft and head. Both readings contain these same three elements; only their enclosing math delimiters differ.')
change('B09',c['P09']['final'],'Retain the two capital Pi glyphs',ev09)
change('B10',c['P10']['final'],'Keep the initial-curve interpretation open',ev10)
change('B11','et '+c['P11b']['final'],'Restore underlining and preserve the abbreviation',ev11)
keep('B12','Retain ell donné from its component strokes','The first group is a single looped ell with one lower foot; no separate e follows it. The next has a d bowl and tall stem, closed o, two low joined n shoulders and a terminal accented e. Those bodies support donné. The long stroke from the line above overlaps the final region without supplying the extra r/i/r sequence of dernier or the v/i/t sequence of devient.')
change('B13',diag,'Keep the diagram and localize three uncertainties',ev13)
change('B14',r'(pour, \deleted{\unsure{tout}}','Qualify the canceled word',ev14)
change('B15',r'$\ell\unsure{=|:=}$ nb','Keep the small equality-mark alternatives open',ev15)
change('B16',r'caract\unsure{eris|is}-','Qualify the compressed medial letters',ev16)
keep('B17','Retain the same J expression','The connected broad top return and long lower loop form J; the raised 1 and lower X/S remain separately visible. Both readings give the same expression and differ only in math delimiters. No detached hat is supplied.')
keep('B19','Retain the identical complete homology expression','The H with low 1, opening parenthesis, large looped J with raised 1 and low X/S, comma, doubled-diagonal Z with low ell and closing parenthesis occupy the same positions in both readings. There is one expression here and no additional connector.')
keep('B20','Retain the identical eta expression','Both readings preserve H_1, the opening parenthesis, eta’s arch and long return, comma, double-stroked Z with low looped ell and the closing parenthesis. The math delimiter spelling alone differs.')
keep('B21','Retain both visible Z-to-T revisions','In each quotient factor the pale Z diagonal and lower horizontal survive beneath the dark central T stem and upper bar. Both readers preserve both layers. The low ells, raised barred I, quotient slash and final point agree; braces around I and math delimiters encode the same ink.')
keep('B23','Retain the live g with its low i_0','The live g has a small open upper bowl, a long downstroke and an upward returning lower branch; its continuous path differs from a separate central stem through a closed phi oval. The adjoining i is dotted and its zero is a separate low loop. Compare the closed upper bowl and descending g in the canceled B05 expression. The first f has its own tall loop and long lower return, with et between the symbols.')
D['B24']=dict(final=r'$H_1(U,\mathbb Z_\ell)\bigl(\xleftarrow{\sim}H_1(U_s,\mathbb Z_\ell)\bigr)$,',changed=False,decision='Retain the complete expression and existing comma',evidence='The second H_1 term sits to the right of a leftward single-headed arrow with a separate tilde above it, all inside outer parentheses. Both low 1s, U_s index and Z/ell terms agree. The following comma was already in the complete page; the blind excerpt includes it, while the first excerpt ended at the parenthesis.')
D['B25']=dict(final=r'$\operatorname{card}I=1$,',changed=False,decision='Retain the cardinality expression and existing comma',evidence='The source has c/a/r/d, capital I with upper/lower bars, two equality strokes and one upright numeral, followed by a descending comma. That comma was already present in the page beyond the first excerpt. Both readings select the same expression.')
main(dict(page=page,root_viewed=[f'crops/{page}_{b}_second.png' for b in D],decisions=D));record(page);assign('reader_b')
