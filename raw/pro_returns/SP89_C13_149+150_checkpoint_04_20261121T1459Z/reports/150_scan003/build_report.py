from pathlib import Path
import json, re, csv

ROOT = Path('/workspace/scratch/8759b8008681')
OUT = ROOT / 'work/reports/150_scan003'
C = (ROOT / 'packets/150_scan003/C.tex').read_text()
H = (ROOT / 'packets/150_scan003/H.tex').read_text()
D = (OUT / 'draft.tex').read_text()
BOXES = json.loads((OUT / 'crop_boxes.json').read_text())
changes = []
def norm(s):
    return s.replace('<<Q>>', chr(96)*2).replace('<<R>>', "''").replace('’', "'")
def flat(s):
    return ' '.join(s.split())
cats = {
 'misread word':'2', 'misread symbol or index':'1', 'omission':'3',
 'text not on the page':'9',
 'deletion state (struck given live or live given struck)':'7',
 'insertion or placement':'6', 'abbreviation expanded or spelling modernised':'8',
 r'readable ink left as \ill{}':'5', 'drawing or diagram':'4', 'other':'10'
}
def A(id, place, c, h, final, evidence, confidence='high',
      kind='misread word', against_c=False, against_h=True, consequential=False,
      crop=None):
    c,h,final=map(norm,(c,h,final))
    p = crop or re.match(r'P\d+',id).group()
    changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,
        crop=f'crops/150_scan003_{p}.png',box=BOXES[p],confidence=confidence,
        kind=kind,against_c=against_c,against_h=against_h,
        marked_in_h=any(x in h for x in [r'\uncertain',r'\ill', '(?)', 'doute']),
        consequential=consequential,error_category=cats[kind]))

A('P01','Top operator after spécialisation',
 r'\unsure{\operatorname{Ord}(X)|\operatorname{Spéc}(X)}',
 r'\mathrm{Spéc}(X)',
 r'\unsure{\operatorname{Ord}(X)|\operatorname{Spéc}(X)}',
 'Overtraced O/S-like opening and p-like older strokes coexist with a tall final d. The layers do not separate enough to establish either one clean word or a deletion sequence. Retained unresolved difference, not a resolution.',
 'low','misread word',False,True,True)
A('P02','Raised prefix before first ordonné',
 r'\inserted{pré}ordonné',r'\supplied{pré}ordonné',
 r'\inserted{pré}ordonné',
 'A small raised p with descender, r and accented é is written above the baseline with a curved attachment; the prefix is actual ink.',
 kind='insertion or placement')
A('P03','Separation axiom, inner parentheses',
 r"l'axiome de séparation $(T_0)$)",r"l'axiome de séparation $T_0$)",
 r"l'axiome de séparation $(T_0)$)",
 'An opening curve before T and a separate close after the lowered 0 enclose the axiom; a further close ends the prose parenthesis.',
 kind='misread symbol or index')
A('P05a','Beginning of preorder-to-space construction',
 r'$I$ ens \inserted{pré}ordonné',r'$I$ ens. \supplied{pré}ordonné',
 r'$I$ ens \inserted{pré}ordonné',
 'No independent stop follows ens. The raised pré has its own p-descender and é accent and attaches before ordonné.',
 kind='insertion or placement')
A('P06a','End of closed-set criterion',
 r'$x\in A,y\leq x\Rightarrow y\in A$',r'$x\in A$, $y\le x\Rightarrow y\in A$ ;',
 r'$x\in A,y\leq x\Rightarrow y\in A$',
 'After the final A the line is blank before the next baseline; no semicolon is present.',
 kind='text not on the page')
A('P06b','End of opposé parenthesis',
 r'(opposé à $I$)',r'(opposé à $I$) ;',r'(opposé à $I$)',
 'The closing parenthesis is followed by blank space, with neither a dot nor a descending comma stroke.',
 kind='text not on the page')
A('P06c','Explanation of tilde',
 r"($\sim$ désigne l'adh. pour $I^\circ$)",
 r"(\uncertain{ou} désigne l'adh. pour $I^{\circ}$)",
 r"($\sim$ désigne l'adh. pour $I^\circ$)",
 'The first mark is a single wave, matching the tilde over the preceding singleton, with no separate o loop or u strokes.',
 kind='misread symbol or index',consequential=True)
A('P07','First cancelled left marginal phrase',
 r'\margin{\deleted{\unsure{lien foncteurs|\illegible{1} fondamentales}}}',
 r'\struck{\ill{} fondamentales}',
 r'\margin{\deleted{\unsure{lien foncteurs|\illegible{1} fondamentales}}}',
 'A heavy cancellation crosses the low joins. A looped f-like descender and later ascender survive, but neither proposed full phrase can be read letter by letter. C candidates are retained explicitly as doubtful; H fondamentales is not established.',
 'low','misread word',False,True)
A('P08','NB1 heading and opening',
 r'\uline{NB1} : Si',r'\emph{NB 1} : si',r'NB1 : Si',
 'NB1 is heavily retraced but has no separate underline. The apparent line beneath belongs to the next-baseline word une. Initial S is large and upper-case-like.',
 'high','other',True,True)
A('P09a','Second equivalence between closures',
 r'\overline{\{x\}}\subset\overline{\{y\}}',
 r'\overline{\lbrace x\rbrace}\subset\overline{\lbrace y\rbrace}',
 r'\overline{\{x\}}\leq\overline{\{y\}}',
 'In the NB1 equivalence, the relation has an angled upper stroke and a distinct short lower bar, matching ≤ on the same page. It is not the open curved subset sign of the earlier definition. Both witnesses have regularized this written sign.',
 'high','misread symbol or index',True,True,True)
A('P09b','Inserted generalization after NB1',
 r'\inserted{Plus gén. $I\longrightarrow X$ continue ssi elle est croissante}',
 r'(Plus gén. $I\to X$ continue ssi elle est croissante)',
 r'\inserted{Plus gén. $I\longrightarrow X$ continue ssi elle est croissante}',
 'The long curved line joins the NB1 brace to the added baseline. It is an attachment leader; there are no independent opening and closing parentheses.',
 kind='insertion or placement',consequential=True)
A('P10','Second cancelled left marginal word',
 r'\margin{\deleted{\unsure{lien|Vue}}}',
 r'« Vue » (?) également biffé',
 r'\margin{\deleted{\unsure{Vue|lien}}}',
 'Tall V-like legs and a final e loop favor Vue, but the strike masks the low joins and does not permit every letter to be isolated. Candidate order is changed while the cancellation remains explicitly unresolved.',
 'low','misread word',True,False)
A('P11a','Article before préordre in NB. 2',
 'un préordre','une préordre','un préordre',
 'The article consists of u and n, ending at the return of n; no separate e follows.')
A('P11b','Abbreviation inside NB. 2 parenthesis',
 r'\unsure{néc.}',r'\uncertain{nécessairement}','néc.',
 'The short group has n, an accented é, c and an independent stop. No continuation for -essairement is written. Resolves C M0242.',
 'high','abbreviation expanded or spelling modernised',True,True)
A('P11c','Words after cancelled small word in NB. 2',
 r'\unsure{ce sera celui de|à savoir celle de}','à savoir celle de','ce sera celui de',
 'Separate ce, then s-e-r-a, then celui with final i and de are visible. There is no à before savoir or terminal -le in the second group. Resolves C M0243.',
 'high','misread word',True,True)
A('P12a','Equivalent open-set formulation',
 "intersections d'ouverts\nsont ouverts",r"\struck{\ill{}} intersection d'ouverts \uncertain{est} ouvert",
 "intersections d'ouverts\nsont ouverts",
 'The noun has a terminal s; the following baseline reads sont with an n before t and ouverts with its final s. Initial retracing of intersections does not isolate an additional cancelled word.',
 'medium','misread word',False,True,True)
A('P12b','Name of opposite topology',
 r'<<Q>>topologie opposée<<R>>',r'« topologie grossière »',r'<<Q>>topologie opposée<<R>>',
 'After the initial o are two p-descenders, then o-s-é-e. The paired quotation strokes are straight, not guillemets.',
 'high','misread word',False,True,True)
A('P13','Heading before two functors',
 r'\unsure{Ceci|Cas de} :',r'Cas \uncertain{de}',r'\unsure{Ceci|Cas}.',
 'There is one short word only, no independent de; the final mark is one dark point rather than two. Internal minims still admit Ceci or Cas. M0244 remains undecided.',
 'medium','misread word',True,True)
A('P15a','First functor identity',
 r'\operatorname{Ord}\circ\operatorname{Esp}=\operatorname{id}_{\unsure{\mathcal E}}',
 r'\mathrm{Ord}\circ\mathrm{Esp}=\mathrm{id}_{\mathcal{E}}$,',
 r'\operatorname{Ord}\cdot\operatorname{Esp}=\operatorname{id}_{\mathcal E}',
 'The first composition mark is a filled dot. The identity subscript has the two curved parts of calligraphic E, and there is no independent comma after the identity. Resolves M0245 while preserving the written category subscript.',
 'high','misread symbol or index',True,True,True)
