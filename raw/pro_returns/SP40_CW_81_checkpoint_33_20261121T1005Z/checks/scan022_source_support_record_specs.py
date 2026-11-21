"""Public source wording for scan022; every ink/count choice comes from root."""

SIGMA = {
 8:(1,r'\widehat{\Sigma}_\alpha^+'),9:(2,r'\widehat{\Sigma}_\alpha^+'),
 20:(4,r'\Sigma_\alpha^-'),22:(5,r'\Sigma_\alpha^+'),
 24:(6,r'\overline{\Sigma_\alpha^-}'),26:(7,r'\widehat{\Sigma}_\alpha^+'),
 28:(8,r'\overline{\Sigma_\alpha^-}'),29:(9,r'\widehat{\Sigma}_\alpha^+'),
 32:(10,r'\Sigma_\alpha^-'),33:(11,r'\overline{\Sigma_\alpha^-}'),
 36:(12,r'\overline{\Sigma_\alpha^-}'),37:(13,r'\overline{\Sigma_\alpha^-}'),
 48:(14,r'\widehat{\Sigma}_\alpha^-'),49:(15,r'\Sigma_\alpha^-'),
 57:(16,r'\widehat{\Sigma}_\alpha^+'),59:(17,r'\widehat{\Sigma}_\beta^+')}

# These public witness values describe the local object. Complete literal
# wording and apparatus remain attached through the frozen witness catalog.
WITNESSES = {
 1:(r'\deleted{On}',r'\struck{Un}'),
 2:('procède','procédé'),
 3:(r"\inserted{On note d'abord que}","On note d'abord que after the struck opening and pour prouver que"),
 4:('Opening deletion macros; no two literal cancellation paths','Opening struck passage; insertion/placement count belongs to L03'),
 5:('No explicit slash below pour in the complete local source','No explicit slash below pour in the complete local source'),
 6:(r'X\setminus',r'X\smallsetminus'),
 7:(r'\bigcup_{\alpha\in K}',r'\bigcup_{\alpha\in K}'),
 10:(r'\unsure{(}',r'('),
 11:('One closing parenthesis command after the qualified disjoints/disjointes; no separate close after K','Inner close after alpha in K and outer close after disjoints'),
 12:('étant','étant'),13:(r'\unsure{disjoints|disjointes}','disjoints'),
 14:(r'\underbrace with rotated = beneath','Apparatus describes an accolade under the first expression and the added = intersection below it'),
 15:(r'\inserted{\bigcap_{\alpha\in K}\Sigma_\alpha^-}',r'Apparatus quotes =\bigcap_{\alpha\in K}\Sigma_\alpha^- below the accolade'),
 16:(r'\left\{ for the two conditions',r'\left\{ for the two conditions'),
 17:('trivial with a crossing rightward arrow','trivial at the left of the second line; apparatus supplies no crossing arrow'),
 18:(r'\deleted{\unsure{\ne|=}}','Apparatus identifies a struck = replaced by the live nonempty relation'),
 19:(r'\deleted{\varnothing} beside the old relation','No old empty-set component is supplied in the apparatus about the struck ='),
 21:('alors que','dès que'),
 23:('précise with acute; no separate adjacent tick','précise with acute; no separate adjacent tick'),
 25:(r'\inserted{\overline V\cap\widehat{\Sigma}_\alpha^+} and \inserted{\overline{\Sigma_\alpha^-}\cap\widehat{\Sigma}_\alpha^+}', 'Apparatus describes one struck lower line containing the two expressions'),
 27:(r'\rotatebox{90}{$\unsure{\deleted{=}|=|\Rightarrow}$}','No right-hand vertical connector is supplied; the apparatus quotes an equals only before the left lower expression'),
 30:('Separate deletion wrappers without the literal enclosing/crossing frame paths','Apparatus explicitly describes an enclosing line and several long diagonal cancellations'),
 31:(r"Comme V\subset\Sigma_\alpha^-, on a V\cap E_\alpha\subset\overline{\Sigma_\alpha^-}\cap E_\alpha, prouvons l'inclusion inverse",r"Comme V\subset\Sigma_\alpha^-, on a V\cap E_\alpha\subset\overline{\Sigma_\alpha^-}\cap E_\alpha, prouvons l'inclusion inverse"),
 34:('No separate left-of-frame trace in the complete local source','No separate left-of-frame trace in the complete local source'),
 35:('Cancelled inverse-inclusion expression without a terminal period','Cancelled inverse-inclusion expression with a terminal period'),
 38:('i.e. with both points; complete cancelled x/neighbourhood wording','i.e. with both points and a TeX space; complete cancelled x/neighbourhood wording'),
 39:('rencontre, without an additional word or period',r'rencontre \ill{}.'),
 40:(r'\deleted{\unsure{on}}',r'\ill{} immediately after Or'),
 41:('peut','par'),42:('considérer','construction'),
 43:(r'\deleted{\unsure{formule|relation}}','Apparatus describes an unspecified struck word replaced by égalité'),
 44:('No explicit point beside the old noun','No explicit point beside the old noun'),
 45:(r'\deleted{\inserted{égalité}}','égalité in the struck passage; apparatus says it replaces a struck word'),
 46:('égalité after comme','égalité after comme'),
 47:(r'\deleted{\unsure{Y|Z}}','Apparatus explicitly identifies a struck X before the displayed equals'),
 50:('dans lequel','dans laquelle'),51:('fermées, acute','fermées, acute'),
 52:('No explicit two-point cluster at the right edge','No explicit two-point cluster at the right edge'),
 53:(r'\uline{fermées}','fermées without emphasis'),
 54:('Live fermées with acute; no independent adjacent upper tick','Live fermées with acute; no independent adjacent upper tick'),
 55:(r'\uline{disjointes}',r'\emph{disjointes}'),
 56:('No explicit detached lower slash','No explicit detached lower slash'),
 58:('Z followed by ordinary equals','Z followed by ordinary equals'),
 60:('No explicit interior point in the last Sigma','No explicit interior point in the last Sigma'),
 61:('No explicit point below/right of the last beta','No explicit point below/right of the last beta'),
 62:(r'\bigcup_{\beta\in K\setminus\{\alpha\}}',r'\bigcup_{\beta\in K\smallsetminus\{\alpha\}}'),
 63:(r'et on doit prouver; \overline{(X\setminus(Y\cup Z))}\cap Y=\overline{(X\setminus Y)}\cap Y',r'et on doit prouver; \overline{\bigl(X\smallsetminus(Y\cup Z)\bigr)}\cap Y=\overline{(X\smallsetminus Y)}\cap Y'),
 64:('ce qui est immédiat','ce qui est immédiat.'),
 65:('% archive sheet number: 21',r'\page{21}; administrative mapping'),
 'ROOT-M01':('No explicit point beside the plain V in the complete local source','No explicit point beside the plain V in the complete local source')}
