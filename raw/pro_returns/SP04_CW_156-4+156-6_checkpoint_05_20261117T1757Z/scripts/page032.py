from author import Page
p=Page('156-4',32)
p.replace(r'\unsure{tt|tte}','tt')
p.replace(r'\unsure{U}','U')
p.replace(r'\unsure{Juin|juin}','Juin')
p.replace('pseudodisques','pseudo-disques')
p.replace(r'accompagnées\unsure{.}', 'accompagnées.')
p.replace(r'\unsure{équivalence|équidistance}','équivalence')
p.replace(r'$L$',r'$\mathcal L$')
def c(loc,C,H,F,ev,cr,dc=False,dh=True,kind='other',conf='high',mark='no',con=''):
 p.change(loc,C,H,F,ev,cr,dc,dh,kind,conf,mark,con)
c('condition designation',"Cont′₄",'emphasized Cont′₄',"Cont′₄",'No underline accompanies this occurrence; prime is raised and 4 low.','condition',kind='other')
c('first pair of figures','F,[G|C]','F,G','F,[G|C]','Second letter has an open curved bowl and downward hooked terminal; the hook supports G but C remains possible.','condition',kind='misread symbol or index',conf='medium')
c('logical abbreviation','sss','ssi','sss','Three small s-strokes: initial short rising/downward segment, central loop with lower curve, separate final loop and lower curve; no i dot.','sss',kind='abbreviation expanded or spelling modernised')
c('quantifier abbreviation','[tt|tte]','U','tt','Two adjacent t uprights share a crossbar; no final e follows.','condition',True,kind='misread word',conf='medium')
c('overwritten stratum letter','deleted [A|X], [U?]','U preceding strate','deleted [A|X], U after strate ouverte','The live U has two upright strokes and curved foot at the next line opening; its inner dark prior diagonals allow A/X.','condition',True,kind='insertion or placement',conf='medium')
c('cancelled residue after V','a, subscript or baseline','omitted','[subscript a|baseline a]','A compact dark a-like loop remains low and right of V under the strike; exact attachment remains uncertain.','condition',kind='omission',conf='low')
c('date','12. [Juin|juin]','12 juin (note 12. Juin)','12. Juin','Initial month letter is a full-height long J descending below the underline; dot follows 12; one stroke underlines date and month.','date',True,kind='other',conf='medium')
c('reflection subject','combinatoire','construction','combinatoire','Initial com, looped b, i dot, n-a-t and final oire remain distinct across the word.','date',kind='misread word',con='The passage concerns the combinatoire of pseudo-discs.')
c('first compound','pseudodisques','pseudo-disques','pseudo-disques','Separate horizontal connecting dash lies between pseudo and disques, as in the next occurrence.','disc',True,False)
c('cancelled symbol before pair','[L|X|D]',r'\ill{}','[L|X|D]','Several diagonal crossing strokes obscure the original tall letter, with curved lower exit; no secure resolution.','disc',kind=r'readable ink left as \ill{}',conf='low',mark='yes')
c('parenthetical qualification','([en|au] un sens convenable)',r'(ou \ill{})','([en|au] un sens convenable)','un, sens and convenable are legible; first low joined group supports en/au without resolving their shared curves.','disc',kind=r'readable ink left as \ill{}',conf='medium',mark='yes')
c('consequence opening','alors les','les','alors les','The line begins a-l-o-r-s, then a separate les before quoted lieux.','disc',kind='omission')
c('live negation','ne sont underlined pas seulement',r'ne [sont?] deleted \ill{} \ill{} seulement','ne sont underlined pas seulement','ne at end of upper line, sont at next line left; compressed pas is live with a lower underline, not a cancellation through its body.','parts',kind='deletion state (struck given live or live given struck)',conf='medium',mark='yes',con='The negated assertion retains live pas: the lieux require additional data.')
c('adjective on parts','contractibles','contractiles','contractibles','Small rounded b followed by tall l appears after the i; the manuscript includes the b.','parts',kind='misread word')
c('abbreviation etc','etc','etc.','etc','No point follows the c before the closing parenthesis.','parts',kind='abbreviation expanded or spelling modernised')
c('point after accompagnées','[.?]','omitted','.','A detached round dot lies on the baseline after the final s and before d’une.','parts',True,kind='omission',conf='medium')
c('additional datum phrase',"une [classe|donnée] d’équivalence de ``[cordes|corde]'' les joignant à ∂D",r'\ill{} \ill{} \ill{} la frontière \ill{} ∂D',"une [classe|donnée] d’équivalence de ``[cordes|corde]'' les joignant à ∂D",'une followed by compressed looped word; next line clearly d’équivalence, de, quoted cordes/corde, les and joignant, then à ∂D. No word frontière lies between them.','cords',True,kind=r'readable ink left as \ill{}',conf='medium',mark='yes',con='Restores the written equivalence-class/cord data associated with the lieux, with remaining lexical doubts marked.')
c('compressed noun','[classe|donnée]','unread','[classe|donnée]','Initial joined loop and ascender can encode cl or d; following shallow undulations do not fully settle the word.','classe',kind=r'readable ink left as \ill{}',conf='low',mark='yes')
c('equivalence word','[équivalence|équidistance]','unread','équivalence','After équi comes a low v, a and tall l, followed by ence; no d-stem or st pair.','cords',True,kind=r'readable ink left as \ill{}',mark='yes')
c('quoted cord word','[cordes|corde]','unread','[cordes|corde]','c-o-r-d-e are visible; final low extension may include s but is compressed into the exit stroke.','cords',kind=r'readable ink left as \ill{}',conf='medium',mark='yes')
c('Du coup consequence','cela montre',r'\ill{}','cela montre','c-e-l-a followed by m, dotted continuation and t stem are visible before que.','cords',kind=r'readable ink left as \ill{}',mark='yes')
c('cancelled que','deleted [que?]',r'deleted \ill{}','deleted [que?]','A q-like descender survives below a dense horizontal cancellation, with little surviving upper body.','bottom',kind=r'readable ink left as \ill{}',conf='low',mark='yes')
c('intended interpretation','en vue',r'\ill{}','en vue','en closes one line and vue begins the next before comma.','bottom',kind=r'readable ink left as \ill{}',mark='yes')
c('description of structure','en termes [dé|de] donnée','sur unread donnée','en termes [dé|de] donnée','en is at the previous line end; next line begins termes, then short de-like group carrying a small mark above e.','bottom',kind='misread word',conf='medium',mark='yes')
c('set abbreviation','ens','ens.','ens','No terminal dot appears between ens and L.','bottom',kind='abbreviation expanded or spelling modernised')
c('page ending',"n’est pas",r'ne \ill{} pas',"n’est pas",'Final line shows n, apostrophe, e-s-t with high t, then pas.','bottom',kind=r'readable ink left as \ill{}',mark='yes')
c('locus letter','L','L',r'\mathcal L','Slanting long stem and low curved foot correspond to the recurring locus letter; witnesses refer to the same sign.','bottom',True,False)
for loc,rd,why,cr,cf in [
 ('first figure pair','G|C','Hooked exit allows G but inner bar is not separately drawn.','condition','medium'),
 ('overwritten stratum','A|X','Dark diagonals underneath live U.','condition','low'),
 ('cancelled a after V',r'_{a}|a','Position is low but cancellation prevents clear attachment.','condition','low'),
 ('cancelled symbol before (D,∂D)','L|X|D','Dense cross-strokes preserve no unique outline.','disc','low'),
 ('parenthetic first word','en|au','Low joined loops permit both readings.','disc','medium'),
 ('additional datum noun','classe|donnée','Compressed joined loops.','classe','low'),
 ('quoted word','cordes|corde','Possible final s shares the exit stroke.','cords','medium'),
 ('cancelled connective','que','Only descender and narrow body remain.','bottom','low'),
 ('en termes de','dé|de','Detached mark above e may be an accent or pen lift.','bottom','medium')]:p.doubt(loc,rd,why,cr,cf)
p.inventory([('text','top','Ainsi Cont′₄ dit que'),('deletion','stratum symbol','A/X under U'),('deletion','top condition','telles que U≠V a, on ait'),('text','date','12. Juin'),('text','main dated paragraph','Depuis hier j’ai pas mal réfléchi'),('deletion','before disc pair','L/X/D'),('text','disc qualification','(D,∂D) est un tel pseudo-disque'),('text','loci and parts','alors les lieux sur D-∂D'),('text','additional datum','mais elles doivent être accompagnées.'),('text','equivalence and cords','une classe/donnée d’équivalence'),('text','interpretation','Du coup, cela montre'),('deletion','after interprétation','que'),('text','final continuation','que j’avais en vue')])
p.notation('logical abbreviation','sss','Three small s strokes, first two joined; no i dot.')
p.r['abbreviations']=[dict(abbreviation='sss',expansion='si et seulement si',evidence='opening criterion'),dict(abbreviation='tt',expansion='toute/tout',evidence='before strate ouverte'),dict(abbreviation='ens',expansion='ensemble',evidence='last lines'),dict(abbreviation='etc',expansion='et cetera',evidence='parts parenthesis')]
p.save()