A('P15b','Second functor identity',
 r'\operatorname{Esp}\circ\operatorname{Ord}\longrightarrow\operatorname{id}_{\unsure{\mathcal O}}',
 r'\mathrm{Esp}\circ\mathrm{Ord}\to\mathrm{id}_{\mathcal{O}}',
 r'\operatorname{Esp}\circ\operatorname{Ord}\longrightarrow\operatorname{id}_{\mathcal O}',
 'Here the composition mark is an open circle. The identity subscript is a round O with a terminal tick, distinct from the preceding two-lobed E. Resolves M0246 without correcting the source types.',
 'high','misread symbol or index',True,False,True)
A('P16','End of explanation referring to NB2',
 'satisfait la cond. du NB2','satisfait la cond. du NB 2)',
 'satisfait la cond. du NB2',
 'No closing parenthesis follows the 2 before the next displayed Hom line. The source parenthesis is left unbalanced.',
 kind='text not on the page')
A('P17','Short rule before Considérons',
 '(nothing)','(nothing)',r'\par\noindent\rule{2cm}{0.4pt}',
 'A short horizontal stroke starts well left of I and lies below the preceding sentence baseline, ending under X. Its position separates paragraphs rather than securely underlining I→X.',
 'medium','omission',True,True)
A('P18','Punctuation after pseudo-partition',
 'pseudo-partition :','pseudo-partition',r'pseudo-partition \unsure{:|.}',
 'One dark point can be distinguished. A second independent point is not secure, so colon/period remains explicit rather than silently omitting the mark.',
 'low','other',False,True)
A('P19a','Argument in inserted inverse-image definition',
 r'\inserted{Posons $X_J^*=\varphi^{-1}(J)$, les}',
 r'\add{Posons $X_J^{*}=\varphi^{-1}(J)$, les}',
 r'\inserted{Posons $X_J^*=\varphi^{-1}(I)$, les}',
 'The argument has a straight stem and top and bottom bars, unlike the hooked J under the first X. The visible letter is I at medium confidence; the expected J is recorded only as a diagnostic.',
 'medium','misread symbol or index',True,True,True)
A('P19b','State of continue ssi below Posons insertion',
 r'\deleted{continue ssi}',r'\struck{continue ssi}','continue ssi',
 'The long bent stroke runs under Posons and turns down at its left, above the bodies of continue ssi. No separate strike crosses those word bodies; they remain live. The attachment/revision state remains a local doubt in the report.',
 'medium','deletion state (struck given live or live given struck)',True,True,True)
A('P20','Parenthesis on disjoint pieces',
 r'les $\unsure{X_i|X_i^*}$ mutuellement disjoints',r'les $X_i^{*}$ mutuellement disjoints',
 r'les $X_i$ mutuellement disjoints',
 'The upper-right region of this X is blank. The visible lower star belongs to the formula on the next baseline, not this parenthetical X_i. Resolves M0247.',
 'high','misread symbol or index',True,True,True)
A('P22a','Start of complement-indexed union',
 r'$X_{\complement\widetilde i}^*',r'\struck{$X$} $X_{\complement\tilde\imath}^{*}',
 r'$X_{\complement\widetilde i}^*',
 'Only one X with retraced diagonal strokes is present before the complement-indexed formula; no spatially separate cancelled X can be isolated.',
 kind='text not on the page')
A('P22b','Subscript of complement union',
 r'\bigcup_{\substack{j\in I\\j\not\geq i}}X_j^*',
 r'\bigcup_{j\in I,\ j\not\ge i}X_j^{*}',
 r'\bigcup_{\substack{j\in I\\j\not\geq i}}X_j^*',
 'The conditions occupy two rows. There is no dark independent comma after I before the lower j condition.',
 kind='misread symbol or index')
A('P23a','Underline under faut',
 'Il faut pour ceci',r'Il \uncertain{faut} \add{donc} pour ceci',
 r'Il \uline{faut} pour ceci',
 'A separate short underline lies beneath faut. The surrounding words read Il faut pour ceci with no additional donc above or between them.',
 'high','other',True,True)
A('P25','Finite-union noun/sign',
 r'est alors $\bigcup$ finie',r'est alors \uncertain{réunion} finie',
 r'est alors $\bigcup$ finie',
 'The mark is a single open-topped U-shaped union glyph. It has no sequence of letter strokes for réunion.',
 kind='misread symbol or index',consequential=True)
A('P26a','Quoted local-finiteness abbreviation',
 r'<<Q>>loct. finie<<R>>',r'« loc\textsuperscript{t} finie »',
 r'<<Q>>loct. finie<<R>>',
 'The t here is on the writing baseline, followed by a distinct stop. Both quote marks are paired straight strokes.',
 kind='abbreviation expanded or spelling modernised')
A('P26b','Explanation of local finiteness',
 'i.e. loc. à ens. de val. fini',r'i.e. loc. \uncertain{dans} $X$ \ill{} \uncertain{va} fini',
 'i.e. loc. à ens. de val. fini',
 'After loc. stands à, then the three short forms ens., de and val. with their separate stops; there is no X or full word dans.',
 kind='misread word',consequential=True)
A('P27','Damaged cancelled line along upper edge',
 r'\margin{\deleted{\illegible{3} $\unsure{x\leq y}\Longleftrightarrow\overline{\{x\}}\subset\overline{\{y\}}$ \unsure{en}}}',
 r'« $\Longleftrightarrow\overline{\lbrace x\rbrace}\subset\overline{\lbrace y\rbrace}$ »',
 r'\margin{\deleted{\illegible{3} $\unsure{x\leq y}\Longleftrightarrow\overline{\{x\}}\subset\overline{\{y\}}$ \unsure{en}}}',
 'The damaged/crossed beginning retains word clusters and part of a y-like hook, but does not settle x≤y. The equivalence, closures and subset sign survive more clearly. The final en-like pair also remains uncertain; H reports only the clearer central formula.',
 'low','omission',False,True)
A('P28a','Opening of upper-right marginal note',
 r'\unsure{comme on veut que la top.}',r'\uncertain{moyennant} \ill{} que la top.',
 r'\unsure{comme on veut que la top.}',
 'The small groups favor comme / on / veut / que / la / top., with a tall t and p descender near the end. Some compressed minims are inseparable, so M0248 is not resolved.',
 'low')
A('P28b','Second line of upper-right note',
 r'\unsure{quotient en $I$ implique} topo',r'de $I$ \ill{} \ill{}',
 r'\unsure{quotient en $I$ implique} topo',
 'A q-descender and following low groups favor quotient en before barred capital I; implique remains compressed. The written topo following it is retained. M0249 remains unresolved.',
 'low',consequential=True)
A('P28c','Question diagnosis in upper-right note',
 'question est mal posée -- plutôt :',r'question est une pure \ill{} :',
 'question est mal posée -- plutôt :',
 'The m/a/l group, descending p of posée, and tall t of plutôt can be separated. The words do not match une pure.',
 'medium')
A('P28d','Request in upper-right marginal note',
 r'quelles conditions supplémentaires sur $\varphi$ i.e. les $X_i^*$ imposer pour avoir unicité ?',
 r'quelles conditions \ill{} que \ill{} les $X_i^{*}$ \ill{}',
 r'quelles conditions supplémentaires sur $\varphi$ i.e. les $X_i^*$ imposer pour avoir unicité ?',
 'The long supplémentaires group has distinct p-descenders and following sur; φ, i.e., les and the starred X_i are visible. Lower overlap with P29 supports imposer pour avoir unicité and the terminal question mark. Tiny joins remain a medium-confidence reading.',
 'medium',r'readable ink left as \ill{}',False,True,True)
A('P29a','Opening question in right column',
 'Dans quels cas','Dans quel cas','Dans quel cas',
 'The final tall l of quel ends in a return stroke, with no independent s before the separate c of cas.',
 'high','misread word',True,False)
A('P29b','Prefix and underline of ordre',
 r"l'\inserted{pré}\uline{ordre}",r"l'\supplied{pré}ordre",
 r"l'\inserted{pré}\uline{ordre}",
 'pré is physically raised above ordre; a separate thick horizontal underline lies beneath the base word.',
 kind='insertion or placement')
A('P31a','Placement of marginal-call star and small par',
 r"(dans le cas $\varphi$ continue) ? * \inserted{\unsure{(par)}}",
 r"i.e. * \add{\uncertain{par}} la famille",
 r"(dans le cas $\varphi$ continue) ? * \inserted{\unsure{(par)}}",
 'The star and small par-like insertion stand after the continuing-question line. Its curved enclosure touches the leader from above, so parentheses and letters are not resolved separately. H moves it before la famille.',
 'medium','insertion or placement',False,True)
A('P31b','Scope of raised plus précisément',
 r'\inserted{plus précisément par $(X_i^*)_{i\in I}$ donné} \deleted{\illegible{3}}',
 r'\struck{\ill{}} \add{Plus précisément} par $(X_i^{*})_{i\in I}$',
 r'\deleted{\illegible{3}} \inserted{plus précisément} par $(X_i^*)_{i\in I}$ donné',
 'Only plus précisément is raised over a cancelled lower-baseline cluster. par, the starred indexed family and donné share the lower baseline. H omits the last word; C wraps too much of the clause as an insertion.',
 'high','insertion or placement',True,True,True)
A('P32','Cancelled word after quand',
 r'\deleted{\unsure{tout}}',r'quand \struck{\ill{}} existe-t-il',
 r'\deleted{\unsure{tout}}',
 'The opening has d/apostrophe-like marks, but cancellation obscures the rest. The inherited tout candidate is retained only as a doubt; no clean reading is established.',
 'low','misread word',False,True)
