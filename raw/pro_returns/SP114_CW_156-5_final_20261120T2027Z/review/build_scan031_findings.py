from pathlib import Path
import json, csv, re

ROOT = Path('/workspace/scratch/d7b9f54fbe44')
OUT = ROOT / 'deliverable/review'
manifest = json.loads((OUT/'scan031_crop_manifest.json').read_text())
crops = {r['locus']: r for r in manifest}

draft = r'''\scanpage{31}\mspage{30}
% @ top, part a
a) $F'$ est une figure. \deleted{i.e.} Notons que \deleted{$|F'|=$}
% @ top, support with braces
\[
 |F'|=\underbrace{|G'|}_{|G|}\cup\underbrace{|F\setminus G|}_{\supset |F|\setminus |G|}\deleted{\unsure{=|\supset}}\supset |F|
\]
% @ upper part, connector
donc, comme $|F'|\subset |F|$, on a
% @ upper part, support equality
\[
 |F'|=|F|
\]
% @ upper part, argument
Il faut prouver que $\forall x\in |F'|=|F|$, $\exists$ plus petit \unsure{élémt|élément|élt} de $F'$ qui le contienne. Distinguons deux cas

% @ upper middle, first case
1$^\circ$) $x\in |G|=|G'|$, soit $A\in G'\deleted{\unsure{\circ}}$ tel que $x\in A^{\circ(G')\deleted{\unsure{)|?}}}$. Si $B\in F'$ et \deleted{\unsure{B}} $x\in B$, prouvons $A\subset B$. Si $B\in G'$, c'est évident. Si $B\in F\setminus G$, alors \deleted{$B$ contient} $A^{\circ(G')}\cap B\ne\phi$ donc $A^{\unsure{\circ|\bullet|*}}\subset B$ OK

% @ middle, second case
2$^\circ$) $x\in |\deleted{\unsure{G}}F|\setminus |G|$, alors les $\deleted{\unsure{B}}A\in F'$ qui contiennent $x$ ne sont pas dans $G'$, ils sont donc dans $F\setminus G$. D'autre part, l'unique \unsure{élémt|élément|élt} $A$ de $F$ tel que $x\in A^{\circ(F)}$ n'est pas dans $G$ puisque $x\notin |G|$, il est donc dans $F\setminus G$, et \deleted{\unsure{si $x\in A$}} c'est \unsure{lui|le} plus petit él. de $F$ (et à fortiori de $F\setminus G$) qui contient $x$, OK~!

% @ lower middle, part b
b) $F'$ \deleted{\unsure{raffine}}\inserted{subdivise} $F$. Comme $|F'|=|F|$, il faut voir \unsure{seult|seulement} que $F'$ raffine $F$. Donc \deleted{que \unsure{tout}} que
% @ lower part, cancelled attempt
\deleted{1$^\circ$) \deleted{$\forall$} $A\in F'$, \unsure{et} l'ens $F^A$ des $B\in F$ tels que $A\subset B$ \unsure{est contenu dans|contienne} un plus petit \inserted{\unsure{a un plus petit}} \unsure{élémt|élément|élt} de $F$. C'est évident si $A\in F$ c'est évident. Si}
\deleted{\unsure{str.} de de $F'$ raffine $F$. Si}

% @ lower part, restated first condition
1$^\circ$) \deleted{$\forall$} $A\in F'$, l'ens $F^A=\{B\in F\mid \deleted{\unsure{B}}A\subset B\}$ a un plus petit \unsure{élémt|élément|élt}. C'est évident si $A\in F$ \deleted{$(B=A)$} (on prend $B=A$) et si $A\in G'$, c'est vrai puisque $G'\ll F$.

% @ bottom, second condition
2$^\circ$) Si $A\in F'$, $B\in F$, alors $A\cap B$ est \deleted{\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.}}\inserted{fermé dans $F'$}, i.e. réunion de strates de $F'$. Si $A\in G'$, comme $G'\ll F$, $A\cap B$ est réunion de strates de $G'$, qui sont aussi des strates de $F'$.
'''
(OUT/'scan031_draft.tex').write_text(draft, encoding='utf-8')

changes=[]
def ch(id,place,C,H,final,evidence,locus,confidence='high',kind='word',against_C=False,against_H=True,H_marked=False,certainty_only=False,consequential=False):
    m=crops[locus]
    changes.append(dict(id=f'031-{id:02}',place=place,C=C,H=H,final=final,evidence=evidence,crop=m['crop'],box=m['box'],rotation=m['rotation'],confidence=confidence,kind=kind,against_C=against_C,against_H=against_H,H_marked=H_marked,certainty_only=certainty_only,consequential=consequential))