for locus,(_,formula) in SIGMA.items(): WITNESSES[locus]=(formula,formula)
WITNESSES[24]=(r'\overline V\cap E_\alpha=\overline{\Sigma_\alpha^-}\cap E_\alpha (qui est donc \ne\varnothing)',)*2

# Literal source choices used when a reader supplied no difference-list row.
# Every one is accompanied by that reader's complete stored source context.
SILENT = {
 4:{'A':'A022-G01-opening-cancellations contains both literal long cancellation paths.','C':'The complete opening source uses deletion wrappers; it supplies no matching two-path opening-cancellation group.'},
 5:{'A':'No explicit below-pour slash in the complete local source and original group registry.','C':'No explicit below-pour slash in the complete local source and original group registry.'},
 6:{'A':'A022-G02-initial-separator supplies the short upright separator after the separate X label.','B':'The complete opening V/X expression supplies its setminus separator.','C':'The complete opening V/X expression supplies its setminus separator.'},
 7:{'A':'A022-G03-initial-union supplies the continuous union body and full alpha-in-K limit.','C':'C022-G01 supplies the complete union and alpha-in-K limit within the opening compound source.'},
 8:{'B':'B022-S01 is a connected head/body with roof, alpha and raised plus; no local role qualifier.'},
 12:{'B':'étant, with acute, in the complete parenthetical source.','C':'étant, with acute, in the complete parenthetical source.'},
 15:{'A':'A022-G06-intersection-insertion and A022-S03 supply the inserted intersection, complete limit and connected minus-alpha Sigma.','B':'B022-G06 and B022-S03 supply the inserted intersection, complete limit and connected minus-alpha Sigma.','C':'C022-G01 and C022-S03 retain the inserted intersection, complete limit and minus-alpha Sigma.'},
 22:{'B':'B022-S05 supplies a connected head/body, alpha and raised plus.'},
 23:{'B':'The complete word source is précise with acute; no independently grouped adjacent tick.','C':'The complete word source is précise with acute; no independently grouped adjacent tick.'},
 24:{'A':'Complete main equality and nonemptiness parenthesis, with joined A022-S06 and its separate closure, minus and alpha.','B':'Complete main equality and nonemptiness parenthesis, with joined B022-S06 and its separate closure, minus and alpha.','C':'Complete main equality and nonemptiness parenthesis, with C022-S06, closure, minus and alpha.'},
 29:{'A':'A022-S09 is joined, with its complete roof, plus and alpha.','B':'Complete hatted plus-alpha Sigma S09 within the lower-right B022-G12 formula.'},
 31:{r:'Complete cancelled Comme line retains plain V after on a, and prouvons l’inclusion inverse.' for r in 'ABC'},
 32:{'A':'A022-S10 supplies the joined minus-alpha Sigma in the cancelled Comme line.','B':'Complete B022-S10 minus-alpha Sigma in the cancelled Comme line.'},
 36:{'A':'Complete barred minus-alpha A022-S12 in the cancelled inverse inclusion.','B':'B022-S12 has connected returning head/body, separate upper closure, minus and alpha.','C':'Complete C022-S12 with its upper closure, minus and alpha.'},
 38:{r:'Complete cancelled Soit/x/neighbourhood source retains i.e. with both points and the following x, W and rencontre wording.' for r in 'ABC'},
 44:{'A':'No explicit separate point beside the old noun in the complete local source and original group registry.','C':'No explicit separate point beside the old noun in the complete local source and original group registry.'},
 45:{r:'Inserted égalité retained inside the cancelled passage, with its complete local state source.' for r in 'ABC'},
 46:{'A':'The second égalité after comme has a firm acute in the complete source.','C':'The second égalité after comme has a firm acute in the complete source.'},
 51:{'B':'The complete cancelled word is fermées with firm acute.','C':'The complete cancelled word is fermées with firm acute.'},
 52:{'A':'No explicit right-edge two-point cluster in the complete local source and original group registry.','C':'No explicit right-edge two-point cluster in the complete local source and original group registry.'},
 54:{'B':'Complete live fermées with acute; no independent adjacent upper-tick group.','C':'Complete live fermées with acute; no independent adjacent upper-tick group.'},
 55:{'A':'Complete disjointes word and second separate A022-G15 underline.','B':'Complete disjointes word and second separate B022-G16 underline.','C':'Complete underlined disjointes in the final live restart.'},
 57:{'A':'A022-S16 retains the joined head/body, roof, plus and alpha.','B':'B022-S16 retains the joined head/body, roof, plus and alpha.'},
 58:{'A':'A:T67 contains Z followed by ordinary equals.','B':'The complete Z definition source contains ordinary equals.'},
 61:{'C':'No explicit below-beta point in the complete final Sigma source and original group registry.'},
 62:{r:'Complete lower union and beta-in-K-setminus-braced-alpha limit in the stored final definition source.' for r in 'ABC'},
 63:{r:'Complete et on doit prouver and the two-sided barred closure/intersection equality in the final stored source.' for r in 'ABC'},
 65:{r:'Archive sheet number 21 is retained as a source comment.' for r in 'ABC'},
 'ROOT-M01':{r:'No explicit plain-V-adjacent point in the inspected complete local source and original group registry.' for r in 'ABC'}}