A('P33','First two empty-set signs',
 r'$X=\varnothing$ il faut que $\operatorname{card}I\leq1$, et si $X\ne\varnothing$',
 r'$X=\emptyset$ il faut que card $I\le 1$, et si $X\neq\emptyset$',
 r'$X=\phi$ il faut que $\operatorname{card}I\leq1$, et si $X\ne\phi$',
 'Both signs are loops crossed by long slanting shafts, the author’s phi-shaped notation. The cardinal bound ends in the digit 1. No standard empty-set glyph is substituted.',
 'high','misread symbol or index',True,True,True)
A('P34a','Two nonemptiness conditions on pieces',
 r'les $X_i^*\ne\varnothing$. Supposons donc $\varphi$ surj. i.e. $X_i^*\ne\varnothing$',
 r'les $X_i^{*}\neq\emptyset$. \struck{Supposons} \uncertain{Supposons} donc $\varphi$ surj. i.e. $X_i^{*}\neq\emptyset$',
 r'les $X_i^*\ne\phi$. Supposons donc $\varphi$ surj. i.e. $X_i^*\ne\phi$',
 'Both nonempty signs have the same crossed-loop phi form. Only one retraced Supposons occupies the baseline; no independent cancelled duplicate is visible.',
 'high','misread symbol or index',True,True,True)
A('P34b','Emphasis on top. quotient',
 r'la \uline{top.} \uline{quotient}',r'la top. \emph{quotient}',
 r'la \uline{top.} \uline{quotient}',
 'There is a short separate underline beneath the line-ending top., followed on the next baseline by the longer underline beneath quotient.',
 kind='omission')
A('P35','Terminal punctuation after dans I',
 r'fermé dans $I$.',r'fermé dans $I$ ;',r'fermé dans $I$',
 'Supplement P53 shows the entire right edge. No separate mark follows I before the dark border; the low dark blob is continuous with I’s bottom bar. Pale lower specks do not match writing ink.',
 'medium','text not on the page',True,True,crop='P53')
A('P36','Singular agreement and position of cas insertion',
 r'de fermés est fermé \inserted{(cas $\varphi$ loc. finie)}',
 r'de fermés \add{(cas $\varphi$ loc. finie)} sont fermés',
 r'de fermés est fermé \inserted{(cas $\varphi$ loc. finie)}',
 'The live baseline reads est and singular fermé. The small (cas φ loc. finie) is raised and its leader attaches after fermé, not before the verb. Source grammar is preserved.',
 'high','misread word',False,True,True)
A('P37a','Future verb',
 'on aura donc','on aurait donc','on aura donc',
 'The a-ending returns directly toward the next word; there are no i-dot or t-ascender/crossbar after aura.')
A('P37b','Cancelled symbols before universal J',
 r'\deleted{$\unsure{x\in}$}',r'ssi \struck{\ill{}} $\forall J\subset I$',
 r'\deleted{$\unsure{x\in}$}',
 'An x-like pair and rounded membership-like shape survive beneath the strike. The crossing prevents a certain reading of both symbols; retain the explicit formula doubt.',
 'low','misread symbol or index',False,True,True)
A('P38','Question about an order',
 'cette préordre est-il\nun ordre',"ceci provient-il d'un ordre",
 'cette préordre est-il\nun ordre',
 'The first group has the paired t-strokes of cette; the next begins with p and reads préordre, followed by separate est-il. No d apostrophe precedes un.',
 'high','misread word',False,True,True)
A('P39a','Chance of chaotic preorder',
 r'(NB <<Q>>en général<<R>> ce préordre aura tte \unsure{chance}',
 r'(\emph{NB} « en général » ce préordre \uncertain{sera} loin',
 r'(NB <<Q>>en général<<R>> ce préordre aura tte chance',
 'aura and the short tte are written. In chance the ch ascender, a/n minims and c/e return can be distinguished; resolves M0251 at medium confidence. Quotation marks are straight. NB has no separate underline here.',
 'medium','misread word',True,True,True)
A('P39b','Nature of preorder',
 'chaotique',r'\uncertain{discrétique}','chaotique',
 'Initial ch, then a/o, the high crossed t, dotted i and long q-descender are visible; the word does not begin discr-.',
 'high','misread word',False,True,True)
A('P39c','Short sufficient-condition wording',
 'Il faut et s. que','Il faut et il suffit que','Il faut et s. que',
 'Only a short s and stop follow et. No il or suffix -uffit is written.',
 kind='abbreviation expanded or spelling modernised')
A('P40','Singleton condition',
 r'les $\{i\}$ soient localement fermés',r'les $\bar\imath$ soient localement fermés',
 r'les $\{i\}$ soient localement fermés',
 'Distinct left and right curly braces enclose a dotted i; there is no horizontal bar over it.',
 kind='misread symbol or index',consequential=True)
A('P41a','Verb after ce qui',
 'qui implique','qui indique','qui implique',
 'The m/p group includes a long p-descender and the later q-descender; there is no d ascender in the middle.')
A('P41b','Local-closedness baseline',
 r'les $X_i^*$ sont loct. fermés',r'les $X_i^{*}$ soient \add{loc\textsuperscript{t}} fermés',
 r'les $X_i^*$ sont loct. fermés',
 'The verb has sont, without a separate i/e. loct. lies on the ordinary baseline, followed by a stop; it is not a raised inserted word.',
 kind='insertion or placement',consequential=True)
A('P41c','Cancelled transition word',
 r"\deleted{\unsure{D'ailleurs}}",r'\struck{\ill{}}',
 r"\deleted{\unsure{D'ailleurs}}",
 'The first tall loop and apostrophe-like mark and some ascenders favor the inherited candidate, but the heavy cancellation masks low letters. No full resolution.',
 'low')
A('P42a','Raised Plus and following précis',
 r'\inserted{\unsure{Plus}} \unsure{précis,}',r'\add{\uncertain{bien}}',
 r'\inserted{\unsure{Plus}} \unsure{précis,}',
 'The raised form favors P-l-u-s; the lower group favors précis. Adjoining cancelled strokes and the final punctuation prevent a clean letter-by-letter resolution. M0252 and M0253 remain doubtful, rather than adopting bien.',
 'low','misread word',False,True)
A('P42b','Cancelled réciproquement',
 r'\deleted{\unsure{réciproquement}}',r'\struck{\ill{}}',
 r'\deleted{\unsure{réciproquement}}',
 'A long cancelled group occupies the next lower baseline; some r/p-like strokes survive, but the strike obscures too much to resolve the inherited candidate.',
 'low')
A('P42c','Second short condition wording',
 'il f. et s. que','il faut et il suffit que','il f. et s. que',
 'Only f with a stop and s with a stop are written between il, et and que; neither full expanded word appears.',
 kind='abbreviation expanded or spelling modernised')
A('P42d','Inserted universal quantifier',
 r'\inserted{$\forall i\in I$}',r'\add{\uncertain{\ill{}}}',
 r'\inserted{$\forall i\in I$}',
 'The raised group has the crossed V-like universal sign, dotted i, open membership sign and barred capital I; the leader joins it before l’on ait.',
 'high',r'readable ink left as \ill{}',False,True,True)
A('P42e','Cancelled quantifier after ait',
 r"\deleted{$\unsure{\forall i\in I|\{i\}}$}",r"l'on ait \struck{\ill{}}",
 r"\deleted{$\unsure{\forall i\in I|\{i\}}$}",
 'Parallel cancellation strokes mask the center of the formula. A high left stroke and right I-like return survive, but do not separate all signs; retain both candidates.',
 'low','misread symbol or index',False,True,True)
A('P43a','Original order of singleton and inverse-image equalities',
 r'$\{i\}=\overline i\cap\widetilde i$ ce qui équivaut à \deleted{$\unsure{\forall i\in I}$} $X_{\overline i}^*\cap X_{\widetilde i}^*=X_i^*$',
 r'$X_{\bar\imath}^{*}\cap X_{\tilde\imath}^{*}=X_i^{*}$ (puisque $\lbrace i\rbrace=\bar\imath\cap\tilde\imath$) ce qui équivaut à \struck{\ill{}} \ldots',
 r'$\{i\}=\overline i\cap\widetilde i$ ce qui équivaut à \deleted{$\unsure{\forall i\in I}$} $X_{\overline i}^*\cap X_{\widetilde i}^*=X_i^*$',
 'Reading left to right gives the singleton equality, ce qui équivaut à, the crossed quantifier, then the starred-X intersection equality. No puisque or parenthetical opening is present. The cancelled quantifier remains uncertain, but both live equalities and all stars/accents are visible.',
 'high','insertion or placement',False,True,True)
A('P43b','Tiny introduction to smallest closed set',
 r'où $X_{\overline i}^*$',r'or $X_{\bar\imath}^{*}$',
 r'\unsure{or|où} $X_{\overline i}^*$',
 'A closed o and short right shoulder are visible, but a separate u and grave accent are not secure. Prefer or provisionally while retaining où; grammar does not settle this source reading.',
 'low','misread word',True,False)
A('P43c','Insertion after smallest closed X',
 r'fermé de $X$ \inserted{$\supset X_i^*$}',
 r'\add{$\supset X_i^{*}$ \ill{}}',
 r'fermé de $X$ \inserted{$\supset X_i^*$}',
 'The raised superset sign and starred X_i have a curved leader ending immediately after the baseline X. No independent further word can be isolated inside the leader.',
 kind='insertion or placement',consequential=True)