ch(1,'folio at head',r'\mspage{30}','not represented in supplied page excerpt',r'\mspage{30}','A two-lobed 3 followed by a closed oval 0 is written above the body; the scan number 31 is metadata, not a second ink numeral.','number',kind='omission')
ch(2,'a), first F prime',r"${\unsure{F|\mathcal F}}'$",r"$F'$",r"$F'$",'The capital has one upright, a bent top crossbar and a separate shorter middle crossbar. No script loop distinguishes it from the ordinary Fs elsewhere on this sheet.','opening',kind='symbol',against_H=False,certainty_only=True)
ch(3,'support display, cancelled relation before final superset',r'\deleted{\unsure{=|\supset}}','omitted',r'\deleted{\unsure{=|\supset}}','A small worked-over oval/parallel-stroke group intervenes between the second support and the live superset. Its cancellation is certain; the original relation is not. The whole support formula and both underbrace labels were read with it.','support_display','low','state',consequential=True)
ch(4,'support equality display, terminal punctuation','no point','point after final support','no point','The right support bar is followed by blank paper; no dark separate full stop is visible in the crop.','support_equality',kind='punctuation')
ch(5,'introductory argument, petit élément word',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','Accented initial e and tall l survive; the medial letters contract to low strokes and the final t rises. The exact abbreviation cannot safely be expanded.','argument_elt','medium','abbreviation')
ch(6,'case 1, after A in G prime',r"$G'\deleted{\unsure{\circ}}$",r"$G'$",r"$G'\deleted{\unsure{\circ}}$",'A separate small densely retraced mark sits immediately to the right of the prime. Cancellation is visible, but the original circle is not fully recoverable.','case1_first','low','state',consequential=True)
ch(7,'case 1, end of the first A exponent',r"$A^{\circ(G')\deleted{\unsure{)|?}}}$",r"$A^{\circ(G')}$",r"$A^{\circ(G')\deleted{\unsure{)|?}}}$",'The open circle and parenthesized G prime are clear; the closing area contains an additional heavy descending/retraced hook. The distinction extra closing parenthesis/question-like hook remains open.','case1_first','low','state',consequential=True)
ch(8,'case 1, after et and before x in B',r'\deleted{\unsure{B}}',r'\struck{\ill{}}',r'\deleted{\unsure{B}}','The cancelled group has a vertical and remnants of two rightward bowls. B is plausible but heavy diagonal and horizontal strokes prevent a fully certain reading.','case1_deleted_B','low','symbol',H_marked=True,consequential=True)
ch(9,'case 1, nonempty intersection',r'\varnothing',r'\emptyset',r'\phi','A long slanted stem passes through a narrow upright oval. This is the author’s phi-shaped empty-set sign, rather than a separately slashed round zero. The whole intersection was inspected.','case1_middle',kind='symbol',against_C=True,consequential=True)
ch(10,'case 1, final raised mark on A',r'\unsure{\bullet|\circ}',r'*; editorial note allows a star or emphasized circle',r'\unsure{\circ|\bullet|*}','The enlarged mark is a thick closed diamond/loop with a small white central aperture; no distinct spokes appear. This favors a heavily inked circle, while the small original mark warrants retaining the alternatives for adjudication.','case1_end','medium','symbol',against_C=True,H_marked=True,consequential=True)
ch(11,'case 2, overwritten letter within first support',r'|\deleted{\unsure{G}}F|',r'|F|',r'|\deleted{\unsure{G}}F|','The live F has two horizontal bars, with a curved earlier stroke visible to its left/underneath. G is compatible with the remnant, not certain.','case2_start','low','state',consequential=True)
ch(12,'case 2, overwritten letter before membership in F prime',r"\deleted{\unsure{B}}A\in F'",r"A\in F'",r"\deleted{\unsure{B}}A\in F'",'The live angular A overlays a rounded two-bowl form. The earlier B remains marked doubtful because the overwritten strokes intersect its bowls.','case2_start','low','state',consequential=True)
ch(13,'case 2, l’unique élément word',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','A tall l and final rising t frame a compressed medial stroke; the crop does not establish an unabbreviated élément.','case2_elt','medium','abbreviation')
ch(14,'case 2, cancelled phrase after et',r'\deleted{\unsure{si $x\in A$}}',r'\struck{\ill{} $A$}',r'\deleted{\unsure{si $x\in A$}}','Initial s-like bend and i dot, a crossed x-like middle, membership and final A remain under several cancellation strokes. The full phrase is plausible but not every letter is plain, so its doubt is retained.','case2_deleted_si','low','word',H_marked=True,consequential=True)
ch(15,'case 2, c’est le/lui','le','lui',r'\unsure{lui|le}','After c’est, the crop shows a tall looped l, a low rounded shoulder and a separate high dot above a short final upright. Those strokes favor lui. The expected grammar is not used to replace the ink.','case2_le','medium','word',against_C=True,consequential=True)
ch(16,'case 2, parenthesis after él. de F',r'(et à fortiori de $F\setminus G$)',r'(cf. définition de $F\smallsetminus G$), placed before plus petit',r'(et à fortiori de $F\setminus G$)','The parenthesis is physically after él. de F. It starts et, has a visibly accented a, then the tall descending f and t/i strokes of fortiori. There is no cf. or définition on this line.','case2_fortiori',kind='word',consequential=True)
ch(17,'case 2, H’s qui est before plus petit','absent',r'qui \uncertain{est}','absent','The line ends at the le/lui word; the next line begins plus petit. There are no intervening qui est strokes. The only visible qui follows the fortiori parenthesis.','case2_end',kind='omission',H_marked=True,consequential=True)
ch(18,'case 2, final qui contient',r'qui contient $x$',r'contenant $x$',r'qui contient $x$','A separate qui stands after the closing parenthesis; on the following line the verb has the dotted i and final t strokes of contient, followed by x, comma, OK and exclamation.','case2_contient',kind='word',consequential=True)
ch(19,'b), seult word',r'\unsure{seult}','seulement',r'\unsure{seult|seulement}','The word has initial seu, a tall l and a flat middle ending in t. A short form is favored, but the compressed middle is not sufficiently discriminating to resolve the spelling.','b_seult','medium','abbreviation',against_C=True)
ch(20,'b), H’s deletion before seulement','absent',r'\struck{\ill{}}','absent','The space before the initial seult stroke contains no independent cancelled word. Long strokes higher up belong to the two f descenders of the previous line’s cancelled raffine.','b_heading',kind='state',H_marked=True)
ch(21,'b), cancelled raffine',r'\deleted{\unsure{raffine}}',r'\struck{raffine}',r'\deleted{\unsure{raffine}}','Two tall f-like descenders and a dotted i are clear, but the initial and medial letter bodies are covered by the cancellation. C’s explicit doubt is retained. The above-line subdivise attaches to this word.','b_refine_subdivide','medium','certainty',certainty_only=True)
ch(22,'b), cancelled que tout',r'\deleted{que \unsure{tout}}',r'\struck{que \ill{}}',r'\deleted{que \unsure{tout}}','After the crossed que is a tall initial t and low connected letters; the final stroke can be t. The noun phrase remains doubtful under its stroke.','b_que_tout','low','word',H_marked=True)
ch(23,'b), second que after the cancellation','live que','included within the following deletion','live que','The second que lies to the right of the stopped cancellation, with its q descender clear and no strike through its body. The nearby A subset B belongs to the boxed cancelled argument below.','b_que_tout',kind='state',consequential=True)
ch(24,'cancelled attempt, sign after 1 degree',r'\deleted{Soit}','no equivalent sign recovered in the supplied H order',r'\deleted{$\forall$}','Two oblique sides meeting low and a middle crossbar form an inverted A; the same cancelled sign appears more clearly before the restated condition. There are no separate letter forms for Soit.','cancel_addition',kind='symbol',against_C=True,consequential=True)
ch(25,'cancelled attempt, A in F prime and et',r"$A\in F'$, \unsure{et}",r"$A\subset B$ in the leading cancellation; $A\in F'$ displaced after tels que",r"$A\in F'$, \unsure{et}",'The membership crescent/bar and F prime follow the initial A in the left part of the cancelled row. The two short word strokes after its comma remain uncertain as et. The upper continuation has l’ens F^A des B in F tels que A subset B.','cancel_line1','medium','word',consequential=True)
ch(26,'cancelled attempt, l’ens punctuation',"l'ens","l'ens.","l'ens",'The terminal s stroke has no separate dot before F superscript A.','cancel_line1',kind='punctuation')
ch(27,'cancelled attempt, verbal phrase',r'\unsure{est contenu dans}','contienne with earlier unreadable text',r'\unsure{est contenu dans|contienne}','Below the raised l’ens continuation, the cancelled phrase begins with low joined strokes then a co-like curve, a tall t-like stem, more low minims and a d-like loop. C’s est contenu dans is favored, but the strike prevents excluding contienne.','cancel_line1','low','word',against_C=True,H_marked=True,consequential=True)
ch(28,'cancelled attempt, slanted left addition',r'\inserted{\unsure{a un plus petit}}',r'1) \ill{} un plus petit',r'\inserted{\unsure{a un plus petit}}','The little slanted addition begins with an isolated a-like loop then un plus petit. Its curved leader reaches the following abbreviated élément region. It is an insertion inside the subsequently cancelled block, not a second numbered item. Some letters intersect the cancellation and remain doubtful.','cancel_addition','medium','state',H_marked=True,consequential=True)
ch(29,'cancelled attempt, abbreviated élément',r'\unsure{élémt|élément|élt}','él.',r'\unsure{élémt|élément|élt}','The crossed word extends beyond an e/l pair to a terminal raised t-like stroke; H’s bare él. loses visible medial/final ink. Exact spelling remains uncertain.','cancel_line2','low','abbreviation')
ch(30,'cancelled lower line, str. de de',r'\unsure{str.} de de',r'\ill{}',r'\unsure{str.} de de','The line starts with a tall/looped group and a separate point, then two distinct short de-like groups before F prime. The duplicate is retained; the initial abbreviation stays uncertain.','cancel_line3','medium','word',H_marked=True,consequential=True)
ch(31,'restated condition 1, cancelled initial sign',r'\deleted{Soit}',r'\struck{$\forall$}',r'\deleted{$\forall$}','The surviving symbol is an inverted A with a crossbar, crossed by a diagonal stroke. Its two legs and bar are individually visible; the form does not contain the letters S-o-i-t.','restated_first',kind='symbol',against_C=True,against_H=False,consequential=True)
ch(32,'restated condition 1, l’ens punctuation',"l'ens","l'ens.","l'ens",'The final low s has a hooked end but there is no separate point between it and F superscript A.','restated_first',kind='punctuation')
ch(33,'restated condition 1, overwritten B before A subset B',r'\deleted{\unsure{B}}A\subset B',r'A\subset B',r'\deleted{\unsure{B}}A\subset B','The first A of the predicate contains an older rounded/vertical stroke under the angular live A. B is compatible with the two remnants but remains uncertain.','restated_first','low','state',consequential=True)
ch(34,'restated condition 1, petit élément word',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','The word again consists of accented initial e, tall l, flattened medial ink and a final t-like rise. No expansion is imposed.','restated_elt_BA','medium','abbreviation')
ch(35,'condition 2, cancelled R-sub-F-prime adjective',r'\unsure{$\mathcal R_{F\prime}$-satu.|$\mathscr R_{F\prime}$-satu.}',r'$R_{F\prime}$-\ill{}',r"\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.}",'The capital has a broad upper loop and a looped lower leg, followed by low F prime. To its right, s-like, a/t and u-like traces survive plus a final point. The strike prevents fully resolving the alphabet or abbreviation; the above-line fermé dans F prime clearly replaces the whole cancelled expression.','bottom_ferme','low','symbol',H_marked=True,consequential=True)

unresolved=[]
def un(place,reading,alternatives,reason,confidence):
    unresolved.append(dict(place=place,reading=reading,alternatives=alternatives,reason=reason,confidence=confidence))
un('support display cancelled relation','=',[r'\supset'],'The cancellation obscures whether two short traces originally formed equals or the return strokes of a superset.','low')
for p in ['introductory argument','case 2 l’unique','cancelled attempt','restated condition 1']:
    un(p+' élément word','élémt',['élément','élt'],'Middle letter strokes collapse to a low run; preserve the abbreviation candidates.','low' if p=='cancelled attempt' else 'medium')
un('case 1 after G prime',r'\circ',[],'The extra small superscript is worked over and cannot be assigned a fully certain original shape.','low')
un('case 1 end of first exponent',')',['?'],'A second closing/hooked retrace remains beside the clear parenthesized G prime.','low')
un('case 1 cancelled capital before x in B','B',[],'Upper and lower bowl remnants are cut by several strikes.','low')
un('case 1 final A superscript',r'\circ',[r'\bullet','*'],'White central aperture favors a thick circle; tiny original size prevents excluding a solid/star reading for final adjudication.','medium')
un('case 2 underlying first support letter','G',[],'A curved remnant survives under the live F.','low')
un('case 2 underlying letter before A in F prime','B',[],'Rounded older strokes lie under the live A.','low')
un('case 2 cancelled phrase',r'si $x\in A$',[],'Heavy strike covers parts of the initial word and x.','low')
un('case 2 c’est word','lui',['le'],'Looped l, low shoulder and dotted final upright favor lui. No qui est is visible before plus petit; grammar does not decide the word.','medium')
un('b cancelled verb','raffine',[],'Two f descenders are clear, but not every initial/medial letter survives the strike.','medium')
un('b short adverb','seult',['seulement'],'Flattened medial letters permit a short form but do not safely establish its exact spelling.','medium')
un('b cancelled word after que','tout',[],'Tall initial and final strokes frame two occluded low letters.','low')
un('cancelled attempt after A in F prime','et',[],'Two small joined strokes are cut by the global cancellation.','low')
un('cancelled attempt verbal phrase','est contenu dans',['contienne'],'Word bodies are crossed through the baseline, though separate d-like and t-like uprights favor C.','low')
un('cancelled slanted insertion','a un plus petit',[],'Initial isolated a-like loop and plus petit are favored; strokes intersect the cancellation and the attachment is via the following élément region.','medium')
un('cancelled final line opening','str.',[],'Tall loop and low short strokes followed by a point; expansion is not supplied.','low')
un('restated condition 1 underlying predicate capital','B',[],'Live angular A covers rounded previous ink.','low')
un('final cancelled adjective',r'$\mathcal R_{F\prime}$-satu.',[r'$\mathscr R_{F\prime}$-satu.'],'Looped R and low F prime are present; font-family distinction and crossed abbreviation remain unresolved.','low')

states=[]
def st(id,macro,C,final,scope,attachment,locus,confidence='high'):
    m=crops[locus]
    states.append(dict(id=f'031-S{id:02}',C_macro=macro,C=C,final=final,scope=scope,attachment=attachment,crop=m['crop'],box=m['box'],rotation=m['rotation'],confidence=confidence,inspected=True))
st(1,'deleted','i.e.','i.e.','Only i.e. between figure. and Notons que is cancelled.','None; live Notons que follows.','opening')
st(2,'deleted',r"$|F'|=$",r"$|F'|=$",'Cancelled inline start of equality following Notons que.','Rewritten as the display below.','opening')
st(3,'deleted',r'\unsure{=|\supset}',r'\unsure{=|\supset}','Only the short relation-like group before the final live superset.','After second underbraced support, before live superset.','support_display','low')
st(4,'deleted',r'\unsure{\circ}',r'\unsure{\circ}','Small overwritten superscript after G prime; prime itself remains live.','A in G prime in first case.','case1_first','low')
st(5,'deleted',r'\unsure{)|?}',r'\unsure{)|?}','Extra high hook beside the exponent closing parenthesis, not the open circle or G prime.','Within exponent of first A in case 1.','case1_first','low')
st(6,'deleted',r'\unsure{B}',r'\unsure{B}','Cancelled capital between et and x in B.','No replacement at the same spot; live x in B follows.','case1_deleted_B','low')
st(7,'deleted',r'$B$ contient',r'$B$ contient','A single crossing covers B and contient; the following A exponent is live.','Superseded by the intersection assertion immediately following.','case1_middle')
st(8,'deleted',r'\unsure{G}',r'\unsure{G}','Older curved letter within the first support bars of case 2.','Overwritten by live F.','case2_start','low')
st(9,'deleted',r'\unsure{B}',r'\unsure{B}','Earlier rounded capital before membership in F prime.','Overwritten by live A.','case2_start','low')
st(10,'deleted',r'\unsure{si $x\in A$}',r'\unsure{si $x\in A$}','Short phrase after et and before c’est; A at its right is inside the cancellation.','Live c’est le/lui follows.','case2_deleted_si','low')
st(11,'deleted',r'\unsure{raffine}',r'\unsure{raffine}','Whole baseline verb between F prime and F, excluding the replacement above.','Replaced by subdivise.','b_refine_subdivide','medium')
st(12,'inserted','subdivise','subdivise','Above-line verb over cancelled raffine.','Attaches between F prime and F.','b_refine_subdivide')
st(13,'deleted',r'que \unsure{tout}',r'que \unsure{tout}','First que plus following doubtful tout; cancellation stops before the second live que.','After Donc, before the live que introducing the abandoned argument.','b_que_tout','low')
st(14,'deleted','Entire first cancelled attempt through its terminal Si','Entire first cancelled attempt through its terminal Si','The long abandoned block is crossed/boxed, including its left 1 degree, formula, prose, and nested slanted insertion.','Follows the live second que; no text is promoted from it to the restated condition.','cancel_line1','medium')
st(15,'deleted (nested)','Soit',r'$\forall$','Distinct heavily cancelled inverted-A sign inside the larger cancelled attempt.','After its 1 degree label, before A in F prime.','cancel_addition')
st(16,'inserted (inside deletion)',r'\unsure{a un plus petit}',r'\unsure{a un plus petit}','Slanted left/interlinear phrase, subsequently included in the cancellation.','Curved leader reaches the following élément region; transcription retains C’s local insertion placement, with attachment uncertainty noted.','cancel_addition','medium')
st(17,'deleted',r"\unsure{str.} de de $F'$ raffine $F$. Si",r"\unsure{str.} de de $F'$ raffine $F$. Si",'Lowest cancelled row; both de-like groups are within the same cancellation.','Continuation of the abandoned attempt.','cancel_line3','medium')
st(18,'deleted','Soit',r'$\forall$','Cancelled inverted-A symbol; following A in F prime is live.','After restated 1 degree label.','restated_first')
st(19,'deleted',r'\unsure{B}',r'\unsure{B}','Earlier rounded capital under the first A of the set predicate.','Overwritten by live A in A subset B.','restated_first','low')
st(20,'deleted',r'$(B=A)$',r'$(B=A)$','Whole parenthesized equality, including both parentheses.','Replaced by the following live parenthesis (on prend B=A).','restated_first')
st(21,'deleted',r"\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.}",r"\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.}",'Whole R-sub-F-prime adjective is struck; its lower subscript remains part of that cancelled expression.','Replacement above is fermé dans F prime.','bottom_ferme','low')
st(22,'inserted',r"fermé dans $F'$",r"fermé dans $F'$",'Above-line phrase spanning cancelled R adjective.','Attaches directly after est, before i.e. réunion.','bottom_ferme')

inventory=[]
def inv(element,kind,position,first_words_or_objects):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first_words_or_objects,hand='handwritten'))
inv('folio','number','top centre',r'30')
inv('a opening','text block','top',r"a) $F'$ est une figure")
inv('support decomposition','display','top below opening',r"|F'|=\underbrace{|G'|}_{|G|}\cup\underbrace{|F\setminus G|}_{\supset |F|\setminus |G|}")
inv('support connector','text block','upper part',r"donc, comme $|F'|\subset |F|$")
inv('support equality','display','upper part centre',r"|F'|=|F|")
inv('existence argument','text block','upper part',r'Il faut prouver que $\forall x$')
inv('case 1','text block','upper middle',r"1$^\circ$) $x\in |G|=|G'|$")
inv('case 2','text block','middle',r'2$^\circ$) $x\in |F|\setminus |G|$')
inv('b introduction','text block','lower middle',r"b) $F'$ \deleted{\unsure{raffine}}\inserted{subdivise} $F$")
inv('restated condition 1','text block','lower part',r"1$^\circ$) \deleted{$\forall$} $A\in F'$")
inv('condition 2','text block','bottom',r"2$^\circ$) Si $A\in F'$, $B\in F$")
for s in states:
    inv(s['id'], 'insertion' if s['C_macro'].startswith('inserted') else 'deletion', {'box':s['box'],'attachment':s['attachment']}, s['final'])

boxes=[]
def bx(name,kind,locus,reading,box=None):
    m=crops[locus]; z=box or m['box']
    boxes.append(dict(box=name,kind=kind,x0=z[0],y0=z[1],x1=z[2],y1=z[3],reading=reading,crop=m['crop'],rotation=m['rotation']))
bx('031-B01','number','number',r'\mspage{30}')
bx('031-B02','deletion','opening',r"a) $F'$ est une figure. \deleted{i.e.} Notons que \deleted{$|F'|=$}")
bx('031-B03','formula doubt','support_display',r"$|F'|=\underbrace{|G'|}_{|G|}\cup\underbrace{|F\setminus G|}_{\supset |F|\setminus |G|}\deleted{\unsure{=|\supset}}\supset |F|$")
bx('031-B04','formula','support_equality',r"$|F'|=|F|$")
bx('031-B05','word difference','argument_elt',r"petit \unsure{élémt|élément|élt} de $F'$")
bx('031-B06','number and formula doubt','case1_first',r"1$^\circ$) $x\in |G|=|G'|$, soit $A\in G'\deleted{\unsure{\circ}}$ tel que $x\in A^{\circ(G')\deleted{\unsure{)|?}}}$")
bx('031-B07','deletion','case1_deleted_B',r'et \deleted{\unsure{B}} $x\in B$')
bx('031-B08','deletion and symbol','case1_middle',r"alors \deleted{$B$ contient} $A^{\circ(G')}\cap B\ne\phi$")
bx('031-B09','formula doubt','case1_end',r'$A^{\unsure{\circ|\bullet|*}}\subset B$ OK')
bx('031-B10','number and overwrite','case2_start',r"2$^\circ$) $x\in |\deleted{\unsure{G}}F|\setminus |G|$, alors les $\deleted{\unsure{B}}A\in F'$")
bx('031-B11','word difference','case2_elt',r"l'unique \unsure{élémt|élément|élt} $A$ de $F$")
bx('031-B12','deletion','case2_deleted_si',r"et \deleted{\unsure{si $x\in A$}} c'est \unsure{lui|le}")
bx('031-B13','word difference','case2_le',r"c'est \unsure{lui|le}")
bx('031-B14','word difference','case2_fortiori',r'(et à fortiori de $F\setminus G$) qui')
bx('031-B15','word difference','case2_contient',r'contient $x$, OK~!')
bx('031-B16','insertion and deletion','b_refine_subdivide',r"$F'$ \deleted{\unsure{raffine}}\inserted{subdivise} $F$.")
bx('031-B17','word difference','b_seult',r"\unsure{seult|seulement} que $F'$")
bx('031-B18','deletion and state difference','b_que_tout',r'Donc \deleted{que \unsure{tout}} que')
bx('031-B19','cancelled word differences','cancel_line1',r"\deleted{1$^\circ$) \deleted{$\forall$} $A\in F'$, \unsure{et} l'ens $F^A$ des $B\in F$ tels que $A\subset B$ \unsure{est contenu dans|contienne} un plus petit}")
bx('031-B20','insertion cancelled again','cancel_addition',r'\deleted{\inserted{\unsure{a un plus petit}}}')
bx('031-B21','cancelled word differences','cancel_line2',r"\deleted{\unsure{élémt|élément|élt} de $F$. C'est évident si $A\in F$ c'est évident. Si}")
bx('031-B22','cancelled word differences','cancel_line3',r"\deleted{\unsure{str.} de de $F'$ raffine $F$. Si}")
bx('031-B23','number deletion formula doubt','restated_first',r"1$^\circ$) \deleted{$\forall$} $A\in F'$, l'ens $F^A=\{B\in F\mid \deleted{\unsure{B}}A\subset B\}$ a un plus petit")
bx('031-B24','abbreviation and deletion','restated_elt_BA',r"\unsure{élémt|élément|élt}. C'est évident si $A\in F$ \deleted{$(B=A)$} (on prend $B=A$)")
bx('031-B25','insertion and deleted formula doubt','bottom_ferme',r"$A\cap B$ est \deleted{\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.}}\inserted{fermé dans $F'$}")
bx('031-B26','number and formula','bottom',r"2$^\circ$) Si $A\in F'$, $B\in F$, alors $A\cap B$")

rows=list(csv.DictReader((ROOT/'packets/031/differences.tsv').open(encoding='utf-8'),delimiter='\t'))
decisions={
1:('031-01','Manuscript 30 retained; scan 31 itself is archive metadata/macro only.'),
2:('031-02','Plain F selected on crop; C doubt resolved without changing its preferred reading.'),
3:('031-03','Cancelled relation retained and left doubtful.'),
4:('031-04','No terminal point in equality display.'),
5:('031-05','Keep explicit spelling doubt; no expansion.'),6:('031-05','Same abbreviated word as preceding row.'),
7:(None,'macro-only: itemize wrapper is not ink.'),8:(None,'macro-only: 1 degree notation is the same ink numeral.'),9:(None,'macro-only: item-label closing bracket.'),
10:('031-06','Retain small cancelled superscript after G prime.'),11:('031-07','Retain extra worked-over exponent hook.'),12:('031-08','Retain doubtful cancelled B.'),
13:('031-10','Circle preferred, with bullet/star alternatives retained for final adjudication.'),14:(None,'H editorial note is not source text; local glyph recorded in 031-10.'),
15:(None,'macro-only: item-label bracket.'),16:(None,'macro-only: 2 degree notation.'),17:(None,'macro-only: item-label closing bracket.'),
18:('031-11','Retain overwritten G under F.'),19:('031-12','Retain overwritten B under A.'),20:('031-13','Keep abbreviation candidates.'),21:('031-13','Same abbreviation as preceding row.'),
22:('031-14','Retain doubtful full cancelled phrase.'),23:('031-15;031-16;031-17','Prefer doubtful lui locally; reject H’s inserted/reordered cf. définition and qui est.'),
24:('031-16;031-18','Retain physically positioned et à fortiori parenthesis, qui and contient.'),25:(None,'macro-only: nonbreaking space before exclamation.'),26:(None,'macro-only: itemize closing wrapper.'),
27:('031-19;031-20','Retain adverb doubt and reject H’s unsupported prior deletion.'),28:('031-22;031-23','Retain doubtful tout and keep second que live.'),
29:('031-24','Cancelled initial is forall, within the abandoned 1 degree item.'),30:('031-25','Membership A in F prime is visibly at the left; C order preferred with doubtful et.'),31:('031-26','No separate point after ens.'),
32:('031-25;031-27','Preserve source order and the unresolved est contenu dans/contienne phrase.'),33:('031-28','Slanted a un plus petit is an insertion in a subsequently cancelled block, not a new 1).'),
34:('031-29','Longer abbreviated word retained with alternatives.'),35:('031-30','Retain str. doubt and both de-like words.'),36:(None,'H editorial cancellation note and itemize opening are not ink; source cancellation covered in state audit.'),
37:(None,'macro-only: restated 1 degree notation.'),38:('031-31','Inverted-A universal sign, not Soit; H item-label bracket itself is macro only.'),39:('031-32','No separate point after ens.'),40:('031-33','Overwritten B under A retained.'),
41:('031-34','Keep abbreviation candidates.'),42:('031-34','Same abbreviation as preceding row.'),43:(None,'macro-only: item-label bracket.'),44:(None,'macro-only: final 2 degree notation.'),45:(None,'macro-only: item-label closing bracket.'),
46:('031-35','Retain script-R/satu. doubt; the above-line replacement is separately audited.'),47:(None,'macro-only: itemize closing wrapper.')}
coverage=[]
for i,row in enumerate(rows,1):
    ids,decision=decisions[i]
    coverage.append(dict(row=i,words_before=row['words before'],C=row['witness C'],H=row['witness H'],change_ids=[] if ids is None else ids.split(';'),decision=decision,macro_only=ids is None))

line_ledger=[
'a) F prime est une figure / cancelled i.e. / Notons que / cancelled equality start',
'support decomposition display (underbrace labels inventoried separately)',
'donc, comme ... on a',
'support equality display',
'Il faut prouver que ... exists plus',
'petit élément ... qui le contienne',
'Distinguons deux cas',
'case 1: label and x in G ... A exponent',
'case 1: Si B in F prime ... Si B in G prime',
'case 1: c’est évident ... nonempty intersection',
'case 1: donc A raised mark subset B OK',
'case 2: label, support difference, alors les A in F prime qui contiennent',
'case 2: x ne sont pas dans G prime ... F minus G',
'case 2: D’autre part, l’unique élément A de F tel que',
'case 2: x in A circle(F) ... x not in support G',
'case 2: il est donc ... cancelled si x in A / c’est le-lui',
'case 2: plus petit él. de F (et à fortiori ...) qui',
'case 2: contient x, OK !',
'b heading through il faut voir (subdivise inventoried separately)',
'seult que F prime raffine F / Donc cancelled que tout / live que',
'cancelled attempt first row and raised l’ens continuation',
'cancelled attempt élément de F / repeated c’est évident / Si',
'cancelled lowest row str. de de F prime raffine F. Si',
'restated 1 degree / cancelled forall / set comprehension / a un',
'plus petit élément / C’est évident ... cancelled (B=A)',
'(on prend B=A) et si A in G prime ... puisque',
'G prime much-less-than F.',
'final 2 degree / Si A in F prime, B in F ... cancelled R adjective',
'i.e. réunion de strates de F prime',
'Si A in G prime, comme G prime much-less-than F ... réunion de',
'strates de G prime, qui sont aussi des strates de F prime'
]

crop_times={
'number':'18:41:31','opening':'18:41:31','support_display':'18:41:31','support_equality':'18:41:32','argument_elt':'18:41:32',
'case1_first':'18:45:01','case1_middle':'18:45:08','case1_deleted_B':'18:45:15','case1_end':'18:45:15',
'case2_start':'18:45:30','case2_elt':'18:45:30','case2_end':'18:45:43','case2_le':'18:46:05','case2_fortiori':'18:46:24','case2_contient':'18:46:24','case2_deleted_si':'18:46:34',
'b_heading':'18:46:34','b_refine_subdivide':'18:46:56','b_seult':'18:46:56','b_que_tout':'18:47:11',
'cancel_line1':'18:47:11','cancel_line2':'18:47:34','cancel_line3':'18:47:34','cancel_addition':'18:47:59',
'restated_first':'18:48:20','restated_elt_BA':'18:48:36','bottom_ferme':'18:48:49','bottom':'18:48:49'}
for m in manifest:
    m['inspected_at']='2026-11-20 '+crop_times[m['locus']]+' UTC'
    m['reader']='B'

findings=dict(
scan='031',manuscript_page='30',reader='B',status='proposed; main reader adjudicates',
line_count=len(line_ledger),line_count_convention='Main text/display baseline groups, including the abandoned writing but excluding folio, underbrace-label row and three separate insertions. The slanted abandoned first row and its upper continuation are treated as one source reading group, not two TeX lines.',line_ledger=line_ledger,
image_dimensions=[1681,2360],bottom_half_original_y_offset=1100,
image_views={
'whole':{'count':1,'at':'2026-11-20 18:38:44 UTC','purpose':'layout and inventory'},
'a':{'count':1,'at':'2026-11-20 18:38:55 UTC','purpose':'token-by-token comparison with both witnesses, including agreement'},
'b':{'count':1,'at':'2026-11-20 18:39:15 UTC','purpose':'token-by-token comparison with both witnesses, including agreement'},
'crop_note':'One pre-compaction multi-image response was truncated before a usable visual reading; existing crop files were re-emitted individually. A later broken-pipe tool call did not produce a usable image. Times listed here are successful actual inspections, not those failed deliveries. argument_elt was revisited while still unresolved at 18:50:24. No settled locus was recropped.'},
changes=changes,unresolved=unresolved,inventory=inventory,
hand_habits=[
{'habit':'Ordinary F may have a bent/curved top arm; the separate shorter middle bar decides the plain capital.','scope':'opening F prime and all live F tokens on scan031','evidence':'opening, restated_first, bottom crops; no exceptional script F found','witness_effect':'C opening alphabet doubt resolved'},
{'habit':'The upper stroke of = can curve downward/back at the right, like a small hook; a separate lower bar remains.','scope':'support equality and b heading equality on scan031','evidence':'support_equality compared with b_heading','witness_effect':'Both witnesses retained; no superset was substituted from the first isolated appearance'},
{'habit':'Small raised circles can become thick diamond-like loops with a tiny white centre.','scope':'first-case final A mark, compared locally with open exponent circles','evidence':'case1_end and case1_first','witness_effect':'C bullet/H star preference reconsidered; local circle/bullet/star doubt retained'},
{'habit':'Universal quantifier is a broad inverted A with a mid-bar; under cancellation it can resemble a word scribble.','scope':'both cancelled item starts in b','evidence':'cancel_addition and restated_first','witness_effect':'C Soit replaced by forall at both places; H correct at the restated place'},
{'habit':'The middle of élément/abbreviated forms and seulement/short form contracts to almost flat low strokes.','scope':'four élément words and b adverb','evidence':'argument_elt, case2_elt, cancel_line2, restated_elt_BA, b_seult','witness_effect':'No expansion; local spelling alternatives remain'},
{'habit':'Repeated f descenders in a cancelled prior-line raffine extend toward the following line.','scope':'b heading before seult','evidence':'b_refine_subdivide and b_heading','witness_effect':'H’s extra cancelled illegible word before seulement is not supported'}
],
notation=[
{'notation':r'\phi (ϕ)','meaning':'l’ensemble vide','observed':'A narrow loop on a long slanted stem follows the nonempty-intersection relation in case1_middle.','status':'consistent with current table; source occurrence individually inspected'},
{'notation':r'A^{\circ(G\prime)}, A^{\circ(F)}','meaning':'circle stratum notation indexed parenthetically by figure','observed':'Open raised circle precedes parenthesized G prime/F in both cases; all letters and parentheses checked.','status':'clear, except separately recorded extra cancelled hook at first G prime occurrence'},
{'notation':r'A^{\circ} / A^{\bullet} / A^*','meaning':'same local superscript question at final A in case 1','observed':'Closed thick loop with central aperture, no separate radial spokes.','status':'circle preferred locally; alternatives remain in first/only ambiguous occurrence'},
{'notation':r'F^A=\{B\in F\mid A\subset B\}','meaning':'set of containing figure elements','observed':'A is raised on F; braces enclose B membership F, divider, A subset B.','status':'clear except older cancelled B beneath live predicate A'},
{'notation':r'G\prime\ll F','meaning':'refinement relation as used by author','observed':'Two distinct adjacent left-facing wedges in both bottom occurrences.','status':'clear'},
{'notation':r'\mathcal R_{F\prime} / \mathscr R_{F\prime}','meaning':'cancelled relation adjective before replacement fermé dans F prime','observed':'Looped capital and low F prime; cancellation covers the join and part of following abbreviation.','status':'alphabet remains local doubt, consistent with shared-table limit'}
],
abbreviations=[
{'written':'i.e.','expansion':'id est','places':['deleted opening occurrence','live final paragraph'],'certainty':'high'},
{'written':'élémt / élt / élément','expansion':'élément if abbreviated','places':['introductory argument','case 2','cancelled attempt','restated 1'],'certainty':'unresolved spelling; do not expand in text'},
{'written':'él.','expansion':'élément','places':['case 2 plus petit él. de F'],'certainty':'high'},
{'written':'seult / seulement','expansion':'seulement if abbreviated','places':['b heading continuation'],'certainty':'unresolved spelling'},
{'written':'ens','expansion':'ensemble','places':['cancelled and restated conditions 1'],'certainty':'high; no added point'},
{'written':'str.','expansion':'not resolved','places':['lowest cancelled row'],'certainty':'low'},
{'written':'satu.','expansion':'not expanded; likely saturation adjective but only ink reading transcribed','places':['cancelled R adjective'],'certainty':'low'},
{'written':'OK','expansion':'not expanded','places':['ends of both cases'],'certainty':'high'}
],
notes=[
{'kind':'claim','text':'Part a asserts that F prime is a figure, first showing its support equals the support of F and then splitting the minimal-containing-element argument into x in support G and x outside that support.'},
{'kind':'claim','text':'Part b changes raffine to above-line subdivise. After a cancelled attempt, it restates a least-containing-element condition and a closed-intersection/union-of-strata condition.'},
{'kind':'mathematical reading limit','text':'No mathematical correctness was used to fill the page. In particular, no qui est was supplied after the doubtful le/lui word even though the resulting phrase can be grammatically awkward.'},
{'kind':'possible author slip','text':'If lui is confirmed, the literal continuation is c’est lui plus petit él. de F ...; retain it. The expected le is kept only as a glyph alternative, not imposed by syntax.'},
{'kind':'author wording','text':'The accented à in à fortiori and the two de-like groups in the cancelled lower row are retained without normalizing.'},
{'kind':'H reconstruction','text':'H’s cf. définition de F minus G and qui est before plus petit have no corresponding ink at those locations. The actual parenthesis is et à fortiori de F minus G after él. de F.'},
{'kind':'cancelled insertion attachment','text':'The slanted a un plus petit addition has its own crop and is inside the subsequently cancelled block. Its leader reaches the abbreviated élément region; precise chronology/replacement scope should remain available for main/blind adjudication.'},
{'kind':'display sign decision','text':'The isolated support equality initially invited a superset-equals doubt because of its hooked upper stroke. The b-heading equality has the same hooked two-stroke form, so = is retained. This was handwriting comparison, not a proof check.'},
{'kind':'source-state inventory','text':'All 19 C deleted scopes and all 3 C inserted scopes were explicitly audited, including the nested cancelled initial sign and the insertion cancelled again. No independent margin note, diagram, drawing or underline was found on this page.'},
{'kind':'method','text':'No OCR, automated text recognition, external research, other-page inspection or TeX compilation was used. All witness agreements were read in the two halves; crop inspections address every C/H word difference and every unresolved source-state/formula locus.'}
],
check_events=[],check_events_note='No proof check was undertaken by this reader. Whole-formula visual inspection and comparison of glyph habits are recorded as reading evidence, not mathematical verification.',
C_state_audit=states,difference_coverage=coverage,second_boxes=boxes,crop_manifest=manifest,
C_doubt_audit=[
{'place':'opening F alphabet','decision':'resolved to plain F','change':'031-02'},
{'place':'support underbraces and labels','decision':'confirmed on entire display crop; C/H agree','crop':crops['support_display']['crop']},
{'place':'cancelled relation','decision':'retained unresolved','change':'031-03'},
{'place':'all four élément words','decision':'retained unresolved','changes':['031-05','031-13','031-29','031-34']},
{'place':'case 1 G prime extra circle and exponent closing','decision':'retained unresolved; cancellations certain','changes':['031-06','031-07']},
{'place':'cancelled and overwritten B/G capitals','decision':'retained unresolved','changes':['031-08','031-11','031-12','031-33']},
{'place':'final case 1 A superscript','decision':'circle now favored; bullet/star alternatives retained','change':'031-10'},
{'place':'case 2 si x in A','decision':'retained unresolved','change':'031-14'},
{'place':'b raffine, seult, tout','decision':'retained unresolved; seult alternative seulement made explicit','changes':['031-19','031-21','031-22']},
{'place':'cancelled et, est contenu dans, slanted a un plus petit, str.','decision':'retained unresolved; H contienne included as a candidate','changes':['031-25','031-27','031-28','031-30']},
{'place':'F superscript A and set notation','decision':'confirmed on full restated formula crop; overwrite remains separately doubtful','crop':crops['restated_first']['crop']},
{'place':'G prime refinement F in bottom paragraphs','decision':'both occurrences visually confirmed as double wedges','crop':crops['bottom']['crop']},
{'place':'final R-satu adjective','decision':'retained unresolved with crop and replacement attachment','change':'031-35'},
{'place':'à fortiori accent and cancelled de de','decision':'retained as written, with crops','changes':['031-16','031-30']}
])

(OUT/'scan031_findings.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len(rows)==47 and len(coverage)==47
assert len(states)==22
assert len([s for s in states if s['C_macro'].startswith('deleted')])==19
assert len([s for s in states if s['C_macro'].startswith('inserted')])==3
assert all((ROOT/c['crop']).is_file() for c in changes)
assert all(0<=c['box'][0]<c['box'][2]<=1681 and 0<=c['box'][1]<c['box'][3]<=2360 for c in changes)
print(json.dumps({'scan':'031','changes':len(changes),'unresolved':len(unresolved),'inventory':len(inventory),'state_audit':len(states),'coverage':len(coverage),'second_boxes':len(boxes),'crops':len(manifest),'main_line_groups':len(line_ledger)},ensure_ascii=False))
