from records import commit,OUT
tex=(OUT.parents[1]/'source/SP58_CW_156-5_witnesses/codex/J156-5-05/pages/J156-5-05_156-5_scan041.tex').read_text()
for a,b in [(r'{\unsure{\tau|\mathcal T}}',r'\tau'),(r'\deleted{C=}',r"\deleted{\unsure{C'|C}=}"),(r'\unsure{fermé de|partie de}','fermé de'),(r'\unsure{Soit|Soient}',r'\unsure{Soient|Soit}'),(r'\unsure{-|\longrightarrow}',r'\longrightarrow'),(r'\unsure{\mathscr{T}|\mathcal T|\tau}',r'\mathscr{T}'),(r'\unsure{a|\ast}','a'),(r'\unsure{B}',r'B'),(r'\unsure{\longrightarrow}',r'\longrightarrow'),(r'\unsure{u|U}','u'),(r'\unsure{_a}',r'_a'),(r'\unsure{X\cap U}',r'X\cap U'),(r'\unsure{\subset}',r'\unsure{\subset|\tau}'),(r'\unsure{sont|sont alors}','sont')]:
 assert a in tex,a
 tex=tex.replace(a,b)
ch=[]
def add(place,c,h,f,e,k='misread word',conf='high',ac=False,ah=True,hm=False,con=''):ch.append((place,c,h,f,e,k,conf,ac,ah,hm,con))
add('topology glyphs throughout','τ','calligraphic T','τ','Both halves: the same looped lowercase topology glyph as on 039–040, distinct from the large underlined family letter.','misread symbol or index')
add('cancelled opening formula, left C','C','C','C′ / C','041 top_C crop (490,20,915,155): raised curved stroke to upper right of C; it may be a prime or a guide to the inserted car C est clause.','misread symbol or index','low',True,True)
add('opening formula cancellation','whole formula deleted','formula rendered live; note says top deleted','whole formula deleted','Upper half: two long diagonal cancellation strokes span the formula, labels and continuation.','insertion or placement')
add('opening formula underlabels','straight underbrackets','underbraces','straight underbrackets','Upper half: flat lines with short end turns, no central brace cusp.','drawing or diagram')
add('right underlabel original','fermé de / partie de','fermeture dans','fermé de','041 underlabel crop (930,150,1620,328): long f descender, fermé ending and de under the shorter horizontal cancellation.','misread word')
add('right underlabel revision state','insertion within cancelled block','plain cancelled continuation','insertion within cancelled block','Same underlabel crop: partie de S ... sits on new raised/smaller baselines across the old fermé de (S,τ), soit A.','insertion or placement')
add('right underlabel prime','τ′_0 / τ_0','τ′_0','τ′_0 / τ_0','Same crop: the diagonal deletion crosses the place of the small high mark; prime remains uncertain.','misread symbol or index','medium')
add('cancelled prose after OK','Je voudrais résumer ... un lemme topologique','Je voudrais voir ... un langage topologique','Je voudrais résumer ce qui a été vu dans un lemme topologique plus général','Upper half y365–585: long résumer and short lemme are plainly visible under the diagonal cancellation.')
add('lemma first word','Soit / Soient','Soient','Soient / Soit','041 soit crop (671,650,857,745): the word extends beyond an early t-like stroke to a final upright; Soient preferred, but retracing leaves Soit possible.','misread word','medium',True,False)
add('first pair old letter','cancelled T before S','omitted','cancelled T before S, doubtful','Upper half: broad old cap beneath the S.','omission','low')
add('T before subset','cancelled subscript 0 / emptyset','omitted','cancelled subscript 0 / emptyset','041 old_indices crop (315,785,437,885): lower oval with an oblique crossing; cannot distinguish 0 plus deletion from old empty-set sign.','omission','low')
add('before sur T','cancelled p','omitted','cancelled p, doubtful','Upper half: independent short descender before live sur.','omission','medium')
add('second abandoned opening end','Il y a alors d′','Il y a alors','Il y a alors d′, d′ doubtful','Lower half top: small ascender and flick at right of alors inside the cancellation.','omission','low')
add('family letter in Soit and (a)','underlined script T, first uncertain','Fraktur T','underlined script T','Lower half: large two-loop calligraphic capital, repeated with underline in (a), distinct in size and construction from τ.','misread symbol or index','medium')
add('(a) least-fine wording','la moins fine que toutes','la moins fine de toutes','la moins fine que toutes','Lower half y1640–1700: que has a descending q, retained despite nonstandard comparative grammar.','misread word')
add('(a) named topology','τ′_a / τ′_*','τ′','τ′_a','041 a_index crop (1395,1610,1545,1700): low rounded loop and rightward tail of a; no radial star.','omission','high',False,True,False,'The named least-fine topology carries an a subscript, omitted in H.')
add('(b) topology named in closedness','τ, unprimed','τ′','τ, unprimed','Lower half y1810–1870: ample space after the topology symbol and no detached prime.','misread symbol or index','high',False,True,False,'The lemma’s closedness criterion literally says τ, although it describes the new least-fine topology.')
add('(b) necessity/sufficiency abbreviation','il f et s.','il faut et il suffit','il f et s.','Lower half: standalone f and s., not full words.','expansion or normalisation')
add('condition 1, overwrites','cancelled A under X, B under U, long arrow','cancelled X∩U before full line','C separate overwrites retained','041 conditions crop (635,1940,1265,2180): crossed old angular letter under X, B-like stem/bowl under U and an arrow below the inserted equality. No separate cancelled complete X∩U at the start.','insertion or placement','medium')
add('definition labels in conditions 1 and 2','dfn','déf','dfn','Conditions crop: reduced d-f-n, with a final short n, above both equals signs.','misread word')
add('condition 1 and condition 3 X index','u / U in first, u in third','U in both','u in both','Conditions crop: short rounded lower-case u, about half the height of U in the defining formula.','misread symbol or index','high')
add('condition 2 old index at first X','cancelled a','omitted','cancelled a','Conditions crop: small oval/tail crossed beside the first X.','omission','medium')
add('condition 2 old B under T, left and right','cancelled B at both T occurrences','omitted','cancelled B at both T occurrences','Conditions crop: broad two-bowl B remnants beneath the live T crossbars.','omission','medium')
add('condition 3 cancelled first closure','overline X∩U, uncertain','ill.','overline X∩U','Conditions crop: X and intersection, followed by the rounded U beneath overline and hatching.','readable ink left as \\ill{}','medium',False,True,True)
add('condition 3 cancelled sign before ∩T','subset','omitted','subset / τ','Conditions crop: hooked old sign with extra crossing loops; subset remains preferred, tau-like old start possible.','misread symbol or index','low',True,True)
add('condition 3 old final subscript','cancelled B under T','omitted','cancelled B under T','Conditions crop: B’s lower loop is distinct beneath the T.','omission','medium')
add('cancelled (c) wording','sont / sont alors; écrits de façon canonique sous la forme +/t','sont exactement ceux de la forme ill. ill. ill. fermés','sont écrits (doubtful) de façon canonique sous la forme +/t','041 c crop (287,2178,1655,2310): de façon canonique and sous la forme are directly visible, no exactement ceux or final fermés. A single vertical crosses the strike at the very end.','misread word','medium',False,True,True)
inv=[('text','top right','40'),('deletion','upper entire block','car C est τ′-fermé; C′/C=(C∩T)∪closure...; OK...'),('insertion','upper above equation within deletion','car C est τ′-fermé'),('display','upper cancelled','C′/C=(C∩T)∪closure(C∩(S∖T))'),('insertion','right underlabel within deletion','partie de S dont la trace sur T...'),('text','lemma heading','Lemme'),('text','lemma assumptions','Soient/Soit (S,τ) espace topologique'),('deletion','lemma assumptions','T under S; subscript 0/emptyset; p'),('display','lemma continuity','(T,τ′_0)→(S,τ) continue'),('deletion','two abandoned starts','Soit τ′ une topologie sur; Il y a alors d′'),('text','family definition','Soit script T l’ens des topologies'),('text','conditions of family','1° plus fines; 2° induisent τ′_0'),('text','circled a','Il y a alors ... la moins fine que toutes'),('text','circled b','Pour qu’une partie X ...'),('display','three conditions in b','X∩U=X_u; X∩T=X_T; closure(X_u)∩T⊂X_T'),('deletion','three conditions','A; B; arrow; a; B; B; closure(X∩U); subset/tau; B'),('insertion','definition signs','dfn above both equals signs'),('deletion','circled c at foot','Les fermés de τ′ sont écrits ... sous la forme +/t')]
notes='''### 041-N1 — General topological lemma

After a cancelled continuation of the previous proof, the page begins a lemma for an arbitrary topological space (S,τ), a closed subset T and a finer topology τ′_0 on T. It defines an underlined family of extensions, names a least-fine member τ′_a and states a three-condition closedness criterion using U=S∖T and X_u, X_T. Clause (c) is cancelled. Manuscript page 40; no date.

### 041-N2 — Literal anomalies

Clause (a) says “la moins fine que toutes”. Clause (b) has an unprimed τ, although the criterion is for the newly constructed least-fine topology. The lower-case u in X_u differs from the upper-case U defining the open complement. The cancelled initial equation has a raised curved mark after C, now recorded as C′/C: a prime and an insertion guide are both possible. In the cancelled underlabel, the trace on S∖T is literally said to equal S∖T. These are preserved and not repaired.

### 041-N3 — Targeted check of the intended criterion

For the least-fine topology with closed sets A∪B, A τ-closed and B τ′_0-closed in T, write X_u=X∩U and X_T=X∩T. If X=A∪B, then X_u=A∩U is relatively τ-closed, X_T=(A∩T)∪B is τ′_0-closed, and cl_τ(X_u)∩T⊂A∩T⊂X_T. Conversely, relative closedness gives cl_τ(X_u)∩U=X_u; together with the boundary inclusion, X=cl_τ(X_u)∪X_T. This is a closed set of the constructed topology. The proof uses only finite unions of closed sets and arbitrary intersections, so it applies to general topologies, not just the preceding ultratopologies. The check concerns the intended primed topology, not the literally unprimed τ of clause (b).'''
doubts=r'''| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| cancelled opening left object | C′ | C with insertion guide | low |
| cancelled right underlabel topology | τ′_0 | τ_0 | medium |
| lemma first word | Soient | Soit | medium |
| older letter under S | T | obscured cap | low |
| old index on T | 0 | emptyset | low |
| cancelled before sur T | p | abandoned downstroke | medium |
| abandoned second opening | d′ | unclear start | low |
| condition 1 old letter | A | obscured diagonal | low |
| condition 3 cancelled sign | subset | τ | low |
| clause c after sont | écrits | heavily crossed letters | low |
| clause c last sign | + | t or abandoned vertical | low |

All 24 listed C doubt places were examined. Resolved: ordinary τ; old fermé de; continuity arrow; script family T; a subscript on τ′; the B overwrites in the three conditions; cancelled arrow; lower-case u; old subscript a; cancelled closure X∩U; and sont. Soient is re-ranked but not forced to certainty. No whole word requires an illegible placeholder on this sheet.'''
hand='''The large underlined family T has two conspicuous loops; a script capital is used consistently, separate from lower-case τ. The a index is a small rounded oval with a right tail, not an asterisk. The repeated earlier B beneath live T retains both bowls. A small prime-like curve above C could also be a placement guide to the raised phrase; it is explicitly left unresolved.'''
commit(41,tex,ch,inv,notes,doubts,hand,notation='Script T denotes the family of extension topologies; τ′_a is its least-fine member. U now denotes S∖T globally. X_u retains the small u shape, and X_T uses T.',abbr='ens = ensemble; il f et s. = il faut et suffit; dfn = définition; top. = topologie.',checks=[('041-N3-criterion','targeted proof check','Proved necessity and sufficiency of relative closedness, closed trace and boundary containment for the intended least-fine extension using X=cl_tau(X_u) union X_T. Literal unprimed τ retained.')])
