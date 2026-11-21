from pathlib import Path
import json, re
root=Path('/workspace/scratch/8759b8008681')
out=root/'work/reports/149_scan133'
c=(root/'packets/149_scan133/C.tex').read_text()
h=(root/'packets/149_scan133/H.tex').read_text()
boxes=json.loads((out/'crop_boxes.json').read_text())
r={'page':'149_scan133','reader':'reader_b','line_count':26,'changes':[],'decisions':[],'inventory':[],'audit_boxes':[],'doubts':[],'notes':[],'check_events':[],'notation':[],'abbreviations':[],'hand':[],'diff_coverage':[],'deletion_insertion_review':[]}
def change(id,place,cv,hv,final,evidence,crop,confidence,kind,ac,ah,mh,con,cat):
    r['changes'].append(dict(id=id,place=place,c=cv,h=hv,final=final,evidence=evidence,crop=f'crops/149_scan133_{crop}.png',box=boxes[crop],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=mh,consequential=con,error_category=str(cat)))
def decision(id,dec,reading,evidence,crop,conf):
    r['decisions'].append(dict(id=id,cote='149',scan='133',decision=dec,reading=reading,evidence=evidence,crop=f'crops/149_scan133_{crop}.png',box=boxes[crop],confidence=conf))
def audit(kind,box,reading):
    r['audit_boxes'].append(dict(box=f'B{len(r["audit_boxes"])+1:02d}',kind=kind,xyxy=box,reading=reading))