A('P43d','Quoted saturated phrase',
 r'<<Q>>saturé<<R>> par la',r'« saturé » pour la',r'<<Q>>saturé<<R>> par la',
 'After the paired straight quotes, the short word has p-descender, a loop and r-return, with no ou group.')
A('P44','Abbreviation after loc. finie',
 'loc. finie assoc.', 'loc. finie associée','loc. finie assoc.',
 'The word stops after the short assoc group, followed by a distinct point and then comma; no -iée continuation is present.',
 kind='abbreviation expanded or spelling modernised')
A('P45','Quoted stratification phrase and underline',
 r'une <<Q>>\uline{stratification fidèle}<<R>>',
 r'« stratification fidèle »',r'une <<Q>>stratification fidèle<<R>>',
 'une precedes two straight opening quote strokes. Neither stratification nor fidèle has an independent underline: the lower strokes are their f-descenders continuing toward the next baseline.',
 'high','other',True,True)
A('P46a','Second local-finiteness abbreviation',
 r'loc\unsure{t.} finie',r'loc\textsuperscript{t} finie',
 r'loc\textsuperscript{t}. finie',
 'A small raised t follows loc and a separate dark stop stands at the baseline below/right of it. Resolves M0254, retaining the actual raised position and stop.',
 'high','abbreviation expanded or spelling modernised',True,True)
A('P46b','Singular telle in definition',
 'finie telle que', 'finie telles que','finie telle que',
 'After the two l-ascenders and e-return there is no independent s before que.')
A('P46c','Family correspondence',
 'ils correspondent à une famille',r'ils correspondent aux familles \add{indexées par $I$ ordonné}',
 'ils correspondent à une famille',
 'The accent over à, separate une, and singular famille are written. The later insertion belongs to the following family/partition line, not this phrase.',
 kind='misread word',consequential=True)
A('P47','Family and partition wording',
 r'$(X_i^*)_{i\in I}$, partitions ensembliste de $X$',
 r'$(X_i^{*})_{i\in I}$ \add{\uncertain{partition}}, \uncertain{constituée} de $X_i$',
 r'$(X_i^*)_{i\in I}$, partitions ensembliste de $X$',
 'After the indexed family, the words lie on the main baseline. partitions has a final short s-like hook; ensembliste has the b/l ascenders and final -iste, not constituée. The final X has no subscript.',
 'medium','misread word',False,True,True)
A('P48a','Raised indexing clause',
 r'\inserted{indicée par $I$ ordonné}',r'\add{indexées par $I$ ordonné}',
 r'\inserted{indicée par $I$ ordonné}',
 'The raised word has i-n-d-i-c-é-e, with a c-curve rather than crossed x and no terminal s. It attaches after the family/partition phrase; the heavy cancellation below remains distinct.',
 kind='insertion or placement',consequential=True)
A('P48b','Low live words below cancellation',
 r'\unsure{tels que}', '(nothing)',r'\unsure{tels que}',
 'A small live group beneath the main cancellation favors tels que. Crowding and nearby strike returns leave the internal letters unresolved; retain the words as explicit doubt rather than omitting them.',
 'low','omission',False,True)
A('P49','Disjointness and singular telle',
 r'\unsure{disjoints} et telle que','disjoints et telles que','disjoints et telle que',
 'The d loop/ascender, dotted i and j-descender support disjoints; -oints is compressed but legible at medium confidence, resolving M0256. After et, telle has no separate final s.',
 'medium','misread word',True,True)
A('P50','Second singular telle',
 'donc telle que','donc telles que','donc telle que',
 'The word ends in the return of e; no extra s intervenes before que.')
A('P51','Last inserted reformulation',
 r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ est \unsure{fermé} ($\Rightarrow$ les $X_i^*$ loc. f.)}',
 r'\add{(i.e. $J$ fermé $\Rightarrow X_J$ fermé $\Rightarrow$ les $X_i^{*}$ loc. f.)}',
 r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ est fermé ($\Rightarrow$ les $X_i^*$ loc. f.)}',
 'The phrase includes short est before the f-loop, compressed r/m joins and final accented e of fermé; resolves M0257 at medium confidence. No opening parenthesis precedes i.e.; an independent parenthesis begins only before the second implication and closes after f.',
 'medium','misread word',True,True,True)
A('P54','Underline beneath spécialisation',
 r'\uline{spécialisation}', 'spécialisation',r'\uline{spécialisation}',
 'Two separated but aligned horizontal underline segments lie beneath the word, distinct from its p-descender and from the definition on the lower line.',
 kind='omission')
A('P56','NB. 2 heading punctuation',
 r'\uline{NB. 2}',r'\emph{NB 2}',r'\uline{NB. 2}',
 'A separate dark point stands between B and the digit 2 above their common underline. P55 was only a clipped context fragment; P56 completes the heading.',
 kind='omission')

# The checks below compare source substrings, not manuscript recognition.
source_mismatches=[]
for a in changes:
    if a['id'] in ['P01','P12b']:
        a['marked_in_h'] = True
    for key,src in [('c',C),('h',H)]:
        if a[key] != '(nothing)' and flat(a[key]) not in flat(src):
            source_mismatches.append((a['id'],key,a[key]))

REPORT = dict(page='150_scan003',reader='reader_b',
    line_count=sum(bool(x.strip()) for x in D.splitlines()),
    changes=changes,decisions=[],inventory=[],audit_boxes=[],doubts=[],notes=[],
    check_events=[],notation=[],abbreviations=[],hand=[],diff_coverage=[],
    deletion_insertion_review=[])

def DEC(id,p,decision,reading,evidence,confidence):
    REPORT['decisions'].append(dict(id=id,cote='150',scan='3',decision=decision,
        reading=norm(reading),evidence=evidence,crop=f'crops/150_scan003_{p}.png',
        box=BOXES[p],confidence=confidence))
DEC('M0241','P01','undecided',r'\unsure{\operatorname{Ord}(X)|\operatorname{Spéc}(X)}',
    'Overtraced opening and tall final d do not separate the older Spéc-like layer from the Ord-like form.','low')
DEC('M0242','P11','first','néc.','Short n-é-c group, accent and independent stop; no expanded continuation.','high')
DEC('M0243','P11','first','ce sera celui de','Separate ce / sera / celui / de groups and final i in celui.','high')
DEC('M0244','P13','undecided',r'\unsure{Ceci|Cas}',
    'One short word only; no independent de. Its internal strokes still admit Ceci or Cas. One following point is retained.','medium')
DEC('M0245','P15','first',r'\mathcal E','Two curved parts distinguish the first identity subscript E. Whole first formula checked.','high')
DEC('M0246','P15','first',r'\mathcal O','Second identity subscript is a round O with terminal tick; whole second formula checked.','high')
DEC('M0247','P20','first',r'X_i','No upper star belongs to the parenthetical X_i; the nearby star lies on the next formula baseline.','high')
DEC('M0248','P28','undecided',r'\unsure{comme on veut que la top.}',
    'Several tiny compressed minims remain inseparable although the C word groups are favored.','low')
DEC('M0249','P28','undecided',r'\unsure{quotient en $I$ implique}',
    'q-descender and capital I are visible; the following compressed joins do not settle every letter of implique.','low')
DEC('M0250','P31','undecided',r'\unsure{(par)}',
    'The p-like descender and low ar-like return survive, but curved enclosure/leader and punctuation are not cleanly separable.','low')
DEC('M0251','P39','first','chance',
    'ch ascender, a/n minims and c/e return support chance, not loin; the cramped joins warrant medium confidence.','medium')
DEC('M0252','P41','undecided',r'\unsure{Plus}',
    'Raised P/l-like strokes and us-like return favor Plus; nearby cancelled writing and crop overlap prevent full separation.','low')
DEC('M0253','P42','undecided',r'\unsure{précis,}',
    'The p/r group and accented vowel favor précis; adjacent cancellation and the last small mark leave the exact ending/punctuation uncertain.','low')
DEC('M0254','P46','first',r'\textsuperscript{t}.',
    'Raised small t and separate baseline stop both visible; draft preserves them as loc\\textsuperscript{t}.','high')
DEC('M0255','P48','undecided',r'\unsure{tels que}',
    'The group remains live below the principal cancellation, but low letters are crowded by returning strike strokes.','low')
DEC('M0256','P49','first','disjoints',
    'Initial d loop/ascender, dotted i, j-descender and compressed -oints support the reading.','medium')
DEC('M0257','P51','first','fermé',
    'f-loop, compressed r/m joins and accented final e in the complete inserted implication; medium confidence.','medium')

def INV(kind,position,text):
    REPORT['inventory'].append(dict(scan='150_scan003',sheet_kind='text',hand='his hand',
        element=f"E{len(REPORT['inventory'])+1:02}",kind=kind,position=position,
        first_words_or_objects=norm(text),transcribed='yes'))
