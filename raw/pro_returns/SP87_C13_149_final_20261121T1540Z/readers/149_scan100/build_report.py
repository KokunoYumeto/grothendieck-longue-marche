import json
from pathlib import Path
base=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
page=base/'readers/149_scan100'
packet=json.loads((page/'input.json').read_text())
manifest=json.loads((page/'crop_manifest.json').read_text())
draft=r"""\scanpage{100}
dégénérée. On peut passer meme à
l'hensélisé (non strict) de $\underline{\mathcal O}_s$, on
trouve la situation d'un trait hensélien
$S$, à corps résiduel $k$ (ici $\mathbf Q$ --- ou une
extension finie de $\mathbf Q$), d'une
courbe $U_\eta$ de type $(g,\nu)$ (ici, $(1,1)$)
sur son pt générique $\eta$, on s'intéresse
à l'extension $\mathcal E_{U_\eta}$ de $\mathcal E_\eta$ par $\pi$,
où ici $\mathcal E_\eta$ s'inscrit encore dans
\[
(30)\qquad 1\longrightarrow T\unsure{\longrightarrow|-}\mathcal E_\eta\longrightarrow\mathcal E_k\unsure{\longrightarrow|-}1
\]
\deleted{On est ici en \unsure{car.} $0$}
\inserted{en plus de}
\[
(31)\qquad 1-\pi-\mathcal E_{U_\eta}\longrightarrow\mathcal E_\eta\longrightarrow1
\]
Ici l'action extérieure de $T$ sur
$\pi$ n'est sûrement pas triviale (je
conjecture qu'elle l'est ssi il y
a ``bonne réduction'') --- donc le groupe
$\mathcal E_k$ n'opère pas lui $=$ extérieurement
sur $\pi$. Mais tout scindage de (30)
\margin{mais je l'ai
démontré, dans le
contexte des VA,
il y a belle
lurette ! Ça doit bien
être connu sur
$H_1$ sûrement \unsure{!!|!}}
\margin{99}
"""
(page/'draft.tex').write_text(draft)
changes=[]
def change(place,c,h,final,evidence,name,confidence='high',kind='misread word',against_c=False,against_h=True,marked=False,consequential=False):
    changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/149_scan100_{name}.png',box=manifest[name][0],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked,consequential=consequential))