NODE_SCOPES={1:['T01'],2:['T02'],3:['T05'],4:['T01','T02','T03','T04','T06'],5:['T06'],6:['T07','T08'],10:[],11:['T11'],12:['T11'],13:['T11'],16:['T13','T14'],17:['T12'],18:['T15'],19:['T15'],21:['T16'],23:['T19'],24:['T20','T21','T22'],31:['T23','T24','T25','T26','T27','T28','T29','T30'],35:['T31'],38:['T32','T33','T34','T35','T36','T37','T38','T39','T40','T41','T42'],39:['T42','T43'],40:['T44'],41:['T45'],42:['T46','T47'],43:['T48','T49'],44:['T48'],45:['T49'],46:['T50','T51','T52','T53'],47:['T54','T55','T56'],50:['T57','T58','T60','T61'],51:['T59'],53:['T63'],54:['T63'],55:['T64'],57:['T65','T66'],58:['T67'],'ROOT-M01':['T26']}

GROUP_OVERRIDES={
 18:['B022-G08'],19:['B022-G08'],
 15:['B022-G06','B022-S03'],
 25:['A022-G10-lower-annotations'],
 27:['A022-G11-right-connector','A022-S08'],
 30:['A022-G14-cancellation-frame'],
 33:['A022-S11','A022-G14-cancellation-frame'],
 40:['A022-G12-local-on-and-noun-cancellations'],
 43:['A022-G12-local-on-and-noun-cancellations'],
 53:['A022-G15-live-underlines'],55:['A022-G15-live-underlines']}