INV('text','upper-left folio','1')
INV('text','left section, top',r'X espace topologique ... spécialisation')
INV('insertion','above first ordonné',r'\inserted{pré}')
INV('display','left, first equivalence',r'x\leq y \overset{déf}{\Longleftrightarrow}\overline{\{x\}}\subset\overline{\{y\}}')
INV('text','left, separation axiom parenthesis',r'(ordonné ssi X satisfait ... (T_0))')
INV('insertion','above second ordonné',r'\inserted{pré}')
INV('text','left, closed/open sets and basis',r'I ens ... fermés les A ... base d’ouverts')
INV('display','below basis definition',r'\operatorname{Esp}(I)')
INV('deletion','left margin, first crossed phrase',r'\deleted{\unsure{lien foncteurs|\illegible{1} fondamentales}}')
INV('text','left, NB1 and closure equivalences','NB1 : Si I,J préordonnés')
INV('insertion','after NB1 with long curved leader',r'Plus gén. I\longrightarrow X continue ssi elle est croissante')
INV('deletion','left margin, second crossed word',r'\deleted{\unsure{Vue|lien}}')
INV('text','left, NB. 2 paragraph',r'\uline{NB. 2} Une topologie')
INV('deletion','NB. 2 after unique',r'\deleted{\illegible{1}}')
INV('text','left, heading to diagram',r'\unsure{Ceci|Cas}. deux foncteurs')
INV('diagram','left center',r'\mathcal E=(Esp), (Préord)=\mathcal O; Ord right, Esp left; rotated memberships to X and I')
INV('display','beside diagram',r'Ord\cdot Esp=id_{\mathcal E}; Esp\circ Ord\longrightarrow id_{\mathcal O}')
INV('text','left center-right of diagram','car l’application ... satisfait la cond. du NB2')
INV('display','left, adjunction line',r'Hom_{\mathcal E}(Esp(I),X)\xrightarrow{\sim}Hom_{\mathcal O}(I,Ord(X))')
INV('text','left, just below adjunction','I→X est continue ssi elle est croissante')
INV('drawing','left, short paragraph separator',r'\par\noindent\rule{2cm}{0.4pt}')
INV('text','left lower section','Considérons maintenant ... pseudo-partition')
INV('deletion','before pseudo-partition',r'\deleted{une}')
INV('insertion','above continue ssi',r'Posons X_J^*=\varphi^{-1}(I), les')
INV('text','left lower section after insertion','continue ssi ... ouverts ... sont fermés')
INV('display','left lower section, closure definition',r'X_i\overset{déf}=X_{\bar i}^*=\bigcup_{j\leq i}X_j')
INV('insertion','finite-case explanation',r'de I')
INV('text','left bottom','plus généralement ... loct. finie ... NB Si I’⊂I')
INV('margin note','damaged top edge across rightward center',r'\deleted{\illegible{3} ... \unsure{x\leq y} ... \unsure{en}}')
INV('margin note','upper right, six small lines','* comme on veut ... quelles conditions ... avoir unicité ?')
INV('text','right column, opening question','Dans quel cas ... ordre ... déterminé')
INV('insertion','above right-column ordre','pré')
INV('insertion','after question and asterisk',r'\unsure{(par)}')
INV('deletion','below plus précisément',r'\deleted{\illegible{3}}')
INV('insertion','raised above cancelled cluster','plus précisément')
INV('text','lower baseline after raised plus précisément',r'par (X_i^*)_{i\in I} donné')
INV('deletion','right column after quand',r'\deleted{\unsure{tout}}')
INV('text','right, existence/uniqueness and quotient paragraphs','existe-t-il ... Pour l’unicité ... Supposons ... top. quotient')
INV('insertion','after est fermé',r'(cas \varphi loc. finie)')
INV('deletion','right, before ∀J criterion',r'\deleted{$\unsure{x\in}$}')
INV('text','right, order criterion and local closedness','À quelles conditions cette préordre ...')
INV('deletion','right, before Plus',r'\deleted{\unsure{D’ailleurs}}')
INV('insertion','right, above cancelled transition',r'\unsure{Plus}')
INV('text','right, preceding shortened condition',r'\unsure{précis,}')
INV('deletion','right, under précis',r'\deleted{\unsure{réciproquement}}')
INV('insertion','right, before l’on ait',r'\forall i\in I')
INV('deletion','right, after l’on ait',r'\deleted{\unsure{\forall i\in I|\{i\}}}')
INV('display','right, singleton and intersection identities',r'\{i\}=\bar i\cap\tilde i ... X_{\bar i}^*\cap X_{\tilde i}^*=X_i^*')
INV('deletion','right, after ce qui équivaut à',r'\deleted{\unsure{\forall i\in I}}')
INV('insertion','right, after smallest closed X',r'\supset X_i^*')
INV('text','right, saturated subsets and faithful stratification','or|où X ... saturé ... une stratification fidèle')
INV('text','right, family definition',r'loc^t. finie ... ordonné ... famille (X_i^*)')
INV('insertion','right lower margin, above cancellation','indicée par I ordonné')
INV('deletion','right lower margin, heavy crossing',r'\deleted{\illegible{4}}')
INV('text','right lower margin under cancellation',r'\unsure{tels que}')
INV('text','right bottom, conditions a and b','disjoints et telle que ... Pour J ... a) ... b)')
INV('insertion','right bottom after condition a',r'i.e. J fermé ⇒ X_J est fermé (⇒ les X_i^* loc. f.)')

def AUD(kind,xyxy,reading):
    REPORT['audit_boxes'].append(dict(box=f"B{len(REPORT['audit_boxes'])+1:02}",
        kind=kind,xyxy=xyxy,reading=norm(reading)))