def inv(kind,pos,words):
    r['inventory'].append(dict(scan='149_scan133',sheet_kind='text',hand='his hand',element=f'E{len(r["inventory"])+1:02d}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
def doubt(place,reading,alternatives,confidence,reason):
    r['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))

# Draft changes are only visual decisions recorded below.
draft=c
replacements={
 r'\varnothing':r'\phi',
 r'\unsure{\underline{D}_J|\bar D_J}':r'\bar D_J',
 r'\unsure{soit}':'soit',
 r'\unsure{composantes|comp.}':'composantes',
 'correspondent aux comp.':'correspondent comp.',
 r"\unsure{l'ombre}":"l'ombre",
 "``compactification''":r"``\unsure{compactification|complétification}''",
 r'\unsure{\infty}':r'\infty',
 r'\unsure{connexes}':'connexes',
 r'\uline{\unsure{pas}}':r'\uline{pas}',
 r'\unsure{ombres}':'ombres',
 r'\inserted{$=X_J\setminus D_J$,}':r'\inserted{$=X_J\setminus D_J$}',
 r'U_{\unsure{\xi}}':r'U_\xi',
 r'\unsure{T^J|\bar T^J}':r'T^J',
 r'\inserted{(par image inverse)}':r'\inserted{par image inverse}',
 r'\unsure{\mathrel{\text{---}}|=|\ldots}':r'\unsure{\mathrel{\cdot-}}',
 r'\unsure{alg. sép.|alg.}':'alg sép',
 r'\unsure{tubulures}':r'\unsure{tubes|tubulures}',
 r'\margin{plutôt $T^J$}':r'\margin{plutôt}',
 r'\unsure{U_{J\alpha}}':r'U_{J\alpha}',
 r'\unsure{\tilde X_{J\alpha}}':r'\tilde X_{J\alpha}'
}
for old,new in replacements.items():
    assert old in draft, old
    draft=draft.replace(old,new)
# Marginal blocks retain their internal writing order; put the small annotation
# immediately after the sequence to which it points, rather than duplicating T^J.
draft=draft.replace('\n\n\\margin{plutôt}\n','\n')
draft=draft.replace('\\]\n---','\\]\n\\margin{plutôt}\n---')

change('P00a','L1, first non-emptiness formula',r'$D_J\ne\varnothing$,',r'$D_J \neq \emptyset$',r'$D_J\ne\phi$,','The empty-set glyph has a loop traversed by a long descending stem, the phi form, rather than a slashed zero. A distinct curved comma follows it. Both witness set-symbol normalizations are replaced by the written glyph.','P00','high','misread symbol or index',True,True,False,False,1)
change('P00b','L1, on trouve sur I',r'on trouve sur $I$',r'on trouve, sur $I$',r'on trouve sur $I$','The terminal e of trouve returns into the following space without an independent comma; sur begins after that space. H supplies punctuation between these words.','P00','high','text not on the page',False,True,False,False,9)
change('P01','Top interlinear parenthesis, whole formula',r'\inserted{(i.e. $\unsure{\underline{D}_J|\bar D_J}=\bigcap_{j\in J}D_j$ \unsure{soit} $\ne\varnothing$)}',r'\add{(i.e.\ $D_J = \bigcap_{j \in J} D_j$ soit $\neq \emptyset$)},',r'\inserted{(i.e. $\bar D_J=\bigcap_{j\in J}D_j$ soit $\ne\phi$)}','A separate dark horizontal stroke lies above D; the hook below is J, not an underline. The small word has s, closed o, an i minim and a final t upright. The final empty-set sign again has a loop and long traversing stem. No separate comma follows the closing parenthesis. This resolves C marks M0183 and M0184 from the crop of the complete insertion.','P01','high','misread symbol or index',True,True,False,True,1)
change('P02','L2, first replaced noun and adjective',r'\deleted{\unsure{solide}} \inserted{maquette} simpliciale',r'\struck{schéma} \add{\uncertain{ensemble}} simplicial',r'\deleted{\unsure{solide}} \inserted{maquette} simpliciale','The inserted word has low m minims, a q descender and the tall double-t cluster followed by e: maquette. The following adjective ends in a separate e after l. The struck noun is heavily retraced; solide remains a cautious candidate, not a resolved cancellation.','P02','medium','misread word',False,True,True,True,2)
change('P03','L3, Les composantes',r'\unsure{composantes|comp.}',r'composantes','composantes','After comp the word continues through several connected letters, including the t ascender and final es; it is not the short abbreviation comp. Resolves C M0185.','P03','high','misread word',True,False,False,False,2)
change('P04','L4, correspondent comp. connexes','correspondent aux comp. connexes',r'correspondent \supplied{aux} comp.\ connexes','correspondent comp. connexes','The apparent stroke before comp. is continuous with the long descending q of topologique on the line above, turns right, and ends in a small loop. No independent u and x can be isolated. The grammatical aux is absent from the ink; H explicitly labels it supplied.','P04','medium','text not on the page',True,False,True,True,9)
change('P05a','L5, ou encore : celles de','ou encore : celles de',r'on connaît : celles du \uncertain{bout} de','ou encore : celles de','The first word ends with the open u return, not n. Encore has the low e/n/c sequence, round o and terminal re, without the ascenders/accents needed for connaît. After celles the ink is the short de; no independent du bout sequence intervenes.','P05','high','misread word',False,True,True,True,2)
change('P05b','L5–6, cancelled formula before hat X',r'$\deleted{\unsure{U_\infty}}\hat X\setminus D$',r'$\widehat{X} \setminus D$',r'$\deleted{\unsure{U_\infty}}\hat X\setminus D$','A cancelled cluster precedes the following live hatted X. Two joined low loops support the infinity subscript, while the upper U-shaped body is crossed by the deletion; uncertainty is retained. H omits the cancelled ink.','P05','medium','omission',False,True,False,False,3)
change('P06','L6 interlinear addition before complété',r"le \inserted{\unsure{l'ombre}} complété",r'le \add{\uncertain{formel}} complété',r"le \inserted{l'ombre} complété",'The raised word begins with a tall l and a separate apostrophe, then o, low m, tall b, r and e. It is l\'ombre, not formel. Its leader attaches before complété. The pre-existing le remains live, however awkward the resulting phrase. Resolves C M0186.','P06','high','misread word',True,True,True,True,2)
change('P07','L7, a un caractère invariant',r'a un caractère invariant p.r.',r'\ill{} une \uncertain{notion} \uncertain{invariante} \uncertain{p.r.}',r'a un caractère invariant p.r.','There is a small closed a before un; caractère shows the repeated c/r forms, crossed t and accented e. Invariant ends at t, with no final e. The p and r abbreviation remains short. H loses the readable a and substitutes notion/invariante.','P07','high','misread word',False,True,True,True,2)
change('P08','L8, quotation marks around the disputed noun',"``compactification''",'« complétification »',r"``\unsure{compactification|complétification}''",'Two short strokes open and two short strokes close the quoted word; they are not drawn guillemets. The compressed middle after comp and before f does not securely distinguish act from lét; that lexical uncertainty is retained separately and is not counted as a departure from C.','P08','medium','other',False,True,False,False,10)
change('P09','L9, infinity and connexes',r'$\unsure{\infty}$-\unsure{connexes}',r'$\infty$-connexes',r'$\infty$-connexes','The sign is formed by two connected loops. Connexes has the initial c/o, joined n minims, crossing x, and terminal es, with no obscured letters. Resolves C M0187 and M0188. The nearby non vides is a separate raised insertion between D_J and sont.','P09','high','misread symbol or index',True,False,False,True,1)
change('P10a','L10, underlined pas',r'\uline{\unsure{pas}}','pas',r'\uline{pas}','The p descender, closed a and terminal s are distinct above a separate short underline. Resolves C M0189 and preserves the source underline absent from H.','P10','high','other',True,True,False,False,10)
change('P10b','L10, sauf pour D_J',r'sauf pour $D_J$',r'si $J$ \uncertain{pour} $D_J$',r'sauf pour $D_J$','The word before pour contains the small s curl, an a oval, low u, and a tall crossing/descending f. It is sauf; no separate J occurs there.','P10','high','misread word',False,True,True,True,2)
change('P12','L12, beginning of the topologie clause','la topologie de notre',r"l'\struck{schéma} \add{\uncertain{ensemble}} simplicial exprime la topologie du",'la topologie de notre','The baseline begins with separate la, followed immediately by topologie (long p/g descenders) and the short words de notre. These precede the struck noun and raised replacement; H reverses that order and loses notre.','P12','high','omission',False,True,True,True,3)
change('P13','L12, second replaced noun and adjective',r'\deleted{\unsure{solide}} \inserted{maquette} simpliciale',r'\struck{schéma} \add{\uncertain{ensemble}} simplicial',r'\deleted{\unsure{solide}} \inserted{maquette} simpliciale','The second raised maquette again has the descending q and paired tall t strokes; simpliciale carries a final e. The cancelled baseline noun is retraced enough that the internal letters of solide cannot all be separated, so its uncertainty remains.','P13','medium','misread word',False,True,True,True,2)
change('P14','L13, le type d’homotopie','le type d\'homotopie','la topologie du type d\'homotopie','le type d\'homotopie','The new line starts with short le, then type with a long y descender. There is no second topologie at this point; that word has already appeared before the replaced noun on the previous baseline. H repeats/reorders the clause.','P14','high','text not on the page',False,True,False,True,9)
change('P15','L14, localisé and cancelled de',r"``localisé'' \deleted{\unsure{de}}",r'« localisé » \struck{\ill{}}',r"``localisé'' \deleted{\unsure{de}}",'Paired short quotation strokes flank localisé. A separate crossed cluster follows before the opening parenthesis; a d-like ascender and terminal e are possible but not wholly separable from the deletion. C’s doubtful de is retained, without claiming full recovery of the cancelled word.','P15','medium','readable ink left as \\ill{}',False,True,True,False,5)
change('P16','L14–15, au sens des ombres, ou',r'au sens des \unsure{ombres}, ou',r'en un sens \uncertain{à préciser} convenable','au sens des ombres, ou','The parenthesis starts au sens on the preceding baseline. Des ombres, ou is present on the next: ombres has an initial round o, low m, a tall looped b and re/s ending. The comma and short ou follow. H omits this entire first branch. Resolves C M0190.','P16','high','omission',True,True,True,True,3)
change('P17','L15, en un sens étale convenable','en un sens étale convenable',r'en un sens \uncertain{à préciser} convenable','en un sens étale convenable','After sens the short word has an accented e, a crossed t, a and a tall l followed by e. It is étale; there is no second word or the longer préciser sequence.','P17','high','misread word',False,True,True,True,2)
change('P18','L16, cancelled local object',r'$\deleted{\unsure{\hat X_J}}X_J$',r'\struck{$X$} $X_J$',r'$\deleted{\unsure{\hat X_J}}X_J$','The cancelled object has a crossing X and a lower hooked J before the following live X_J. The upper hat-like stroke is entangled with the cancellation, so the complete struck formula remains doubtful. H’s bare cancelled X omits the lower index.','P18','medium','misread symbol or index',False,True,False,True,1)
change('P19a','L17, inserted definition of U_J',r'\inserted{$=X_J\setminus D_J$,}',r'\add{$= X_J \setminus D_J$}',r'\inserted{$=X_J\setminus D_J$}','The inserted equality has both hooked J indices. The small descending stroke at its right belongs to the insertion leader; no independent comma remains after D_J. C’s comma is removed.','P19','high','text not on the page',True,False,False,False,9)
change('P19b','L17, trace de U_xi',r'$U_{\unsure{\xi}}$',r'$U$',r'$U_\xi$','A small sign sits below/right of U with three turning horizontal parts and a descending loop, the handwritten xi. It is separate from the neighboring letters, and is not blank as in H. Resolves C M0191.','P19','high','misread symbol or index',True,True,False,True,1)
change('P20','L19, cancelled p.r. à and live étalement',r'\deleted{p.r. à} étalement',r'par \uncertain{p.v.}\ algébrique',r'\deleted{p.r. à} étalement','The p descender, two stops, short r and grave-accented à lie beneath the cancellation. The following étalement is on the live baseline, with accented e, tall t/l and the ment ending. No live par or algébrique is written here.','P20','high','deletion state (struck given live or live given struck)',False,True,True,True,7)
change('P21','L19, on aura une suite exacte','on aura une suite exacte','on trouve une suite exacte','on aura une suite exacte','After on, the word has a round a, low u, short r and another a. There is no t ascender or v/e ending. The future aura is clear.','P21','high','misread word',False,True,False,True,2)
change('P22a','Equation (37), first term',r'\unsure{T^J|\bar T^J}',r'T^{J}',r'T^J','The capital has one roof stroke joined to the descending T stem; there is no separate second horizontal above it. The raised J is distinct. Resolves C M0192; the following arrow remains uncertain.','P22','high','misread symbol or index',True,False,False,True,1)
change('P22b','Equation (37), cancelled exponent above E_DJ',r'\mathcal E_{D_J}^{\deleted{\unsure{\tilde D_J}}}',r'\mathcal{E}_{D_J}',r'\mathcal E_{D_J}^{\deleted{\unsure{\tilde D_J}}}','Raised, struck ink is physically present above the final E term: a tilde-like top and hooked J can be distinguished, while the D body is retraced. The exponent is retained under deletion and doubt. H mentions it only in an editorial note instead of transcribing it at its source position.','P22','medium','omission',False,True,True,True,3)
change('P23a','L21, de façon précise','de façon précise','de façon plus précise','de façon précise','The baseline moves directly from façon to précise. The slanted crossing marks belong to the marginal annotation and do not supply independent p/l/u/s letters; H’s plus is absent.','P23','high','text not on the page',False,True,False,False,9)
change('P23b','L21, choisissant','choisissant','choisissons','choisissant','The ending after choisiss has an a-shaped junction, n minims, and a final rising t stroke, not the rounded on plus terminal s of choisissons.','P23','high','misread word',False,True,False,True,2)
change('P24','L22, on trouvera','on trouvera','on trouve','on trouvera','After trouve the connected r hook and final a oval are both written. H drops these final two letters and changes the future to present.','P24','high','misread word',False,True,False,True,2)
change('P25a','L22–23, insertion par image inverse',r'\inserted{(par image inverse)}',r"(par image inverse \add{d'ailleurs})",r'\inserted{par image inverse}','Par image inverse is raised above the line. The apparent opening stroke continues into one long curve under the phrase and returns on the right; it is the insertion leader, with no independent opening or closing parenthesis. D’ailleurs is written on the baseline below and is not part of this insertion. Both witnesses misread the leader as parentheses.','P25','medium','insertion or placement',True,True,False,True,6)
change('P25b','L23, d’où d’ailleurs',"d'où d'ailleurs",r"d'où \uncertain{aussi}","d'où d'ailleurs",'After d’où the baseline shows d, an apostrophe, a, two tall l strokes and the remaining eurs sequence. It is d’ailleurs, not aussi. The phrase is on the live baseline, separate from the raised insertion.','P25','high','misread word',False,True,True,True,2)
change('P27','L25, par tilde L_J',r'par $\tilde L_J$',r'$\widetilde{L}_J$',r'par $\tilde L_J$','The short word before the formula has a long descending p, joined a and terminal r hook. Par is live and separate from the tilde above L. H omits it.','P27','high','omission',False,True,False,False,3)
change('P28a','L25, whole formula containing the disputed separator',r'$\tilde X_J\unsure{\mathrel{\text{---}}|=|\ldots}\tilde U_J$',r'$\widetilde{X}_J - \widetilde{U}_J$',r'$\tilde X_J\unsure{\mathrel{\cdot-}}\tilde U_J$','Both neighboring objects have separate tildes and hooked J indices. Between them is a dark dot followed by one short horizontal stroke; a second parallel stroke needed for = is not secure. The literal dot–dash appearance is retained inside uncertainty, without deciding what relation was intended.','P28','medium','misread symbol or index',True,True,False,True,1)
change('P28b','L26, raised alg sép after ext.',r'\inserted{\unsure{alg. sép.|alg.}}',r'\add{algébr.}',r'\inserted{alg sép}','The raised word group has a, tall l and descending g, followed by s, accented e and descending p. The second group is present; no separate abbreviation stop is securely visible after either group. The small return at the end is part of the leader. Resolves M0195 as the written short forms alg sép, without supplying stops.','P28','medium','abbreviation expanded or spelling modernised',True,True,False,True,8)
change('P28c','L25–26, attachment of the short insertion and state of de L',r"le corps des fonctions de $\tilde X_J\unsure{\mathrel{\text{---}}|=|\ldots}\tilde U_J$, c'est une ext. \inserted{\unsure{alg. sép.|alg.}} de $L$, et",r"le corps des fonctions \add{algébr.}\ de $\widetilde{X}_J - \widetilde{U}_J$, c'est une ext.\ \add{de $L$}, et",r"le corps des fonctions de $\tilde X_J\unsure{\mathrel{\cdot-}}\tilde U_J$, c'est une ext. \inserted{alg sép} de $L$, et",'The raised alg sép sits over the final ext. clause and its leader attaches after ext.; it does not attach after fonctions on the previous baseline. De L is already written in the baseline continuation and is not an insertion. The doubtful relation is handled separately in P28a.','P28','high','insertion or placement',False,True,False,True,6)
change('P29','Upper left oblique margin note',r"\margin{il vaut mieux travailler avec les ``\unsure{tubulures} étales''\ldots}",r'\marginal{il \uncertain{est} \uncertain{plus} \uncertain{convenable} \uncertain{de prendre} les « \uncertain{tubulaires} » \ill{} \uncertain{ou} « \uncertain{formels} »…}',r"\margin{il vaut mieux travailler avec les ``\unsure{tubes|tubulures} étales''\ldots}",'The slanted note reads il vaut mieux travailler avec les: vaut has its final t; travailler has the repeated tall l strokes and er ending; avec is short and separately spaced. The quoted noun has t and b ascenders and a short terminal body, favoring tubes; no second l is distinguishable, but overlapping pale main text prevents full certainty. Étales has a visible accented e and tall t/l. The note ends with paired quotation strokes and three points. P33 is the additional tight crop of the unresolved noun.','P29','medium','misread word',True,True,True,True,2)
change('P30','Lower left oblique margin note',r"\margin{il faut choisir $\tilde D_J$ ``au dessus de $\bar K$''\ldots}",r'\marginal{\ill{} \uncertain{dessus} $\widetilde{D}_J$ \ill{} $U_J$ \ill{} \uncertain{revêtement universel} \ill{} $D_J$ \ill{}}',r"\margin{il faut choisir $\tilde D_J$ ``au dessus de $\bar K$''\ldots}",'Il faut choisir is written continuously on the oblique line, including the tall f/t and choisir sequence. The next object has a wave over D and a hooked J. The quoted phrase is au dessus de, followed by K with a separate horizontal bar; paired strokes close the quotation and three points follow. H’s fragmented margin does not preserve this readable sentence.','P30','high','readable ink left as \\ill{}',False,True,True,True,5)
change('P32','Small marginal annotation by the first term of (37)',r'\margin{plutôt $T^J$}', '',r'\margin{plutôt}','The oblique word has p, tall l, u, t, accented o and final t. Its neighboring T^J is the single T^J already on the horizontal equation baseline; after rotating the crop, the word becomes horizontal but that T remains tilted. There is no second handwritten T^J in the margin. The word is attached to that equation term without repeating it.','P32','high','text not on the page',True,True,False,True,9)
change('P34','NB margin, second U formula',r'$\unsure{U_{J\alpha}}$',r'$U_J$',r'$U_{J\alpha}$','In the second U formula, the two arms of U are separate from the hooked J and the small looped alpha to its right. These strokes can be followed despite the crossing main text. Resolves C M0200 at medium confidence; this does not settle the earlier, more crowded U subscript.','P34','medium','misread symbol or index',True,True,False,True,1)
change('P36','NB margin, tilde X formula',r'$\unsure{\tilde X_{J\alpha}}$', '',r'$\tilde X_{J\alpha}$','After d’où the formula has two crossing diagonals for X, a separate wavy tilde above, a hooked J below/right and a small looped alpha. The neighboring large tilted strokes belong to the main-text line, not this formula. Resolves C M0202 at medium confidence.','P36','medium','misread symbol or index',True,True,False,True,1)
change('P37','NB margin, heading and beginning',r'\uline{NB} Il faut partir de','',r'\uline{NB} Il faut partir de','The left edge carries distinct N and B with a short independent underline. Il, the tall f/t of faut, and partir follow on the same oblique baseline. H does not transcribe the heading or this opening. The further line continues through the crowded formula shown in P34.','P37','high','omission',False,True,False,True,3)
change('P31','NB margin, continuation omitted or fragmented in H',r"$\unsure{U_{J\bar K}}$, \unsure{si on veut}, d'un rev. universel $\unsure{\tilde V_0}$ de $\unsure{U_{J\alpha}}$ (qu'on va \unsure{multiplier} au dessus de $\bar K$ bien sûr), d'où $\unsure{\tilde X_{J\alpha}}$, $\unsure{\tilde D_{J\alpha}}$.",r'\marginal{\ill{} \uncertain{dessus} $\widetilde{D}_J$ \ill{} $U_J$ \ill{} \uncertain{revêtement universel} \ill{} $D_J$ \ill{}}',r"$\unsure{U_{J\bar K}}$, \unsure{si on veut}, d'un rev. universel $\unsure{\tilde V_0}$ de $U_{J\alpha}$ (qu'on va \unsure{multiplier} au dessus de $\bar K$ bien sûr), d'où $\tilde X_{J\alpha}$, $\unsure{\tilde D_{J\alpha}}$.",'The rotated marginal block has distinct short d’un, then rev. with a visible stop and the full universel; H’s revêtement is an expansion. Qu’on va, au dessus de and bien sûr remain legible on the lower oblique lines. The first U subscript, si on veut, the small V-like cover symbol, multiplier ending and final D index remain doubtful because separate main-text strokes cross them. P34–P37 isolate those clusters. The partial main text at the edge is excluded from the note.','P31','medium','omission',False,True,True,True,3)
change('P30n','Lower left handwritten foliation',r'\margin{132}','',r'\margin{132}','The small marginal number has a straight 1, a double-curved 3 and a hooked/diagonal 2. It is separate from the oblique mathematical notes and absent from H.','P30','high','omission',False,True,False,False,3)

# Every packet doubt, in packet order.
decision('M0183','alternative',r'\bar D_J','The complete inserted formula shows a distinct horizontal stroke above D; the lower hook is J, not an underline.','P01','high')
decision('M0184','first','soit','In the small raised word the initial s, closed o, i minim and final t upright are separately visible.','P01','high')
decision('M0185','first','composantes','The writing continues after comp through the ante/es sequence, including a tall t; it is not the abbreviation comp.','P03','high')
decision('M0186','first',"l'ombre",'The raised word has initial l and apostrophe, then o/m, tall b and re ending; its leader attaches before complété.','P06','high')
decision('M0187','first',r'\infty','Two joined loops form the infinity sign between sont and the hyphen. The surrounding D_J and non vides insertion were checked together.','P09','high')
decision('M0188','first','connexes','Initial c/o, joined n minims, crossing x and final es are visible after the infinity sign and hyphen.','P09','high')
decision('M0189','first','pas','The p descender, a oval and terminal s stand clearly above a separate underline.','P10','high')
decision('M0190','first','ombres','Initial o, low m, tall looped b and re/s ending are legible between des and the comma.','P16','high')
decision('M0191','first',r'\xi','The subscript has three short turning parts and a descending loop below U; it is distinct from the following sur.','P19','high')
decision('M0192','first',r'T^J','There is one roof stroke of T and its joined stem; no independent overbar. The raised J and entire sequence were checked.','P22','high')
decision('M0193','undecided',r'\unsure{\hookrightarrow|\to}','The left end has a descending/returning curve compatible with a hook, but a marginal stroke reaches the same place. The arrowhead and shaft are clear; the origin of the return is not separable.','P22','medium')
decision('M0194','undecided',r'\unsure{\mathrel{\cdot-}}','Between the complete tilded X_J and U_J is a dark dot followed by one short dash. A second parallel bar is not secure. The visible dot–dash is transcribed under doubt; no algebraic relation is inferred.','P28','medium')
decision('M0195','other','alg sép','The inserted a/l/g and s/é/p letter groups are distinct. No independent stop is securely separable after either group; the terminal return belongs to the leader. Retain both short forms without supplied stops.','P28','medium')
decision('M0196','undecided',r'\unsure{tubes|tubulures}','The noun has the ascenders of t and b and a short terminal body. A second l after b and a long ures sequence are not distinguishable. Tubes is favored, but pale crossing main text prevents full certainty.','P33','medium')
decision('M0197','undecided',r'\unsure{U_{J\bar K}}','The U body can be followed, but the descending stroke of the main-text façon runs through the low cluster; the subscript letters and proposed K bar cannot all be isolated.','P34','low')
decision('M0198','undecided',r'\unsure{si on veut}','The small connected cluster after the first marginal U is crossed by larger main-text strokes. Parts of the s/i, rounded on and veut-like ending are plausible, but not all letters are independent.','P34','low')
decision('M0199','undecided',r'\unsure{\tilde V_0}','A small rounded V/C-like body and a low oval compatible with 0 occur after universel. Nearby W-like strokes overlap its top; the base letter and tilde are not fully separable.','P35','low')
decision('M0200','first',r'U_{J\alpha}','The second U has two clear arms, a lower hooked J and a separate small looped alpha. These can be followed apart from the larger crossing strokes.','P34','medium')
decision('M0201','undecided',r'\unsure{multiplier}','The beginning shows low m/u and tall l/t-like strokes with a descending p cluster, but the compressed ending overlaps the next line and cannot be read letter by letter.','P36','low')
decision('M0202','first',r'\tilde X_{J\alpha}','After d’où, the two X diagonals, wavy tilde, hooked J and small looped alpha are separately identifiable; the larger tilted strokes below belong to the main text.','P36','medium')
decision('M0203','undecided',r'\unsure{\tilde D_{J\alpha}}','The final marginal object has a D-shaped body, upper wave and hooked J. The far-right alpha-like part is small and crowded, so the complete formula remains doubtful.','P36','low')

# Physical inventory, including all alterations and marginal writing.
inv('text','top centre, approximately [744,12,805,57]','66')
inv('text','main text L1–L13, upper half','telle que D_J ... le type d’homotopie de U_infty')
inv('insertion','top interline, P01','(i.e. bar D_J = intersection ... soit nonempty)')
inv('deletion','L2, below raised maquette, P02','solide [doubtful]')
inv('insertion','above L2, P02','maquette')
inv('deletion','L5 at right, P05','U_infty [doubtful]')
inv('insertion','above complété in L6, P06',"l'ombre")
inv('insertion','above L9 between D_J and sont, P09','non vides')
inv('deletion','L12, under second maquette, P13','solide [doubtful]')
inv('insertion','above L12, P13','maquette')
inv('text','main text L14–L19','Considérons maintenant le localisé ... une suite exacte')
inv('deletion','L14, after localisé, P15','de [doubtful]')
inv('deletion','L16, after soit and before X_J, P18','hat X_J [doubtful]')
inv('insertion','above L17, after U_J, P19','=X_J minus D_J')
inv('deletion','start of L19, P20','p.r. à')
inv('display','L20, equation (37), P22','T^J to E_UJ^(bar L) to E_DJ to 1')
inv('deletion','raised above last E term of (37), P22','tilde D_J [doubtful]')
inv('text','main text L21–L26, lower half','de façon précise, choisissant ... de L, et')
inv('insertion','above L23, P25','par image inverse')
inv('deletion','L24, after map to U and semicolon, P26','et on [doubtful]')
inv('insertion','above final line after ext., P28','alg sép')
inv('margin note','upper left, oblique, P29/P33','il vaut mieux travailler avec les tubes/tubulures étales...')
inv('margin note','beside first term of (37), P32','plutôt')
inv('margin note','lower left, oblique, P30','il faut choisir tilde D_J au dessus de bar K...')
inv('margin note','lower left to bottom centre, oblique and crossing main text, P31/P34–P37','NB Il faut partir de ...')
inv('margin note','far left near lower oblique notes, P30','132')

# Audit targets. Crop boxes include neighboring ink as context; the readings name
# the target baseline, insertion or marginal block rather than duplicating that context.
audit('handwritten number',[744,12,805,57],r'\mspage{66}')
audit('C/H different words; doubtful formula',[640,58,925,143],r'$D_J\ne\phi$,')
audit('insertion; doubtful formula; C/H different words',boxes['P01'],r'\inserted{(i.e. $\bar D_J=\bigcap_{j\in J}D_j$ soit $\ne\phi$)}')
audit('C/H different words',[1000,80,1635,143],r'on trouve sur $I$ une')
audit('insertion; struck passage; C/H different words; less than high confidence departure',boxes['P02'],r'\deleted{\unsure{solide}} \inserted{maquette} simpliciale')
audit('C/H different words',boxes['P03'],'composantes')
audit('C/H different words; less than high confidence departure',[285,301,1370,402],'connexes correspondent comp. connexes')
audit('C/H different words; struck passage; doubtful formula',boxes['P05'],r'ou encore : celles de $\deleted{\unsure{U_\infty}}$')
audit('insertion; C/H different words',boxes['P06'],r"le \inserted{l'ombre} complété")
audit('C/H different words',boxes['P07'],'a un caractère invariant p.r.')
audit('C/H different words; less than high confidence departure',boxes['P08'],r"``\unsure{compactification|complétification}''")
audit('insertion; doubtful formula',boxes['P09'],r'$D_J$ \inserted{non vides} sont $\infty$-connexes')
audit('C/H different words',boxes['P10'],r'\uline{pas} le cas, sauf pour $D_J$')
audit('C/H different words',boxes['P12'],'la topologie de notre')
audit('insertion; struck passage; C/H different words; less than high confidence departure',boxes['P13'],r'\deleted{\unsure{solide}} \inserted{maquette} simpliciale exprime')
audit('C/H different words',boxes['P14'],r"le type d'homotopie de $U_\infty$.")
audit('struck passage; C/H different words; less than high confidence departure',boxes['P15'],r"``localisé'' \deleted{\unsure{de}} (au sens")
audit('C/H different words',boxes['P16'],'des ombres, ou')
audit('C/H different words',boxes['P17'],'en un sens étale convenable)')
audit('struck passage; doubtful formula; C/H different words',boxes['P18'],r'soit $\deleted{\unsure{\hat X_J}}X_J$')
audit('insertion; doubtful formula; C/H different words',boxes['P19'],r'$U_J$ \inserted{$=X_J\setminus D_J$} la trace de $U_\xi$')
audit('struck passage; C/H different words',boxes['P20'],r'\deleted{p.r. à} étalement),')
audit('C/H different words',boxes['P21'],'on aura une suite exacte')
audit('doubtful formula; struck passage; handwritten number',boxes['P22'],r'\tag{37} T^J\unsure{\hookrightarrow|\to}\mathcal E_{U_J}^{\bar L}\longrightarrow\mathcal E_{D_J}^{\deleted{\unsure{\tilde D_J}}}\longrightarrow1')
audit('C/H different words',boxes['P23'],'de façon précise, choisissant un rev. universel')
audit('C/H different words',boxes['P24'],'on trouvera un rev. universel')
audit('insertion; C/H different words; less than high confidence departure',boxes['P25'],r"\inserted{par image inverse} d'où d'ailleurs")
audit('struck passage; C/H different words',boxes['P26'],r'\deleted{\unsure{et on}} on désigne')
audit('C/H different words',boxes['P27'],r'par $\tilde L_J$')
audit('insertion; doubtful formula; C/H different words; less than high confidence departure',boxes['P28'],r"$\tilde X_J\unsure{\mathrel{\cdot-}}\tilde U_J$, c'est une ext. \inserted{alg sép} de $L$, et")
audit('margin note; C/H different words; less than high confidence departure',boxes['P29'],r"il vaut mieux travailler avec les ``\unsure{tubes|tubulures} étales''\ldots")
audit('margin note; C/H different words',boxes['P30'],r"il faut choisir $\tilde D_J$ ``au dessus de $\bar K$''\ldots")
audit('margin note; C/H different words',boxes['P32'],'plutôt')
audit('margin note; doubtful formula; handwritten number; C/H different words; less than high confidence departure',[18,1823,792,2345],r"\uline{NB} Il faut partir de $\unsure{U_{J\bar K}}$, \unsure{si on veut}, d'un rev. universel $\unsure{\tilde V_0}$ de $U_{J\alpha}$ (qu'on va \unsure{multiplier} au dessus de $\bar K$ bien sûr), d'où $\tilde X_{J\alpha}$, $\unsure{\tilde D_{J\alpha}}$.")
audit('handwritten number; margin note',[20,2020,90,2068],'132')

# Residual doubts include unregistered uncertainties inside deletions.
doubt('L2, first cancelled noun',r'\deleted{\unsure{solide}}','H: schéma','low','The cancellation overlays the inner letter sequence. Maquette is clear above it; the cancelled noun is not resolved from the replacement.')
doubt('L5, cancelled object before hat X',r'\deleted{\unsure{U_\infty}}','Base letter uncertain under the strike','medium','The paired subscript loops are clearer than the upper body. The deletion crosses that body, so the whole object remains marked.')
doubt('L8, quoted noun',r'\unsure{compactification|complétification}','compactification / complétification','medium','After comp the compressed tall cluster before f does not give independently separable act or lét. Quotation marks are clear.')
doubt('L12, second cancelled noun',r'\deleted{\unsure{solide}}','H: schéma','low','The separate letters under the dark deletion cannot all be isolated, despite the suggestive outline.')
doubt('L14, cancelled word after localisé',r'\deleted{\unsure{de}}','H leaves it illegible','low','An ascender and a terminal loop suggest de, but cancellation overlaps both. No certainty resolution is made.')
doubt('L16, cancelled local object',r'\deleted{\unsure{\hat X_J}}','X_J with an uncertain upper accent','medium','X and the lower J can be traced; the proposed hat overlaps cancellation strokes.')
doubt('Equation (37), first arrow',r'\unsure{\hookrightarrow|\to}',r'\hookrightarrow / \to','medium','The left return is compatible with a hook but may include the stroke of the nearby marginal annotation.')
doubt('Equation (37), cancelled exponent',r'\deleted{\unsure{\tilde D_J}}','Exact base letter under the strike','medium','The upper wave and lower hook survive, while the D body is retraced and not letter-perfect.')
doubt('L24, cancelled words before on désigne',r'\deleted{\unsure{et on}}','et on / et une / et un','low','Et is visible, but the following low letters merge with the strike; the vowels and final strokes are not individually recoverable.')
doubt('L25, separator between tilded spaces',r'\unsure{\mathrel{\cdot-}}','A dot plus dash is visible; = or a simple separator may have been intended','medium','The source has one dark point and one short horizontal stroke, without two clear parallel bars. The transcription records appearance without imposing an intended relation.')
doubt('Upper oblique note, quoted noun',r'\unsure{tubes|tubulures}','tubes / tubulures; H tubulaires is not supported by a full letter sequence','medium','The shorter body and lack of a second l favor tubes; crossing pale main-text strokes still make the terminal letters less than certain.')
doubt('NB, first U formula',r'\unsure{U_{J\bar K}}','Subscript letters and bar unresolved','low','A long descender from the main text crosses the subscript and obscures the supposed K/bar combination.')
doubt('NB, phrase after first U',r'\unsure{si on veut}','No secure alternative','low','The small phrase lies under larger oblique crossings; individual letters cannot all be detached from neighboring writing.')
doubt('NB, proposed universal-cover symbol',r'\unsure{\tilde V_0}',r'V/C/W-like base form with low oval; tilde uncertain','low','The body is rounded and crowded. The small oval is compatible with 0, but the upper wave and base letter cannot be separated cleanly.')
doubt('NB, multiplier',r'\unsure{multiplier}','No secure alternative; ending remains compressed','low','Initial minims and tall l/t-like strokes are visible, but the ending merges into adjacent writing and cannot be resolved letter by letter.')
doubt('NB, final D formula',r'\unsure{\tilde D_{J\alpha}}','Exact final subscript uncertain','low','D, an upper wave and J are plausible; the far-right alpha-like stroke is too crowded for a full certainty resolution.')

r['notes']=[
 {'id':'N01','text':'The page continues a discussion of the simplicial maquette associated with nonempty intersections D_J. The author asks “quelle est sa signification topologique?” and connects components with D=X\\setminus U and the completed neighborhood minus D. He then considers the hypothetical infinity-connectedness of the nonempty D_J, explicitly says that this is not the case except for a stratum reduced to a point, and asks whether the maquette could express the homotopy type of U_infty. This is a report of his question and hypothetical argument, not a theorem verification.'},
 {'id':'N02','text':'Two source constructions remain grammatically awkward: “connexes correspondent comp. connexes” has no independent aux in the ink, and the later phrase retains “le l’ombre complété”. The long q descender above the first gap is not an aux. Neither expression has been silently repaired. The middle of the quoted compactification/complétification word remains unresolved.'},
 {'id':'N03','text':'The second paragraph introduces a localization of X along D_J and the trace U_J. Equation (37) is presented as an exact sequence with first term T^J, an E object over U_J with barred L, an E object over D_J carrying a cancelled exponent, and terminal 1. The first arrow may have a hook, but the marginal stroke prevents certainty. The small marginal word “plutôt” points to this single T^J; C duplicates that target in its separate margin transcription.'},
 {'id':'N04','text':'The continuation chooses a universal cover of D_J and speaks of a universal cover of X_J by inverse image, then defines the function field tilde L_J. “Par image inverse” is raised and carried by one continuous curved leader; neither of the parentheses supplied by both witnesses is independent ink. The relation between tilde X_J and tilde U_J is visibly dot–dash-like and remains uncertain. Alg sép is inserted after ext.; no separate stops are secure.'},
 {'id':'N05','text':'The upper oblique note recommends working with the quoted “tubes” or “tubulures” étales; the short noun is not settled. The lower note says to choose tilde D_J “au dessus de bar K”. The dense NB starts “Il faut partir de” and contains a universal-cover construction; its first U subscript, phrase si on veut, cover symbol, multiplier ending and final D formula remain uncertain. Larger main-text strokes crossing these lines have not been incorporated as extra marginal words.'},
 {'id':'N06','text':'The handwritten page number is 66, the sequence number is (37), the sequence ends in the digit 1, the doubtful NB cover symbol includes a low oval read as 0, and the separate lower marginal foliation is 132. All are included in audit boxes. The scan identifier 133 and H’s editorial page/margin notes are not additional handwritten source text.'},
 {'id':'N07','text':'The page was read visually from the complete image and the two supplied native halves, then from saved crops of word disagreements, resolved doubts, cancellations and crowded formulas. There are 26 main baselines including the displayed sequence, excluding interlinear insertions and oblique margins. No OCR, external research, TeX compilation, proof check or computation was performed; check_events is therefore empty.'}
]
r['notation']=[
 {'form':r'\phi','meaning':"ϕ : l'ensemble vide",'evidence':'L1 and top insertion: each sign has a loop traversed by a long descending stem; the surrounding inequalities express non-emptiness.'},
 {'form':r'\bar D_J=\bigcap_{j\in J}D_j','meaning':'The intersection notation explicitly given in the top insertion; the D bears an upper horizontal bar.','evidence':'P01, complete inserted parenthesis.'},
 {'form':r'\hat X','meaning':'The object called the complété of X along D, with an inserted l’ombre.','evidence':'L6 and P06; the source description is preserved despite its grammar.'},
 {'form':r'X_J,\ U_J=X_J\setminus D_J','meaning':'The localized object and the inserted expression for its open part.','evidence':'L16–L17 and P18–P19.'},
 {'form':r'T^J','meaning':'The first term of sequence (37), annotated by the marginal plutôt.','evidence':'P22 and P32 show one written T^J, without an independent bar or duplicate marginal term.'},
 {'form':r'\mathcal E_{U_J}^{\bar L},\ \mathcal E_{D_J}','meaning':'The E objects appearing in the exact sequence; the final object also has a cancelled doubtful exponent.','evidence':'Equation (37), P22; no definition beyond the source’s local description is inferred.'},
 {'form':r'\tilde D_J,\ \tilde X_J,\ \tilde U_J,\ \tilde L_J','meaning':'Universal-cover and associated open/function-field notation in the continuation.','evidence':'L21–L26; tilde L_J is introduced by “le corps des fonctions”.'},
 {'form':r'\bar K','meaning':'The barred K occurring in the quoted “au dessus” marginal requirement and NB.','evidence':'P30 and the lower NB; a separate horizontal bar is visible over K.'}
]
r['abbreviations']=[
 {'form':'i.e.','expansion':'id est'},
 {'form':'comp.','expansion':'composantes'},
 {'form':'p.r.','expansion':'par rapport'},
 {'form':'rev.','expansion':'revêtement'},
 {'form':'ext.','expansion':'extension'},
 {'form':'alg','expansion':'algébrique'},
 {'form':'sép','expansion':'séparable'},
 {'form':'NB','expansion':'nota bene'}
]
r['hand']=[
 {'habit':'Very long q descenders can run into the next baseline and end in a loop resembling a short word.','places':'149_scan133 L3–L4, P04','consistency':'Direct continuity from the q in topologique to the low loop is visible at this occurrence.','witness_errors':'C gives aux as live text; H correctly labels aux as an editorial supply.'},
 {'habit':'The empty-set sign is a phi-like loop with a long traversing stem.','places':'149_scan133 L1 and top insertion, P00–P01','consistency':'The two occurrences on this page have the same loop/stem construction.','witness_errors':'C normalizes to varnothing and H to emptyset.'},
 {'habit':'J indices have a broad lower hook; a hook below D can resemble an underline if read without the complete formula.','places':'149_scan133 top insertion, local objects, sequence and NB','consistency':'The lower hooked shape recurs in the clear J indices; crowded NB indices remain locally uncertain.','witness_errors':'C considers an underlined D in M0183; H drops the J from one cancelled object.'},
 {'habit':'Curved insertion leaders may imitate commas or paired parentheses.','places':'149_scan133 U_J insertion P19 and par image inverse P25','consistency':'At both places the apparent punctuation can be traced continuously into the attachment stroke.','witness_errors':'C supplies a comma after the U_J definition; both witnesses surround par image inverse with parentheses.'},
 {'habit':'Tall repeated t/l strokes and q descenders distinguish maquette from more familiar replacement nouns.','places':'149_scan133 two maquette insertions, P02 and P13','consistency':'Both occurrences have the q descender and paired tall t cluster.','witness_errors':'H reads ensemble and changes simpliciale to simplicial.'},
 {'habit':'Small trailing connected ra can be missed at a word end.','places':'149_scan133 on trouvera, P24','consistency':'The r hook and final a oval are distinct at this occurrence; no broader claim is made.','witness_errors':'H reads trouve.'},
 {'habit':'Oblique marginal formulas overlap larger horizontal main-text writing, which tilts differently when the note is rotated.','places':'149_scan133 P31–P37','consistency':'Separating the two baseline directions distinguishes the note’s plutôt from the main-equation T^J and prevents main-text descenders from becoming marginal indices.','witness_errors':'C duplicates T^J in the margin; both witnesses leave or misread crowded NB symbols.'},
 {'habit':'Paired short straight strokes serve as double quotation marks.','places':'149_scan133 quoted compactification/complétification, localisé, and oblique notes','consistency':'The inspected pairs are straight quotation strokes, not drawn guillemets.','witness_errors':'H substitutes French guillemets.'}
]
coverage={
1:'Editorial scan/page wrapper difference only; scanpage 133 is the archive marker.',
2:'H editorial words de l’auteur are not source text; handwritten 66 retained and audited.',
3:'P00a: distinct comma after the first phi-shaped empty-set sign retained.',
4:'P01/M0183: upper bar on D resolved; written phi and complete inserted formula retained.',
5:'P01: no independent comma after the closing inserted parenthesis.',
6:'P00b: no independent comma after trouve.',
7:'P02: maquette and feminine simpliciale; cancelled solide remains doubtful.',
8:'P03/M0185: full composantes resolved, not comp.',
9:'P05a: ou encore, not on connaît.',
10:'P05a: celles de; no independent du bout.',
11:'P05b: cancelled U_infty candidate retained under uncertainty.',
12:'P06/M0186: inserted l’ombre resolved; preceding le remains.',
13:'Same visible dash; TeX triple hyphen versus Unicode em dash is not a source difference.',
14:'P07: a un caractère invariant p.r. is legible.',
15:'P08: straight quotation strokes retained; compactification/complétification remains uncertain.',
16:'P10b: sauf pour D_J, not si J.',
17:'P12–P14: source order la topologie de notre ... simpliciale exprime le type retained; H reorders it.',
18:'P12–P14: de notre and the replaced noun belong after topologie; no second topologie before type.',
19:'P15: straight quotes and a cancelled doubtful de; H’s illegibility is retained only as residual uncertainty.',
20:'P15–P16/M0190: au sens des ombres, ou is present before the second branch.',
21:'P17: en un sens étale convenable.',
22:'P18: cancelled formula includes lower J; proposed hat remains uncertain.',
23:'P19a: C comma after inserted D_J removed because stroke is the leader; H agrees.',
24:'P19b/M0191: xi subscript is written and resolved.',
25:'P20: no live par; p.r. à is struck.',
26:'P20: r form with stop, not v; deletion retained.',
27:'P20: struck à followed by live étalement, not algébrique.',
28:'P21: on aura, not on trouve.',
29:'Formula-number wrapper only: handwritten (37) retained through tag{37}.',
30:'Formula-number wrapper only: handwritten closing parenthesis belongs to (37), not extra source text.',
31:'P22a/M0192 resolves T^J without bar; M0193 preserves hook/ordinary-arrow uncertainty.',
32:'P22b: raised cancelled exponent retained at E_DJ under doubt; H describes it only editorially.',
33:'Same source dash; macro/punctuation encoding difference only.',
34:'P23a: no independent plus after façon.',
35:'P23b: choisissant, not choisissons.',
36:'P24: future trouvera retains final ra.',
37:'P25a: par image inverse alone is inserted, with a leader rather than parentheses; d’ailleurs is not part of it.',
38:'P25b: live baseline d’où d’ailleurs, not aussi.',
39:'P26 residual doubt: et on is retained as a candidate; et une/et un cannot be excluded under the strike. No false certainty resolution.',
40:'P27: live par before tilde L_J is present.',
41:'P28b–c: short alg sép is attached after ext.; no added algébr. after fonctions.',
42:'P28a/M0194: literal dot followed by short dash retained under uncertainty; no forced equals sign.',
43:'P28b–c/M0195: both alg and sép groups present, no secure independent stops; de L is live baseline text.',
44:'P29: il vaut mieux travailler avec les, clear despite H’s alternative phrases.',
45:'P29–P30/M0196: tubes favored with tubulures alternative; étales clear; separate il faut choisir note retained.',
46:'P30/P32/P37: au dessus de bar K, marginal plutôt without duplicated T^J, and underlined NB opening all retained.',
47:'P31 and M0197–M0198: first U subscript and si on veut remain doubtful; d’un rev. is written short and not expanded.',
48:'P31/P34/P36 and M0199–M0202: full NB continuation retained; U_Jalpha and tilde X_Jalpha resolved at medium confidence, other named doubts retained.',
49:'P31/M0203: final marginal D formula remains doubtful; H’s general editorial note is excluded from source text.',
50:'P30n: handwritten 132 retained; H’s editorial statement about a cancelled exponent is not transcribed as another margin note.'
}
r['diff_coverage']=[{'row':i,'disposition':coverage[i]} for i in range(1,51)]
r['deletion_insertion_review']=[
 {'text':r'\inserted{(i.e. $\bar D_J=\bigcap_{j\in J}D_j$ soit $\ne\phi$)}','scope_attachment':'Raised full parenthesis attached after the initial non-emptiness condition; no new comma at its end.','evidence':'P01 shows the complete inserted line and both delimiters.'},
 {'text':r'\deleted{\unsure{solide}} \inserted{maquette}','scope_attachment':'First struck noun only; raised maquette replaces that noun before live simpliciale.','evidence':'P02: dark cancellation stays on the baseline noun; the raised replacement is separate and not struck.'},
 {'text':r'\deleted{\unsure{U_\infty}}','scope_attachment':'Only the cluster after celles de is cancelled; the following hat X minus D remains live.','evidence':'P05 shows the crossing strokes confined to the preceding U/infinity candidate.'},
 {'text':r"\inserted{l'ombre}",'scope_attachment':'Inserted before complété, after the existing live le.','evidence':'P06: the raised l’ombre and leader point to this gap, without cancelling le.'},
 {'text':r'\inserted{non vides}','scope_attachment':'Qualifies D_J between the baseline D_J and sont.','evidence':'P09: two raised words and attachment at that gap.'},
 {'text':r'\deleted{\unsure{solide}} \inserted{maquette}','scope_attachment':'Second occurrence: the baseline noun after de notre is cancelled and maquette replaces it; simpliciale exprime remains live.','evidence':'P13 shows the upper q/t cluster independently of the crossed lower word.'},
 {'text':r'\deleted{\unsure{de}}','scope_attachment':'Cancelled short word after the closing quotes of localisé and before the parenthesis.','evidence':'P15: a compact crossed cluster is distinct from the opening parenthesis.'},
 {'text':r'\deleted{\unsure{\hat X_J}}','scope_attachment':'Cancelled proposed object after soit, before live X_J.','evidence':'P18: the lower J belongs to the crossed cluster; the second X_J is unstruck.'},
 {'text':r'\inserted{$=X_J\setminus D_J$}','scope_attachment':'Defines the immediately preceding U_J; no independent comma after the insertion.','evidence':'P19: the apparent comma continues into the leader, while both J indices remain part of the formula.'},
 {'text':r'\deleted{p.r. à}','scope_attachment':'All three abbreviated/short parts are struck; following étalement remains live.','evidence':'P20: cancellation crosses p.r. à and ends before the accented e of étalement.'},
 {'text':r'\deleted{\unsure{\tilde D_J}}','scope_attachment':'Cancelled exponent of the E_DJ term in (37), not an independent marginal line.','evidence':'P22: small raised cluster above the final E term; body retraced, so uncertainty is preserved.'},
 {'text':r'\inserted{par image inverse}','scope_attachment':'Raised qualification of the universal-cover construction before tilde X_J; continuous leader is not parentheses.','evidence':'P25: one curved stroke runs from the left of par beneath the inserted words and returns on the right. Baseline d’ailleurs is outside it.'},
 {'text':r'\deleted{\unsure{et on}}','scope_attachment':'Cancelled short phrase after the semicolon; following on désigne is live.','evidence':'P26: the heavy strike covers et and following low letters, but stops before the separate live on.'},
 {'text':r'\inserted{alg sép}','scope_attachment':'Raised qualification of ext. on the final line, before live de L.','evidence':'P28: leader attaches to the final clause, not to fonctions on the previous line; no independent stops are secure.'}
]

# Structural validation only: no OCR or TeX compilation.
assert len(r['decisions'])==21
assert [d['id'] for d in r['decisions']]==[f'M{i:04d}' for i in range(183,204)]
assert [d['row'] for d in r['diff_coverage']]==list(range(1,51))
assert len({d['id'] for d in r['changes']})==len(r['changes'])
required=('page reader line_count changes decisions inventory audit_boxes doubts notes check_events notation abbreviations hand diff_coverage deletion_insertion_review').split()
assert set(required)==set(r)
for item in r['changes']+r['decisions']:
    assert (root/'work'/item['crop']).is_file(), item['crop']
    b=item['box']; assert 0<=b[0]<b[2]<=1680 and 0<=b[1]<b[3]<=2359
for item in r['audit_boxes']:
    b=item['xyxy']; assert 0<=b[0]<b[2]<=1680 and 0<=b[1]<b[3]<=2359
normalize=lambda s:re.sub(r'\s+',' ',s).strip()
source_issues=[]
for item in r['changes']:
    for key,source in [('c',c),('h',h)]:
        if item[key] and normalize(item[key]) not in normalize(source):
            source_issues.append((item['id'],key,item[key]))
assert not source_issues, source_issues
# Every resolved mark must have exactly the retained reading present in the draft.
for item in r['decisions']:
    assert item['reading'] in draft, (item['id'],item['reading'])
assert '\\margin{plutôt $T^J$}' not in draft
assert '\\inserted{(par image inverse)}' not in draft
assert 'correspondent aux' not in draft
assert '\\inserted{alg sép}' in draft
assert draft.count('{')==draft.count('}')
(out/'draft.tex').write_text(draft)
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':r['page'],'changes':len(r['changes']),'marks':len(r['decisions']),'audit_boxes':len(r['audit_boxes']),'inventory':len(r['inventory']),'doubts':len(r['doubts']),'crops':len(boxes),'resolved_marks':sum(d['decision']!='undecided' for d in r['decisions']),'unresolved_marks':sum(d['decision']=='undecided' for d in r['decisions']),'source_strings_validated':True},ensure_ascii=False))