ALT={
 1:'On',2:'procéde; procédé; procede',
 11:'Two separate closing parentheses; complete upper and lower edge runs retained under either count/attachment reading.',
 18:r'\deleted{=}; the old empty-set component and the separate live \ne\varnothing continuation remain present.',
 25:r'\deleted{\inserted{\overline V\cap\widehat\Sigma_\alpha^+},\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+}}; primary is the complete live inserted pair.',
 27:'Live vertical equals; arrow-like form. Primary remains deleted vertical equals; one shared S08 horizontal run retained.',
 33:r'\Sigma_\alpha^- without a closure reading of the shared upper run; the complete barred primary, upper-rule role and cancelled-passage state remain explicit.',
 40:'The supplied on candidate remains qualified; no further supported word candidate is supplied.',
 46:'egalité, unaccented',47:'Deleted Z; deleted X; complete Y-like primary and its local crossings retained.',
 51:'fermé es without the inserted space (acute alternative); fermees (unaccented alternative).'}
ALT[51]=r'ferm\unsure{é|e}es as the acute/unaccented alternatives to grave-primary ferm\unsure{è|é|e}es.'
for l in [8,9,20,22,26,28,32,37,48,49,59]:
 ALT[l]='Short head as letter head or retrace; independent upper-run role remains unresolved. The complete sign, index and any roof/closure are retained.'
for l in [5,23,34,44,52,54,56,60,61,'ROOT-M01']:
 ALT[l]='No character, punctuation or operation assigned; attachment, role, hand and surface origin remain unresolved.'
ALT[58]='Precise relation-role allocation remains unresolved; equals is the primary of the complete returning literal form.'

KIND={l:'drawing or diagram' for l in range(1,66)}
for l in [1,2,12,13,21,41,42,43,46,50,51]:KIND[l]='misread word'
for l in [3,15,45]:KIND[l]='insertion or placement'
for l in [5,23,34,44,52,54,56,60,61]:KIND[l]='omission'
for l in [25,27]:KIND[l]='deletion state (struck given live or live given struck)'
for l in [6,10,18,47,58]:KIND[l]='misread symbol or index'
for l in [35,39,64]:KIND[l]='text not on the page'
KIND[40]=r'readable ink left as \ill{}'
for l in [24,31,38,55,62,63,65]:KIND[l]='other'
KIND['ROOT-M01']='omission'

S_STATUS='The range 81/15–22 quotes Sigma_1^+ and U_s with no exact local counterpart in the complete 022 reading; no locally applicable quoted correction on 022, no bar added from the range; its author states no scan viewed. This records transcription scope only, without confirming or refuting the mathematical argument.'

NOTES=(r'The cancelled opening proposes a recurrence on $\operatorname{card}K$; the inserted restart is “On note d’abord que”. The manuscript gives the nonempty and empty intersection conditions and writes $\overline V\cap E_\alpha=\overline{\Sigma_\alpha^-}\cap E_\alpha$, followed by “qui est donc $\ne\varnothing$”. Its cancelled inverse-inclusion and neighbourhood argument contains the locally struck on and the replacement of formule by inserted égalité. The plain V after on a and the locally qualified shared rules are retained as written. The live restart names two closed disjoint parts Y and Z and ends with $\overline{(X\setminus(Y\cup Z))}\cap Y=\overline{(X\setminus Y)}\cap Y$, called “ce qui est immédiat” by the author. These statements remain attributed to the manuscript; no mathematical check was performed.')