# Target scopes follow handwritten baselines; surrounding edge fragments are not
# promoted to independent text. Each required insertion/cancellation is included.
AUD('handwritten number',[58,8,115,82],'1')
AUD('doubtful formula; C/H different words',BOXES['P01'],r'\unsure{\operatorname{Ord}(X)|\operatorname{Spéc}(X)}')
AUD('insertion',[520,104,656,193],r'\inserted{pré}')
AUD('C/H different words',[727,157,944,219],r'\uline{spécialisation}')
AUD('handwritten number; C/H different words',BOXES['P03'],r'l’axiome de séparation $(T_0)$)')
AUD('insertion; C/H different words',BOXES['P05'],r'$I$ ens \inserted{pré}ordonné')
AUD('C/H different words',BOXES['P06'],r'fermés les $A\subset I$ t.q. $x\in A,y\leq x\Rightarrow y\in A$ ouverts les ens. fermés dans $I^\circ$ (opposé à $I$) base d’ouverts : les ens $I_{\geq x}=\widetilde{\{x\}}$ ($\sim$ désigne l’adh. pour $I^\circ$)')
AUD('margin note; struck passage; C/H different words',BOXES['P07'],r'\deleted{\unsure{lien foncteurs|\illegible{1} fondamentales}}')
AUD('handwritten number; C/H different words',BOXES['P08'],r'NB1 : Si $I,J$ préordonnés, $f:I\longrightarrow J$ une application, alors $f$ croissante ssi $f$ continue.')
AUD('doubtful formula; C/H different words',BOXES['P09'],r'$\overline{\{x\}}=I_{\leq x}=\{y\in I\mid y\leq x\}$ donc $x\leq y\Longleftrightarrow\overline{\{x\}}\leq\overline{\{y\}}\Longleftrightarrow x\in\overline{\{y\}}$ \inserted{Plus gén. $I\longrightarrow X$ continue ssi elle est croissante}')
AUD('margin note; struck passage; less than high confidence departure',BOXES['P10'],r'\deleted{\unsure{Vue|lien}}')
AUD('handwritten number; C/H different words',[516,692,608,746],r'\uline{NB. 2}')
AUD('C/H different words; struck passage',BOXES['P11'],r'un préordre (néc. unique, \deleted{\illegible{1}} ce sera celui de')
AUD('C/H different words',BOXES['P12'],r'la spécialisation) ssi les réunions quelc. de fermés sont fermés $\Longleftrightarrow$ intersections d’ouverts sont ouverts (i.e. $\exists$ une <<Q>>topologie opposée<<R>> !)')
AUD('C/H different words; less than high confidence departure',BOXES['P13'],r'\unsure{Ceci|Cas}. deux foncteurs')
AUD('doubtful formula',BOXES['P15'],r'$\operatorname{Ord}\cdot\operatorname{Esp}=\operatorname{id}_{\mathcal E}$ $\operatorname{Esp}\circ\operatorname{Ord}\longrightarrow\operatorname{id}_{\mathcal O}$')
AUD('handwritten number; C/H different words',BOXES['P16'],r'car l’application $\operatorname{id}_X:X\longrightarrow X$ est continue de $\operatorname{Esp}\operatorname{Ord}X$ dans $X$ (et est $\simeq$ ssi $X$ satisfait la cond. du NB2')
AUD('less than high confidence departure',[72,1313,328,1370],r'\par\noindent\rule{2cm}{0.4pt}')
AUD('struck passage; C/H different words; less than high confidence departure',BOXES['P18'],r'i.e. \deleted{une} pseudo-partition \unsure{:|.} $X=\bigcup_{i\in I}X_i^*$')
AUD('insertion; handwritten number; doubtful formula; less than high confidence departure',BOXES['P19'],r'\inserted{Posons $X_J^*=\varphi^{-1}(I)$, les} continue ssi')
AUD('doubtful formula; C/H different words',BOXES['P20'],r'(les $X_i$ mutuellement disjoints).')
AUD('handwritten number',BOXES['P21'],r'$\varphi^{-1}(I_{\geq i})$ ouverts')
AUD('C/H different words',BOXES['P22'],r'i.e. ssi les $X_{\widetilde i}^*=\bigcup_{j\geq i}X_j^*$ sont ouverts, i.e. ssi les $X_{\complement\widetilde i}^*=\bigcup_{\substack{j\in I\\j\not\geq i}}X_j^*$ sont fermés. Il \uline{faut} pour ceci que les')
AUD('C/H different words',BOXES['P24'],r'$X_i\overset{\mathrm{déf}}=X_{\overline i}^*=\bigcup_{j\leq i}X_j$')
AUD('insertion',BOXES['P52'],r'\inserted{de $I$}')
AUD('C/H different words',BOXES['P25'],r'si $I$ est fini (car tt fermé \inserted{de $I$} est alors $\bigcup$ finie de fermés de la forme $\overline i$)')
AUD('C/H different words',BOXES['P26'],r'plus généralement si $\varphi$ est <<Q>>loct. finie<<R>> i.e. loc. à ens. de val. fini')
AUD('margin note; struck passage; doubtful formula',BOXES['P27'],r'\deleted{\illegible{3} $\unsure{x\leq y}\Longleftrightarrow\overline{\{x\}}\subset\overline{\{y\}}$ \unsure{en}}')
AUD('margin note; C/H different words; doubtful formula',[2030,47,2540,240],r'* \unsure{comme on veut que la top.} \unsure{quotient en $I$ implique} topo, la question est mal posée -- plutôt : quelles conditions supplémentaires sur $\varphi$ i.e. les $X_i^*$ imposer pour avoir unicité ?')
AUD('insertion; C/H different words',BOXES['P29'],r'Dans quel cas l’\inserted{pré}\uline{ordre} de l’ens $I$ est-il déterminé')
AUD('insertion; struck passage; doubtful formula; C/H different words',BOXES['P31'],r'i.e. la famille $(X_i)_{i\in I}$ (dans le * \inserted{\unsure{(par)}} \deleted{\illegible{3}} \inserted{plus précisément} par $(X_i^*)_{i\in I}$ donné')
AUD('struck passage; C/H different words',BOXES['P32'],r'quand \deleted{\unsure{tout}} existe-t-il')
AUD('handwritten number; C/H different words',BOXES['P33'],r'Pour l’unicité, il est clair que si $X=\phi$ il faut que $\operatorname{card}I\leq1$, et si $X\ne\phi$ que $\varphi$ soit')
AUD('C/H different words',BOXES['P34'],r'surjective i.e. les $X_i^*\ne\phi$. Supposons donc $\varphi$ surj. i.e. $X_i^*\ne\phi$. On aimerait que la top. de $I$ soit la \uline{top.}')
AUD('C/H different words; less than high confidence departure',BOXES['P53'],r'$I$')
AUD('insertion; C/H different words',BOXES['P36'],r'Cette topologie sur $I$ est bien telle que les réunions de fermés est fermé \inserted{(cas $\varphi$ loc. finie)} donc est associée à un ordre')
AUD('struck passage; doubtful formula; C/H different words',BOXES['P37'],r'unique de $I$. Pour cet ordre, on aura donc $i\leq j$ ssi \deleted{$\unsure{x\in}$} $\forall J\subset I$ tel que $X_J^*$ fermé et $j\in J$, on')
AUD('C/H different words',BOXES['P38'],r'a $i\in J$. À quelles conditions cette préordre est-il')
AUD('C/H different words; less than high confidence departure',BOXES['P39'],r'un ordre (NB <<Q>>en général<<R>> ce préordre aura tte chance d’être chaotique !) Il faut et s. que')
AUD('C/H different words',BOXES['P40'],r'les $\{i\}$ soient localement fermés dans $I$, ce')
AUD('insertion; struck passage; C/H different words',[1520,1121,2536,1213],r'qui implique que les $X_i^*$ sont loct. fermés. \deleted{\unsure{D’ailleurs}} \inserted{\unsure{Plus}}')
AUD('struck passage; C/H different words',BOXES['P42'],r'\unsure{précis,} \deleted{\unsure{réciproquement}} il f. et s. que \inserted{$\forall i\in I$} l’on ait \deleted{$\unsure{\forall i\in I|\{i\}}$}')
AUD('struck passage; doubtful formula; insertion; C/H different words; less than high confidence departure',BOXES['P43'],r'$\{i\}=\overline i\cap\widetilde i$ ce qui équivaut à \deleted{$\unsure{\forall i\in I}$} $X_{\overline i}^*\cap X_{\widetilde i}^*=X_i^*$, \unsure{or|où} $X_{\overline i}^*$ est le plus petit fermé de $X$ \inserted{$\supset X_i^*$} <<Q>>saturé<<R>> par la')
AUD('C/H different words',BOXES['P44'],r'relation d’équivalence loc. finie assoc., et $X_{\widetilde i}^*$ est le')
AUD('C/H different words',BOXES['P45'],r'plus petit ouvert saturé $\supset X_i^*$. On pourrait appeler une <<Q>>stratification fidèle<<R>> de $X$ une relation d’équiv.')
AUD('C/H different words',BOXES['P46'],r'loc\textsuperscript{t}. finie telle que l’ens préordonné quotient $I$ soit \uline{ordonné} -- ils correspondent à une famille')
AUD('doubtful formula; C/H different words',BOXES['P47'],r'$(X_i^*)_{i\in I}$, partitions ensembliste de $X$')
AUD('insertion; struck passage; C/H different words',BOXES['P48'],r'\inserted{indicée par $I$ ordonné} \deleted{\illegible{4}} \unsure{tels que}')
AUD('C/H different words; less than high confidence departure',BOXES['P49'],r'disjoints et telle que')
AUD('C/H different words',BOXES['P50'],r'Pour $J\subset I$, on ait $X_J$ fermé ssi $J$ fermé. donc telle que a) les $X_i\overset{\mathrm{déf}}=\bigcup_{j\leq i}X_j^*$ fermés,')
AUD('insertion; doubtful formula; C/H different words; less than high confidence departure',BOXES['P51'],r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ est fermé ($\Rightarrow$ les $X_i^*$ loc. f.)}')

def DO(place,reading,alternatives,confidence,reason):
    REPORT['doubts'].append(dict(place=place,reading=norm(reading),
        alternatives=norm(alternatives),confidence=confidence,reason=reason))
DO('P01 operator',r'\unsure{\operatorname{Ord}(X)|\operatorname{Spéc}(X)}','Ord(X) / Spéc(X)','low','Overtraced layers cannot be independently assigned.')
DO('P07 cancelled phrase',r'\unsure{lien foncteurs|\illegible{1} fondamentales}','possible D’-like opening; no full alternative established','low','Strike masks low letters; no full cancelled reading resolved.')
DO('P10 cancelled word',r'\unsure{Vue|lien}','Vue / lien','low','V-like tall strokes favor Vue but low joins are cancelled.')
DO('P13 heading',r'\unsure{Ceci|Cas}','Ceci / Cas','medium','Only one word; internal strokes remain ambiguous; separate de rejected.')
DO('P18 punctuation',r'\unsure{:|.}',': / .','low','One point clear; second point not secure.')
DO('P19 inserted formula',r'X_J^*=\varphi^{-1}(I)',r'X_J^*=\varphi^{-1}(J)','medium','Top/bottom bars support I; expected J is not substituted.')
DO('P19 revision state','continue ssi live','cancelled continue ssi','medium','No independent cancellation through letter bodies; long bent stroke is treated as insertion leader.')
DO('P25/P52 insertion',r'\inserted{de $I$}','same reading, overlapping de strokes','medium','de partly overlaps a descender from preceding fermés; I is retraced.')
DO('P27 damaged cancelled line',r'\illegible{3} $\unsure{x\leq y}\Longleftrightarrow\overline{\{x\}}\subset\overline{\{y\}}$ \unsure{en}',
   'unreadable initial clusters; x≤y and en not fully recoverable','low','Torn/crossed ink at top edge.')
DO('P28 upper-right note, line 1',r'\unsure{comme on veut que la top.}','H moyennant ...','low','Tiny compressed minims remain uncertain.')
DO('P28 upper-right note, line 2',r'\unsure{quotient en $I$ implique}','H de I ...','low','Middle word joins compressed; context does not resolve them.')
DO('P28 lower request','conditions supplémentaires sur φ ... imposer pour avoir unicité ?','same reading','medium','Tiny letters and lower overlap; most distinctive ascenders/descenders support reading.')
DO('P31 small insertion',r'\unsure{(par)}','par with leader rather than parentheses','low','Curved enclosure connects to upper leader; not settled.')
DO('P32 cancelled word',r'\deleted{\unsure{tout}}',"possible d' opening; no complete alternative",'low','Crossing prevents letter-by-letter reading.')
DO('P35 terminal punctuation','none','C period / H semicolon','medium','No distinct point after I at edge; lower pale specks excluded.')
DO('P37 cancelled symbols',r'\deleted{$\unsure{x\in}$}','unresolved crossed symbols','low','Both symbols crossed.')
DO('P39 chance','chance','same reading','medium','Compressed a/n/c/e joins; distinctive beginning/end favor chance.')
DO('P41 cancelled D’ailleurs',r'\deleted{\unsure{D’ailleurs}}','unreadable cancelled transition','low','Not every letter separates from strike.')
DO('P41/P42 raised and live transition',r'\inserted{\unsure{Plus}} \unsure{précis,}','H bien','low','Nearby crossed writing and punctuation remain unresolved.')
DO('P42 cancelled réciproquement',r'\deleted{\unsure{réciproquement}}','unreadable cancelled group','low','Some descenders survive, but not every letter.')
DO('P42 cancelled quantifier',r'\deleted{$\unsure{\forall i\in I|\{i\}}$}',r'\forall i\in I / \{i\}','low','Parallel strikes obscure center of formula.')
DO('P43 cancelled quantifier',r'\deleted{$\unsure{\forall i\in I}$}','crossed formula unresolved','low','Formula body not recoverable independently of context.')
DO('P43 tiny introducer',r'\unsure{or|où}','or / où','low','Short right shoulder and no secure diacritic; do not decide from grammar.')
DO('P47 partitions wording','partitions ensembliste de X','partition ensembliste de X','medium','Terminal short s-like hook retained; compressed ending.')
DO('P48 live group below cancellation',r'\unsure{tels que}','unresolved short live group','low','Crowding from strike returns.')
DO('P49 disjoints','disjoints','same reading','medium','Ending -oints compressed, distinctive d/i/j support resolution.')
DO('P51 final fermé','fermé','same reading','medium','Small f-loop and accented e support reading; inner r/m joins crowded.')