change('meme','même','encore','meme','The word has two low m-shaped groups with small e returns; there is no tall or descending letter and no sequence corresponding to encore. The generous blank space above both e positions contains no detached circumflex or other accent. The unaccented written form is retained.','meme',against_c=True)
change('on','on','i.e.','on','A small closed oval is followed by one low n-shaped return. There are no dotted i, punctuation points, or separate e that would support i.e.','on')
change('trouve',r'\unsure{trouve|dans}','partir de','trouve','The initial letter has a tall stem and a separate crossbar, followed by the short r return, a small o, low joined u/v strokes and an e return. There is neither the initial d bowl of dans nor a p descender or second word de. The source phrase remains literally on trouve la situation.','trouve')
change('Q_dash','---','(nothing)','---','An independent short horizontal stroke stands between the completed Q and the beginning of ou; it is separated from the Q tail and the word entry.','Q_dash',kind='omission')
change('tuple_comma','(ici, $(1,1)$)','(ici $(1,1)$)','(ici, $(1,1)$)','After the dotted i of ici a separate low curved comma precedes the inner opening parenthesis. Both 1 digits and the internal tuple comma are visible.','tuple',kind='omission')
change('sinscrit',"s'inscrit","s'insère","s'inscrit",'After the initial s, apostrophe and dotted i, the word has the compressed n/s/c/r run and a high final crossed t; the final tall letter excludes the low re ending of insère.','sinscrit')
change('revision_cancelled',r'\deleted{On est ici en \unsure{car.} $0$}',r'\struck{\ill{} ici \ill{}}',r'\deleted{On est ici en \unsure{car.} $0$}','A long continuous strike crosses the whole baseline. Below and beside it remain the initial O loop and low n, the e/s run with tall crossed t of est, two dotted i around c in ici, the small en group, an open c followed by a/r-like low ink, and a separate closed oval 0. The strike merges the interior of car., so that abbreviation remains doubtful. The upper en plus de has its own baseline and is not crossed.','revision',confidence='medium',kind=r'readable ink left as \ill{}',marked=True,consequential=True)
change('revision_inserted',r'\inserted{en plus de}','(nothing)',r'\inserted{en plus de}','Above the cancelled line are an independent open e/n group, a descending p followed by tall l and the u/s run, and a separate d/e group. These letters sit above the long cancellation stroke and supply the live linking phrase before (31).','revision',kind='insertion or placement',consequential=True)
change('formula31_link1',r'1-\pi',r'1\to\pi',r'1-\pi','Between 1 and pi is one nearly horizontal shaft ending in a short thickened return. It has no independent upper/lower arrowhead arms, in contrast with the two explicit heads later in this same display.','formula31',kind='misread symbol or index',consequential=True)
change('formula31_link2',r'\pi-\mathcal E_{U_\eta}',r'\pi\to\mathcal E_{U_\eta}',r'\pi-\mathcal E_{U_\eta}','The second connector is likewise a plain horizontal stroke with a blunt rounded end. The later connector before E_eta has a distinct two-arm head and the final one a small separate curved head; neither feature occurs here.','formula31',kind='misread symbol or index',consequential=True)
change('surement','sûrement',r'\uncertain{évidemment}','sûrement','The word begins with a short s and low u with a detached accent above; compressed r/e/m/e/n strokes lead to a high terminal t return. There is no initial accented e followed by a d ascender as required by évidemment.','lower_claim',marked=True,consequential=True)
change('conjecture',"je conjecture qu'elle l'est ssi il y a",'pas de',"je\nconjecture qu'elle l'est ssi il y\na",'After the opening parenthesis the j has a descender. The next line has conjecture, including its descending j and crossed t, then qu’elle with two l ascenders, l’est with its tall t, the short three-letter ssi, and il y; the a begins the following line before the quotation marks. H replaces these visible words by pas de.','lower_claim',consequential=True)
change('lui_no_par',"n'opère pas lui","n'opère pas par lui","n'opère pas lui",'The high descending p of pas is followed by its low ending and then the tall loop of l in lui. The intervening gap has no second p descender or ar sequence.','lui_equal',kind='text not on the page')
change('lui_equal','lui $=$','lui-même','lui $=$','Exactly two separate horizontal parallel strokes follow lui. They form the literal equals-sign short form; no hyphen followed by the letters même is written.','lui_equal',kind='abbreviation expanded or spelling modernised')
change('final30_comma','(30)','(30),','(30)','After the 3 and rounded 0 the closing parenthesis curves downward; the blank area immediately after it contains no independent comma.','final30',kind='text not on the page')
margin=r"""\margin{mais je l'ai
démontré, dans le
contexte des VA,
il y a belle
lurette ! Ça doit bien
être connu sur
$H_1$ sûrement \unsure{!!|!}}"""
change('margin_note',r"mais je l'ai démontré, dans le contexte des VA, il y a belle lurette ! \unsure{Ça doit bien} être connu sur $H_1$ sûrement \unsure{!!}",r'\uncertain{mais} \ill{} $\subset\pi$ \ill{} \ill{} \ill{} ! \ill{} — note en oblique dans la marge inférieure gauche, non lue',margin,'After rotation by -40 degrees, the note has a consistent approximately horizontal writing direction: mais with dotted i, je with a descender, looped l and apostrophe in l’ai; démontré with a d ascender, crossed t and terminal accent; dans le; contexte with crossed t; des VA with distinct capital V and A; il y a belle with the y descender and two l loops; lurette with crossed t strokes and a separate exclamation; Ça with its cedilla, doit with tall d and crossed t, bien with the b ascender and dotted i; être, connu, sur, H with low 1, and sûrement with an accent. The apparent subset/pi in H mixes the marginal le-like trace with the differently oriented main-text pi. The final punctuation contains one clear upright stroke and several dots; a second stem is not secure, so !!|! remains open.','margin_note',confidence='medium',kind=r'readable ink left as \ill{}',marked=True,consequential=True)
change('folio99',r'\margin{99}','(nothing)',r'\margin{99}','At the lower-left paper edge are two closed upper loops, each followed by a long descending stem and lower turn: 99. Their orientation and placement are separate from the oblique marginal note.','folio99',kind='omission')
marks=[
 dict(id='M1292',decision='first',reading='trouve',evidence='Tall initial t with a visible crossbar, short r return, rounded o, low u/v run and final e; no initial d bowl. No grammatical repair is made to on trouve la situation.',crop='crops/149_scan100_trouve.png',box=manifest['trouve'][0],confidence='high'),
 dict(id='M1293',decision='first',reading='Ça doit bien',evidence='The rotated crop separates the capital C with low cedilla and a, then the tall d and crossed t of doit, followed by the b ascender and dotted i of bien. The crowded low e/n joins are consistent with this reading; the phrase is readable at medium confidence.',crop='crops/149_scan100_margin_note.png',box=manifest['margin_note'][0],confidence='medium'),
 dict(id='M1294',decision='undecided',reading=r'\unsure{!!|!}',evidence='The ending has one independent upright stem and low dots, but no securely separable second upright stem. Two exclamation marks remain possible; one cannot be excluded.',crop='crops/149_scan100_margin_note.png',box=manifest['margin_note'][0],confidence='low')
]
def inv(element,kind,position,words,hand='main authorial hand'):
 return dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes')
