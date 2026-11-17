from author import Page
p=Page('156-4',63)
p.replace(r'\unsure{ou|où}', 'ou')
p.replace('q.e.d.', 'qed.')
p.replace('Alors on a', r'Alors \unsure{on a|ou}')
p.replace(r'\deleted{\unsure{alors}}', r'\deleted{alors}')
p.replace(r'F_{\unsure{1|2}}', 'F_1')
p.replace(r'\unsure{lemme}', r'\unsure{lemme|Lemme}')
p.replace(r'\deleted{$\unsure{F=\coprod F_i}$}', r'\deleted{$F=\coprod F_i$}')
p.replace(r'\deleted{\unsure{et}}', r'\deleted{et}')
p.replace(r'\deleted{\unsure{finie}}', r'\deleted{fini}')
p.replace("\\unsure{``complém.res''|``comprises''|``compl. disj.''}", "\\unsure{``compl. dis''|``complém.res''|``comprises''}")
p.replace(r"l'ens \unsure{des|de} ses strates", "l'ens de ses strates")
p.replace(r'\deleted{$\unsure{F|F_0|F_i}$}', r'\deleted{$F$}')
p.replace("entre l'ens. des comp. conn.", "entre l'ens des comp. conn.")
p.replace('\n\nOn écrit', '\n\n'+r'\margin{\begin{tikzpicture}[x=1cm,y=1cm]\draw[line width=.45pt] (0,0) .. controls (.02,-.65) and (.01,-1.3) .. (.08,-1.65) .. controls (.13,-1.86) and (.04,-2.06) .. (.03,-2.12);\end{tikzpicture}}'+'\n\nOn écrit')
p.change('opening connector',r'\unsure{ou|où}','avec','ou','Two low connected curves form ou; no accent or letters av- precede them.','top',dc=True,kind='misread word')
p.change('opening parenthetical reference','(cf p. 57), inserted','(cf. p. 57), baseline','(cf p. 57), inserted','The reference is raised above the crossed G-prime / G-double-prime phrase; cf has no following point.','top',kind='insertion or placement')
p.change('opening cancelled phrase punctuation','disjoints,','disjoints','disjoints,','The descending comma after disjoints is crossed along with the phrase.','top')
p.change('opening line 2 final punctuation',"G''=G.","G''=G,", "G''=G.",'The narrow edge crop shows a compact point after the final G at the paper edge.','top_edge')
p.change('proof ending','q.e.d.','cqfd.','qed.','Three joined letters q, e, d are followed by one point; no internal points or initial c are visible.','top',dc=True,kind='abbreviation expanded or spelling modernised')
p.change('Corollary 1 heading','Corollaire underlined, 1 outside underline','Corollaire 1 underlined','Corollaire underlined, 1 outside underline','The horizontal underline ends below the word before the separate numeral.','cor1')
p.change('Corollary 1 after Alors','on a','ou',r'\unsure{on a|ou}','A short low wave is followed by a separate compact ink mark; compression prevents a secure choice between the two readings.','cor1_alors',dc=True,kind='misread word',confidence='low')
p.doubt('Corollary 1 after Alors','on a|ou','The low wave and separate dark mark are too compressed to settle the connector','cor1_alors','low')
p.change('Corollary 1 disjunction punctuation','F_0=F_1 ou','F_0=F_1, ou','F_0=F_1 ou','There is no comma between the first F_1 and ou.','cor1')
p.change('Corollary 1 cancelled adverb',r'\unsure{alors}',r'\ill{}','alors, deleted','The tall l loop and following rounded o survive below the horizontal strike; the ending bends down.','cor1_formula',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.change('Corollary 1 raised replacement','dans ce cas, inserted','dans ce cas, uncertain insertion','dans ce cas, inserted','Three groups are visible above the deleted adverb: the d loop, ce, and the final low cas.','cor1_formula',kind='other',confidence='medium',marked='yes')
p.change('Corollary 1 second summand',r'F_{\unsure{1|2}}','F_1','F_1','The index has a single downward stem and a straight basal foot, without the upper curved turn of 2.','cor1_formula',dc=True,dh=False,kind='misread symbol or index',confidence='medium')
p.change('Corollary 1 old letter under H',r'\deleted{\unsure{G|F}}H','H, deleted',r'\deleted{\unsure{G|F}}H','An older curved body is overwritten by the two vertical stems of H; its identity remains obscured.','cor1_formula',kind='omission',confidence='low')
p.doubt('Corollary 1 old letter under H','G|F','The overwrite covers the upper and middle strokes of the earlier letter','cor1_formula','low')
p.change('Corollary 1 final summand',r'\amalg H live',r'\amalg H deleted',r'\amalg H live','The only continuous horizontal line is the base of the amalgamation sign; no cancellation crosses that sign and H.','cor1_formula',kind='deletion state (struck given live or live given struck)',consequential='The final amalgamation with H in Corollary 1 remains live.')
p.change('left of Corollary 1','omitted','vertical bracket described in note','curved vertical rule reproduced in TikZ','One thin rule descends beside the statement, bends slightly right, and returns left near its lower end.','cor1',dc=True,kind='drawing or diagram')
p.change('Corollary 1 proof','on applique lemme?',r'on \ill{} que G \ill{}',r'on applique \unsure{lemme|Lemme}','The doubled descending p strokes, l, i point, and q descender spell applique; the following word has l/e/m/m/e strokes, with initial case uncertain.','proof_end',dc=True,kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.doubt('Corollary 1 proof ending','lemme|Lemme','The initial open tall curve does not securely establish case','proof_end')
p.change('Corollary 2 cancellation state','whole paragraph deleted','main text live; note reports cancellation','whole paragraph deleted','Long oblique cancellation strokes cross the heading, body and final decomposition.','cor2_top',kind='deletion state (struck given live or live given struck)')
p.change('Corollary 2 family index',r'\unsure{j|i}\in I',r'i\in I',r'\unsure{j|i}\in I','The first index has a curved low hook, but the small upper mark and its baseline remain ambiguous.','cor2_top',kind='misread symbol or index',confidence='low')
p.doubt('Corollary 2 family index','j|i','The curved low stroke favours j, but the small index is compressed','cor2_top','low')
p.change('Corollary 2 pairwise qualifier','disjointes','distinctes','disjointes','After dis-, a j descender and rounded o precede the n and t; the word ends -tes.','cor2_top',kind='misread word',confidence='medium')
p.change('Corollary 2 earlier formula',r'\unsure{F=\coprod F_i}',r'F_0\amalg F_1',r'F=\coprod F_i','The first F is followed by two short equal strokes beneath the cancellation, then the large coproduct sign and F with a small i.','cor2_oldformula',dc=True,kind='misread symbol or index',confidence='medium')
p.change('Corollary 2 construction phrase','la figure engendrée par les F_i est leur somme disjointe',r'\ill{} figures \ill{} par les F_i est \ill{} réunion disjointe','la figure engendrée par les F_i est leur somme disjointe','The singular figure, long g descender in engendrée, leur, and low connected somme are individually visible between the long cancellation strokes.','cor2_middle',kind=r'readable ink left as \ill{}',marked='yes')
p.change('Corollary 2 small cancelled connector',r'\unsure{et}','omitted','et, deleted','A small e loop and short t stroke lie below the coproduct line immediately before subset F.','cor2_middle',dc=True,kind='omission',confidence='medium')
p.change('Corollary 2 earlier adjective',r'\unsure{finie}','fini','fini, deleted','The separate dot and short vertical final i are followed by clear space; there is no terminal e.','cor2_fini',dc=True,dh=False,kind='misread word')
p.change('cancelled observation opening',"Il n'est pas évident que tte figure non vide ait une composante connexe",r"Je n'ai pas pu déduire que ... figure ... soit ... comp. connexes", "Il n'est pas évident que tte figure non vide ait une composante connexe",'The opening Il, apostrophe and est, p descender of pas, accented évident, abbreviated tte, and the continuous singular composante connexe are visible.','old_observation',kind='misread word')
p.change('cancelled observation state','whole paragraph deleted','fragments partly live, with cancellation note','whole paragraph deleted','The same long diagonal cancellation strokes extend through this paragraph and the raised replacement.','old_observation',kind='deletion state (struck given live or live given struck)')
p.change('cancelled observation earlier difficulty',r"la difficulté étant dans l'\unsure{existence} \unsure{ou}",r'fragmentary \ill{} text',r"la difficulté étant dans l'\unsure{existence} \unsure{ou}",'The two f ascenders in difficulté and the letters étant dans are readable beneath the horizontal strike. The remainder overlaps the replacement figures and stays uncertain.','old_observation',kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.doubt('cancelled observation after dans', 'existence','The later insertion and horizontal strike cover the middle and end of the word','old_existence_full','low')
p.doubt('cancelled observation after existence','ou','Only two small low curves remain beneath the crossing text','old_existence_full','low')
p.change('cancelled observation continuation',r'\unsure{à} des sous-figures',r'fragments ... des ... sous-figures',r'\unsure{à} des sous-figures','The small initial rounded a is visible but its accent is covered; des and the full hyphenated sous-figures remain readable.','old_compl',kind=r'readable ink left as \ill{}',confidence='medium',marked='yes')
p.doubt('cancelled observation continuation','à','The cancellation passes through the accent position of the initial a','old_compl','low')
p.change('cancelled observation quoted qualifier',"\\unsure{``complém.res''|``comprises''|``compl. disj.''}",r'« \ill{} »',"\\unsure{``compl. dis''|``complém.res''|``comprises''}",'Two upper quote strokes surround the damaged phrase. The p descender and a separated d-like loop support compl. dis as first reading; heavy crossing leaves alternatives open.','old_compl_word',dc=True,kind=r'readable ink left as \ill{}',confidence='low',marked='yes')
p.doubt('cancelled observation quoted qualifier',"``compl. dis''|``complém.res''|``comprises''",'Horizontal and oblique cancellation strokes cover the letter joins; the tall line above belongs partly to the interlinear insertion','old_compl_word','low')
p.change('cancelled observation interlinear replacement','Mais c\'est vrai pour les figures de t.f., et a fortiori pour les figures finies. Les','fragmentary Mais ... et ... pour les ... figures finies. Les',"Mais c'est vrai pour les figures de t.f., et a fortiori pour les figures finies. Les, inserted then cancelled",'The raised Mais c’est vrai, figures, t.f. with points, a fortiori, and the continuation figures finies. Les are readable between the earlier lines.','old_observation',kind=r'readable ink left as \ill{}',marked='yes')
p.change('Proposition inclusion insertion',r'\inserted{\subset M}',r'\subset\mathcal M baseline',r'\inserted{\subset M}','Subset M is placed above the line and joined down to the end of A=bar F by a curved insertion leader. M has two plain tall humps.','prop',kind='insertion or placement')
p.change('Proposition first ens punctuation',"l'ens", "l'ens.", "l'ens",'No separate point follows the final low stroke of ens.','prop')
p.change('Proposition strata phrase',r'\unsure{des|de} ses strates','de ses strates','de ses strates','The short e after the d loop ends before the separate ses; no additional s stroke is present.','prop',dc=True,dh=False,kind='misread word',confidence='medium')
p.change('Proposition old figure letter',r'\unsure{F|F_0|F_i}','F_0','F, deleted','The old F stands above the baseline word figure and is crossed by a horizontal stroke. The loop underneath belongs to figure; no independent subscript follows F.','prop_oldF',dc=True,kind='misread symbol or index',confidence='medium')
p.change('Proposition criterion abbreviation','il f et s','il faut et il suffit','il f et s','A single f with long descender and a single s flank et; the full expanded words are absent.','prop_bottom',kind='abbreviation expanded or spelling modernised')
p.change('Proposition ordered-set abbreviation',"l'ens ordonné", "l'ens. ordonné", "l'ens ordonné",'The short final stroke of ens continues to its endpoint without a detached period.','prop_bottom')
p.change('Proposition final set abbreviation',"entre l'ens. des", "entre l'ens. des", "entre l'ens des",'The final ens has a low terminal stroke followed by a clear gap before des; no detached period is visible.','prop_bottom',dc=True)
p.change('Proposition last words','comp. conn.','composantes','comp. conn.','The page ends with two short groups, comp with its p descender and point, then conn with a final point.','prop_bottom',kind='abbreviation expanded or spelling modernised')
p.inventory([
 ('text','top','En effet, G=G′ amalg G″'),
 ('deletion','top, line 2','G′ et G″ disjoints,'),
 ('insertion','top, above line 2','(cf p. 57)'),
 ('text','upper middle','Corollaire 1 Soient F_0,F_1'),
 ('deletion','Corollary 1 heading','Deux'),
 ('deletion','Corollary 1 final line','alors'),
 ('insertion','Corollary 1 above final line','dans ce cas'),
 ('deletion','Corollary 1 final H','old G|F'),
 ('drawing','left of Corollary 1','single curved vertical rule'),
 ('text','under Corollary 1','On écrit F=F_0 amalg G'),
 ('deletion','central block','Corollaire 2 Soit (F_i)'),
 ('deletion','Corollary 2 earlier formula','F=coprod F_i'),
 ('deletion','Corollary 2 before subset F','et'),
 ('deletion','Corollary 2 parenthesis','fini'),
 ('deletion','under Corollary 2','Il n’est pas évident que tte figure'),
 ('deletion','observation earlier continuation','la difficulté étant dans l’existence ou'),
 ('deletion','observation next earlier line','à des sous-figures'),
 ('insertion','between observation lines','Mais c’est vrai pour les figures de t.f.'),
 ('deletion','whole replacement continuation','Mais c’est vrai ... figures finies. Les'),
 ('text','bottom block','Proposition Soit F une figure'),
 ('insertion','above proposition first line','subset M and curved leader'),
 ('deletion','proposition second line','Alors l’application'),
 ('deletion','proposition above figure','F'),
])
p.notation('coproduct sign',r'\coprod','Two vertical stems joined by a long horizontal baseline, in the cancelled Corollary 2.')
p.r['abbreviations']=[dict(abbreviation=a,expansion=b,evidence='156-4:063; visible manuscript form retained') for a,b in [('qed.','quod erat demonstrandum'),('comp. conn.','composante(s) connexe(s)'),('tte','toute'),('t.f.','type fini'),('il f et s','il faut et suffit'),('ens','ensemble'),('corr.','correspondance')]]
p.save()