REPORT['notes']=[
 dict(id='N01',text='The sheet is a landscape double leaf with handwritten folio 1, a wide left discussion and narrower right continuation. It develops specialization preorders, the associated topology on a preorder, two functors and an adjunction, then asks which preorders a pseudo-partition determines. The upper-right asterisk note asks “quelles conditions supplémentaires ... imposer pour avoir unicité ?”. This is a report of source contents, not verification of its claims.'),
 dict(id='N02',text='Several apparent slips are preserved: the NB1 closure equivalence uses a written ≤ where the earlier definition uses subset; the two identity subscripts are written E then O; the Posons insertion appears to use inverse image of I although its left index is J; the summand in the left closure formula is unstarred X_j. These are visual diagnostics only. Parent will append any independently performed mathematical checks.'),
 dict(id='N03',text='Source grammar is preserved, including “cette préordre”, “les réunions de fermés est fermé”, and “partitions ensembliste”. The opening parenthesis in the identity-map explanation has no written closing parenthesis after NB2. No missing punctuation or grammatical word has been supplied.'),
 dict(id='N04',text='Whole image and both supplied native halves were inspected once; required places P01–P52 were inspected once each. P53 completes only the clipped extreme-right punctuation of P35. P54 inspects previously uncropped specialization underlining. P55 was a clipped context fragment; P56 completes only its missing NB. 2 heading. No OCR, outside research or TeX compilation was used. line_count counts nonempty logical draft lines, including display and diagram rows.'),
 dict(id='N05',text='The short horizontal stroke below the adjunction explanation is rendered as a paragraph separator. Its source position starts far left of I→X and lies below the sentence baseline, so it is not assigned as a certain underline.'),
]
REPORT['notation']=[
 dict(form=r'\phi',meaning="ϕ : l’ensemble vide",evidence='Four right-column crossed-loop signs in X=φ and X_i*≠φ; P33/P34.'),
 dict(form=r'\operatorname{Ord}(X)',meaning='Specialization preorder attached to a topological space; initial operator name remains overwritten Ord/Spéc.',evidence='Top definition and repeated Ord labels in diagram and adjunction.'),
 dict(form=r'\operatorname{Esp}(I)',meaning='Topology on a preorder with downward closed sets and upward open sets as specified by source.',evidence='Left definitions of closed A and basis I_{≥x}.'),
 dict(form=r'\overline{\{x\}},\ \widetilde{\{x\}}',meaning='Closure for I and the opposite preorder I° respectively.',evidence='Source says the wave denotes l’adh. pour I°; basis formula and closure identity.'),
 dict(form=r'X_J^*,\ X_i^*',meaning='Pieces and inverse-image unions associated to the pseudo-partition; written Posons argument is preserved as I.',evidence='Left lower Posons insertion and union formula.'),
 dict(form=r'\mathcal E,\ \mathcal O',meaning='Category labels beside (Esp) and (Préord).',evidence='Complete two-arrow diagram, P14; identity subscripts preserved as E then O.'),
 dict(form=r'\operatorname{Ord}\cdot\operatorname{Esp},\ \operatorname{Esp}\circ\operatorname{Ord}',meaning='Two visually different composition marks, a filled dot then open circle.',evidence='P15 first and second identities.'),
]
REPORT['abbreviations']=[
 dict(form=a,expansion=b) for a,b in [
 ('ssi','si et seulement si'),('ens / ens.','ensemble(s)'),('top.','topologie / topologique'),
 ('t.q.','tel(s) que'),('adh.','adhérence'),('gén.','généralement'),
 ('néc.','nécessairement'),('quelc.','quelconques'),('cond.','condition'),
 ('i.e.','id est'),('tt / tte','tout / toute'),('loct. / locᵗ. / loc.','localement'),
 ('val.','valeurs'),('surj.','surjective'),('s.','suffit / suffisant'),
 ('f.','faut; fermé in loc. f.'),('assoc.','associée'),('d’équiv.','d’équivalence')]]
REPORT['hand']=[
 dict(habit='A loop crossed by a long shaft is the author’s phi-shaped empty-set sign.',places='P33/P34, four occurrences',consistency='All four locally compared examples agree.',witness_errors='C varnothing and H emptyset regularize the glyph.'),
 dict(habit='Capital I has top and bottom bars; J has a hooked lower return.',places='P19 inverse-image argument; nearby J under X and J criterion P37',consistency='Local comparison supports I in the inserted argument at medium confidence.',witness_errors='Both witnesses read expected J in P19.'),
 dict(habit='Curved insertion leaders can resemble parentheses or cancellation strokes.',places='P09 generalization; P19 Posons; P31 small par; P43 superset insertion',consistency='Attachment assessed separately at each place; small par enclosure remains unresolved.',witness_errors='H supplies parentheses at P09; both witnesses strike live continue ssi at P19.'),
 dict(habit='Repeated tracing of one word or X is not a separate cancelled duplicate.',places='P22 first complement X; P34 Supposons',consistency='Only one body occupies each baseline location.',witness_errors='H introduces an extra struck X and a struck duplicate Supposons.'),
 dict(habit='Abbreviation stops and vertical position vary.',places='P11 néc.; P26 baseline loct.; P46 raised t with baseline stop',consistency='Each occurrence read separately rather than regularized.',witness_errors='H expands néc. and several f./s./assoc. forms; omits stops or changes t position.'),
 dict(habit='Terminal pen returns can look like final s.',places='P29 quel; P46/P49/P50 telle; P47 partitions',consistency='Singular quel/telle supported; partitions ending retained with medium confidence.',witness_errors='C quels; H several telles/plural family readings.'),
 dict(habit='The lowered f/p descenders may resemble underlines.',places='P45 stratification fidèle; P08 next-line une beneath NB1',consistency='No independent underlines at those two places; true separate rules at P54, P56 and ordonné P46.',witness_errors='C underlines NB1 and stratification fidèle.'),
]