inventory=[
 inv('main_upper','text','top through y1211; nine prose baselines',"dégénérée. On peut passer meme à l’hensélisé"),
 inv('display30','display','middle, y1249–1415',r'(30), 1, T, E_eta, E_k, 1'),
 inv('cancelled_line','deletion','below (30), baseline around y1500',r'On est ici en \unsure{car.} 0'),
 inv('upper_replacement','insertion','above cancelled line, around y1450–1490','en plus de'),
 inv('display31','display','middle-lower, y1521–1663',r'(31), 1, pi, E_{U_eta}, E_eta, 1'),
 inv('main_lower','text','below (31), six prose baselines to the lower-right edge',"Ici l’action extérieure de T sur pi n’est sûrement pas triviale"),
 inv('diagonal_comment','margin note','lower-left diagonal note, original box [18,1790,643,2347]',"mais je l’ai démontré, dans le contexte des VA"),
 inv('folio','margin note','very bottom left, [20,2295,90,2354]','99','pagination hand; no secure distinct writer inferred')
]
spans=[
 ('meme','text','meme'),
 ('on','text','on'),
 ('trouve','text','trouve'),
 ('Q_dash','text',r'$\mathbf Q$ --- ou une'),
 ('tuple','text',r'$(g,\nu)$ (ici, $(1,1)$)'),
 ('extension','text',"l'extension"),
 ('sinscrit','text',"s'inscrit"),
 ('formula30','display',r'(30)\qquad 1\longrightarrow T\unsure{\longrightarrow|-}\mathcal E_\eta\longrightarrow\mathcal E_k\unsure{\longrightarrow|-}1'),
 ('revision','deletion and insertion',r'\deleted{On est ici en \unsure{car.} $0$}'+'\n'+r'\inserted{en plus de}'),
 ('formula31','display',r'(31)\qquad 1-\pi-\mathcal E_{U_\eta}\longrightarrow\mathcal E_\eta\longrightarrow1'),
 ('lower_claim','text',r'$\pi$ n\'est sûrement pas triviale (je'.replace("\\'", "'")+'\n'+"conjecture qu'elle l'est ssi il y\n"+"a ``bonne réduction'') --- donc le"),
 ('lui_equal','text',r"n'opère pas lui $=$ extérieurement"),
 ('final30','text','de (30)'),
 ('margin_note','margin note',margin),
 ('folio99','margin note',r'\margin{99}')
]
second=[]
for i,(name,kind,reading) in enumerate(spans,1):
 x0,y0,x1,y1=manifest[name][0]
 assert reading in draft,(name,repr(reading))
 second.append(dict(box=f'100-B{i:02d}',kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
notes=("This leaf passes to a non-strict henselian trait and places the curve-group extension (31) alongside the inertia/residue extension (30). It states that the outer action of T on pi is nontrivial here, conjectures triviality exactly in the good-reduction case, and says that E_k therefore does not itself act outwardly without further choice. The leaf ends mid-sentence after mentioning a splitting of (30). An oblique authorial note says the assertion was proved in the context of VA and should be known on H_1. These are the author's geometric assertions, not proofs supplied by this transcription. "
"Whole source and both supplied full-resolution halves were each viewed once; every main-text line, including words on which C and H agree, was compared directly with the ink. Fifteen unique crops were inspected once for decisions; no decided place was recropped. Each crop is autocontrasted, LANCZOS-upscaled to 2200 pixels wide and lightly sharpened. The margin crop alone is rotated by -40 degrees; its reported box is in the original unrotated page. "
"Line count 27 comprises 18 main baselines (15 prose, two displays, one deleted line), one separate interlinear replacement, seven approximately diagonal note rows, and the isolated folio 99. The words Ça doit bien bend across the crowded fifth marginal row; source line breaks are represented where feasible. The note intersects differently oriented main-text strokes; these are not separate marginal symbols. "
"The accent is absent from meme, whereas detached accent strokes occur in sûrement; neither expected spelling nor witness agreement supplies missing ink. The source reads on trouve la situation without se or dans. The dense crossings in extension are the x/t letter structure and retracing; no independently cancelled underlying word is recoverable. The struck car. stays doubtful because the strike merges its inner letters. In (30), the first and third links have distinct heads; the second and fourth have tiny hooked endpoints, so arrow is retained only as the preferred alternative to a plain shaft. In (31), the first two links are plain shafts and the final two have heads. The short form lui = is preserved. The final (30) has no following comma. "
"M1292 is resolved to trouve; M1293 is read Ça doit bien at medium confidence; M1294 remains !!|! at low confidence. C's car. doubt is not a supplied MARKS item and is recorded only below. Pure scan macros, conventional E/O/Q font encodings, quotation typography, and the em-dash/TeX-hyphen tokenizer mismatch are not collation changes. No OCR, outside research, other-page witnesses, or TeX compilation were used.")
check_events=[
 dict(statement_id='149.100.outer-action-descent',type='targeted proof check',who='reader A (/root/reader_a)',outcome="Conditional group-theoretic proof performed from the two displayed extensions: because pi is normal in E_{U_eta}, conjugation by a lift of e in E_eta gives an automorphism of pi. Replacing a lift x by a*x, with a in pi, changes the automorphism by an inner automorphism, so its class rho(e) in Out(pi) is well-defined; products of lifts show rho is a homomorphism. Write q:E_eta→E_k for the quotient in (30). If rho factors through q then every t in T has rho(t)=1. Conversely, if rho(T)=1, set bar-rho(q(e))=rho(e); two representatives differ by T and give the same value, so this is a well-defined unique homomorphism. Thus nontrivial rho|T prevents descent to E_k. Given a splitting s:E_k→E_eta, rho∘s is an outer action after that choice. This checks the abstract group-theoretic implication used in the prose, not the geometric assertion that rho|T is nontrivial; topological continuity is not separately proved. No omitted continuation after Mais tout scindage is supplied."),
 dict(statement_id='149.100.geometric-inertia-criterion',type='carried as background without fault found',who='reader A (/root/reader_a)',outcome="The page asserts nontrivial outer inertia in the stated degeneration and explicitly labels the good-reduction equivalence a conjecture. Neither geometric assertion is proved by the material on this leaf or by the formal quotient check; both remain authorial/background claims in this run."),
 dict(statement_id='149.100.marginal-VA-H1-claim',type='carried as background without fault found',who='reader A (/root/reader_a)',outcome="The author says in the margin that he had proved the claim in the context of VA and that it should be known on H_1. No proof or reference is supplied on this leaf; this note records the author's qualification without upgrading it to an independently checked theorem.")
]
hand_observations=[
 dict(habit='An expected French accent can be absent even when the same page supplies accents elsewhere.',pages='100',evidence='meme crop has blank space above the two e positions; main and marginal sûrement have detached accent strokes.',witness_errors='C supplies the circumflex in même; H changes the entire word to encore.'),
 dict(habit='A long final t may end a very compressed cursive word.',pages='100',evidence='sinscrit crop has a high final crossed return after the compressed scri run; trouve has a tall initial crossed t.',witness_errors="H reads s’insère and partir de; the first loses the terminal t and the second supplies an absent word."),
 dict(habit='Long connectors can be plain shafts or have very small terminal hooks; heads must be judged locally.',pages='100',evidence='formula31 first two ends are blunt; its final two are headed. formula30 second/final ends have only tiny downturned hooks.',witness_errors='H turns both first links of (31) into arrows; C and H both print definite arrows for two less certain links in (30).'),
 dict(habit='Oblique notes can bend individual words around main-text strokes.',pages='100',evidence='After rotation, the VA note has seven writing rows, while nearby pi and other main-text letters retain a different diagonal direction; Ça doit bien changes height locally.',witness_errors='H leaves nearly all the note unread and treats an intersecting pi as part of a marginal subset/pi expression.')
]
notation_additions=[dict(written='meme without an independent accent',transcription='meme',evidence='149_scan100_meme crop: the area above the word is blank; retain the written absence of the circumflex. No general spelling replacement is inferred.')]
abbreviations=[
 dict(form='pt',expansion='point'),dict(form='ssi',expansion='si et seulement si'),
 dict(form='=',expansion='même, in lui ='),dict(form='VA',expansion='variétés abéliennes (contextual expansion; not inserted into the diplomatic text)'),
 dict(form='car.',expansion='caractéristique (the struck abbreviated reading itself remains uncertain)')
]
unresolved=[
 dict(place='formula30_second_and_final_links',reading=r'\unsure{\longrightarrow|-}',alternatives='A small arrowhead versus a plain shaft ending in a pen return, separately at T–E_eta and E_k–1.',confidence='medium'),
 dict(place='revision_cancelled_car',reading=r'\unsure{car.}',alternatives='car. preferred; the cancellation prevents secure separation of the inner a/r and abbreviation point. No expanded form is supplied.',confidence='low'),
 dict(place='margin_note_ending',reading=r'\unsure{!!|!}',alternatives='Two exclamation marks or one; at least one upright stem is visible, but the additional low dots do not securely establish a second stem.',confidence='low')
]
coverage=[]
def cov(d,place=None,reason=''):
 coverage.append(dict(diff_id=d,disposition='substantive' if place else 'macro/editorial only',change_place=place or '',reason=reason))
cov('D0517',reason='The scanpage{100} metadata macro is not an additional source numeral; actual lower folio 99 is treated separately.')
cov('D0518','meme','The literal word has no visible circumflex; C changes its spelling and H changes its lexical identity.')
cov('D0519','on','This row spans two source lines and two unique crops: on and trouve. Both are recorded as separate change places.')
cov('D0520','Q_dash','An independent source dash after Q is omitted in H.')
cov('D0521','tuple_comma','The source has a comma after ici.')
cov('D0522','sinscrit','The high final t supports inscrit rather than insère.')
cov('D0523','revision_cancelled','On est is recoverable within the cancelled line; H leaves it illegible.')
cov('D0524','revision_cancelled','The cancelled continuation en car. 0 and the live upper replacement en plus de are both present; the replacement is separately recorded at revision_inserted.')
cov('D0525','formula31_link1','The first link in (31) is a plain shaft.')
cov('D0526','formula31_link2','The second link in (31) is a plain shaft.')
cov('D0527','surement','The visible word is sûrement, not H’s uncertain évidemment.')
cov('D0528','conjecture','H replaces a full explicit conjecture clause with pas de.')
cov('D0529',reason='Both witnesses have the same word réduction and closing quotation marks; TeX paired apostrophes versus guillemets is quotation encoding. The source double strokes are transcribed by the agreed double-quote convention.')
cov('D0530',reason='The full H witness already contains an em dash in this position. The difference row is a tokenizer mismatch between TeX hyphens and an em dash, not an omitted source mark.')
cov('D0531','lui_no_par','No independent par occurs between pas and lui.')
cov('D0532','lui_equal','The written equals sign is retained as a short form rather than expanded to même.')
cov('D0533','final30_comma','No comma follows the closing parenthesis of the final (30).')
cov('D0534','margin_note','The oblique note reads mais je l’ai démontré; H’s subset/pi expression and unread-note description do not give the source text.')
cov('D0535','margin_note','The rest of the note is read with the final punctuation left doubtful. The separate folio99 change also falls within this aggregated difference row; H’s non lue is an editorial description.')
report=dict(scan=100,line_count=27,changes=changes,marks=marks,inventory=inventory,second_boxes=second,notes=notes,check_events=check_events,hand_observations=hand_observations,notation_additions=notation_additions,abbreviations=abbreviations,unresolved=unresolved,diff_coverage=coverage)
(page/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert {d['diff_id'] for d in coverage}=={d['diff_id'] for d in packet['differences']}
assert {m['id'] for m in marks}=={m['id'] for m in packet['marks']}
assert all((base/x['crop']).is_file() for x in changes+marks)
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(c['kind'] in allowed for c in changes)
assert draft.count('{')==draft.count('}')
print(json.dumps({'changes':len(changes),'against_C':sum(c['against_c'] for c in changes),'against_H':sum(c['against_h'] for c in changes),'marks':len(marks),'diffs':len(coverage),'substantive_diff_rows':sum(d['disposition']=='substantive' for d in coverage),'inventory':len(inventory),'second_boxes':len(second),'crops':len(manifest),'line_count':report['line_count'],'unresolved':len(unresolved)},ensure_ascii=False))