coverage={
 1:'H editorial leaf description excluded; manuscript folio 1 retained and audited.',
 2:'Editorial pagination context excluded; mspage 1 retained.',
 3:'P01 unresolved Ord/Spéc.',4:'H editorial doubt note excluded; P01 records uncertainty.',
 5:'P03 inner parentheses retained.',6:'P03 separate outer close retained.',
 7:'P05a no stop after ens.',8:'P06a no semicolon.',9:'P06b no semicolon.',
 10:'P06c literal wave, not ou.',11:'Display delimiters only; same Esp(I).',
 12:'P07 cancelled phrase unresolved; P08 NB1; H narrative note excluded.',
 13:'P07 retained uncertainty and P08 plain NB1.',
 14:'Display macro only.',15:'Alignment macro only.',
 16:'Display macro plus P09b no independent opening parenthesis.',
 17:'P10 cancelled Vue/lien and P09b no closing parenthesis; H attachment note editorial.',
 18:'H editorial reference to NB1, not additional manuscript text.',
 19:'H editorial-note boundary; NB. 2 retained, punctuation P56.',
 20:'P11a un.',21:'P11b néc., M0242 resolved.',
 22:'P11c ce sera celui de, M0243 resolved; preceding cancelled word remains illegible.',
 23:'P12a intersections plural; no extra cancelled word.',24:'P12a sont ouverts plural.',
 25:'P12b straight quote strokes.',26:'P12b opposée.',
 27:'P13 unresolved Ceci/Cas; H explanatory note excluded.',28:'P13 one point, no de.',
 29:'Diagram wrapper only; complete diagram independently inspected P14.',
 30:'Diagram layout option only.',31:'Equivalent two-arrow layout, Ord right/Esp left verified P14.',
 32:'Membership included in diagram; H records it in editorial note.',
 33:'Equivalent lower leftward Esp arrow verified P14.',
 34:'Rotated memberships, X and I transcribed in complete diagram; H describes same ink in note.',
 35:'Display delimiter only.',
 36:'P15a no comma; shared filled-dot correction also logged.',
 37:'H explanatory note excluded; P15a/b identity subscripts visually resolved and source order retained.',
 38:'H thin-space command, not a literal comma; same reading.',
 39:'H thin-space command, not a literal comma; same reading.',
 40:'P16 no closing parenthesis; digit 2 audited.',
 41:'Display scope only; adjonction remains on source baseline.',
 42:'Display scope only; whole adjunction inspected P17.',
 43:'P18 explicit colon/period doubt.',
 44:'P20 unstarred X_i, M0247 resolved.',
 45:'Dotless-i accent macro only; complete first union read P22.',
 46:'P22a no separate struck X.',
 47:'Dotless-i accent macro only.',
 48:'P22b two-row subscript, no written comma.',
 49:'P23a no donc and source underline under faut.',
 50:'Display delimiter only.',51:'Dotless-i accent macro only; unstarred final X_j preserved.',
 52:'Display delimiter only.',53:'P25 union glyph.',
 54:'Dotless-i accent macro only.',55:'P26a baseline loct. and straight quotes.',
 56:'P26b à ens. de val.',
 57:'P27 cancelled damaged line retained; H mathematical editorial note excluded.',
 58:'P27 unresolved opening relation and retained central formula; H editorial note excluded.',
 59:'P27 uncertain final en retained.',
 60:'P28a unresolved first marginal phrase.',61:'P28b unresolved quotient en I implique.',
 62:'P28b retains written topo.',63:'P28c mal posée -- plutôt.',
 64:'P28d full request retained.',65:'P28d lower margin completed; H editorial note excluded.',
 66:'P29a singular quel.',
 67:'P31a source placement of star and small par; no insertion before la famille.',
 68:'P31a source question order retained.',
 69:'P31b donné on baseline retained; cancelled cluster and raised plus précisément separated.',
 70:'P32 cancelled candidate remains uncertain.',
 71:'P34a only one retraced Supposons.',
 72:'P35/P53 no independent punctuation at right edge.',
 73:'P36 singular est fermé retained.',74:'P36 placement and singular agreement retained.',
 75:'P37a aura.',76:'P37b cancelled x∈ unresolved.',
 77:'P38 cette préordre est-il.',78:'P38 un, without d apostrophe.',
 79:'P39a straight quote strokes.',80:'P39a straight close quote strokes.',
 81:'P39a aura tte chance; M0251 resolved medium.',
 82:'P39b chaotique.',83:'P39c short s.',
 84:'P40 singleton braces, not overbar.',
 85:'P41a implique.',86:'P41b sont loct. on baseline.',
 87:'P41c/P42a/P42b retain explicit doubts and revision states.',
 88:'P42c f. retained.',89:'P42c s. retained.',
 90:'P42d inserted ∀i∈I read.',
 91:'P42e/P43a cancelled formula doubts and complete singleton equality/order retained.',
 92:'Dotless-i accent macro only; P43a complete equality read.',
 93:'Dotless-i accent macro only; P43a complete equality read.',
 94:'P43a source order, no puisque; P43b or/où unresolved; P43c insertion attachment.',
 95:'P43b/c source text and superset attachment, not H reordered clause.',
 96:'P43c/d superset insertion, straight quotes and par.',
 97:'P44 assoc. retained.',98:'Dotless-i accent macro only.',
 99:'P45 une present and straight opening quotes.',
 100:'P45 straight close quotes; no underline.',
 101:'P46a distinct stop, raised t; M0254 resolved.',
 102:'P46b singular telle.',
 103:'P46c à une famille; P48a insertion attaches to following partition line.',
 104:'P47 partitions is on baseline, not insertion.',
 105:'P47 partitions ensembliste.',
 106:'P47 unindexed X and P48a indicée par.',
 107:'P48a/b complete insertion, cancellation and doubtful live tels que retained.',
 108:'P49 disjoints resolved medium and singular telle.',
 109:'P50 singular telle.',
 110:'P50/P51 source comma after fermés; no opening parenthesis before i.e.',
 111:'P51 est retained and fermé resolved medium.',
 112:'P51 inner parenthesis before second implication retained.',
 113:'H editorial note excluded; no ellipsis introduced for its prose description.',
}
with (ROOT/'packets/150_scan003/differences.tsv').open() as f:
    diffrows=list(csv.DictReader(f,delimiter='\t'))
assert len(diffrows)==113 and set(coverage)==set(range(1,114))
REPORT['diff_coverage']=[dict(row=i,disposition=coverage[i]) for i in range(1,114)]

reviews=[
 (r'\inserted{pré} (two left occurrences)','Each raised prefix attaches directly before ordonné.','P02/P05 actual ink, not editorial supply.'),
 (r'\deleted{\unsure{lien foncteurs|\illegible{1} fondamentales}}','First left marginal cancellation.','P07: cancellation masks low joins; no resolved phrase.'),
 (r'\inserted{Plus gén. ...}','Generalizes NB1, attached by long curved leader.','P09: no independent parentheses.'),
 (r'\deleted{\unsure{Vue|lien}}','Second left marginal cancellation.','P10: V-like tall strokes and final e favor Vue, but crossed low joins remain unresolved.'),
 (r'\deleted{\illegible{1}}','Small cancelled word after unique in NB. 2.','P11: remains unreadable; ce sera celui de follows live.'),
 (r'\deleted{une}','Only une before pseudo-partition is cancelled.','P18: separate crossed word before live pseudo-partition.'),
 (r'\inserted{Posons $X_J^*=\varphi^{-1}(I)$, les}','Raised over the continuing sentence.','P19: leader bends left/down; RHS I read from top/bottom bars.'),
 ('continue ssi','Live words under Posons insertion, not struck.','P19: no independent stroke through bodies; former deletion state remains locally uncertain.'),
 (r'\inserted{de $I$}','Attaches after fermé in finite-case parenthesis.','P25/P52: de partly overlaps preceding descender; top/bottom of I completed in P52.'),
 (r'\deleted{\illegible{3} ... \unsure{en}}','Damaged cancelled upper-edge line, kept as a margin item.','P27: central formula survives; initial/final groups uncertain.'),
 ('* comme on veut ... avoir unicité ?','Upper-right note called by star after the right-column opening question.','P28 with lower overlap P29; full six-line note retained.'),
 (r'\inserted{pré}','Raised above right-column ordre.','P29: prefix and independent underline visible.'),
 (r'\inserted{\unsure{(par)}}','Small insertion after question and star; exact enclosure unresolved.','P31: enclosure touches leader; no certainty inferred from syntax.'),
 (r'\deleted{\illegible{3}} \inserted{plus précisément}','Raised replacement over cancelled lower-baseline cluster.','P31: only plus précisément raised; par (X_i*)...donné remains baseline live text.'),
 (r'\deleted{\unsure{tout}}','One cancelled group after quand.','P32: d/apostrophe-like opening, unreadable crossed remainder.'),
 ('Supposons','One live retraced word.','P34: no separate cancelled duplicate.'),
 (r'\inserted{(cas $\varphi$ loc. finie)}','Attaches after singular est fermé.','P36: raised line and leader separate from baseline verb.'),
 (r'\deleted{$\unsure{x\in}$}','Crossed symbols before ∀J.','P37: candidate remains doubtful.'),
 (r'\deleted{\unsure{D’ailleurs}} \inserted{\unsure{Plus}}','Raised replacement over a cancelled transition.','P40/P41: letters partially crowded; uncertainty retained.'),
 (r'\unsure{précis,} \deleted{\unsure{réciproquement}}','précis-like live group and a separate crossed lower group.','P42: exact letters/punctuation and cancellation text remain doubtful.'),
 (r'\inserted{$\forall i\in I$}','Inserted before l’on ait.','P41/P42: complete quantifier visible with leader.'),
 (r'\deleted{$\unsure{\forall i\in I|\{i\}}$}','Cancelled immediately after l’on ait.','P42: parallel strike strokes, no full resolution.'),
 (r'\deleted{$\unsure{\forall i\in I}$}','Cancelled after ce qui équivaut à.','P43: formula remains doubtful; no grammar-based resolution.'),
 (r'\inserted{$\supset X_i^*$}','Attaches after X in le plus petit fermé de X.','P43: enclosing curved leader is not extra text or independent parentheses.'),
 (r'\inserted{indicée par $I$ ordonné}','Raised after partition/family phrase.','P48: separate from cancellation below.'),
 (r'\deleted{\illegible{4}} \unsure{tels que}','Heavily crossed group, then low live group.','P48: low candidate is not fully recoverable; no words silently omitted.'),
 (r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ est fermé ($\Rightarrow$ les $X_i^*$ loc. f.)}','Inserted after a) condition, before b).','P51: no outer opening parenthesis at i.e.; inner implication has its own parentheses.'),
]
REPORT['deletion_insertion_review']=[dict(text=norm(t),scope_attachment=s,evidence=e) for t,s,e in reviews]

# Exact original mark ordering, required keys and geometric sanity are validation
# of the deliverable structure, not a second manuscript reading.
with (ROOT/'packets/150_scan003/marks.tsv').open() as f:
    marks=list(csv.DictReader(f,delimiter='\t'))
assert [x['id'] for x in REPORT['decisions']]==[x['id'] for x in marks]
for a in REPORT['changes']:
    assert (ROOT/'work'/a['crop']).exists()
    x0,y0,x1,y1=a['box'];assert 0<=x0<x1<=2557 and 0<=y0<y1<=1955
for a in REPORT['audit_boxes']:
    x0,y0,x1,y1=a['xyxy'];assert 0<=x0<x1<=2557 and 0<=y0<y1<=1955
(OUT/'report.json').write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),marks=len(REPORT['decisions']),
    inventory=len(REPORT['inventory']),audit_boxes=len(REPORT['audit_boxes']),
    doubts=len(REPORT['doubts']),diff_rows=len(diffrows),source_mismatches=source_mismatches),
    ensure_ascii=False,indent=2))
