import json
from pathlib import Path

ROOT=Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
PAGE='150_scan090'
packet=json.loads(Path('/workspace/scratch/d7279cb02214/reading_packets/150_scan090/packet.json').read_text())
rows=json.loads((ROOT/'records'/f'{PAGE}_cropmap.json').read_text())
cm={r[0]:r for r in rows}
changes=[]
def change(cid,place,C,H,final,evidence,crop,confidence,kind,error,ac=False,ah=False,con=False,mh=False,change_type=None):
    d=dict(id=cid,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/{PAGE}_{crop}.png',box=cm[crop][1],confidence=confidence,kind=kind,error_kind=str(error),against_C=ac,against_H=ah,consequential=con,marked_in_H=mh)
    if change_type:d['change_type']=change_type
    changes.append(d)

change('C01','Opening On dit: H duplicates a marginal formula tail',
       'On dit aussi',r'On dit \add{(\ill{} $j\le i\le k$)} aussi','On dit aussi',
       'The slanting tels que and j<=i<=k continue the single oblique formula (84) from the lower left. Their baseline cuts across the horizontal On dit area; there is no separate parenthesized insertion attached to On dit. H gives this tail both here and in its marginal formula.',
       'margin_tail','high','text not on the page',9,ah=True,mh=True)
change('C02','Opening aussi alors,',
       'aussi alors,','aussi, dans ce cas,','aussi alors,',
       'One reduced word follows aussi: a low initial run rises into a tall l, followed by the low ors group and a distinct comma. There are no separate dans, ce or cas words and no comma between aussi and alors.',
       'alors','high','misread word',2,ah=True)
change('C03','Short underline beneath the initial C of C\'est',
       "C'est",r"\emph{C'est}",r"\uline{C}'est",
       'A short independent horizontal stroke lies below C, separated from the C\'s own lower return. It stops before the apostrophe and est. C omits it; H emphasizes the whole word. The candidate restricts the underline to C.',
       'property_revision','high','other',10,ac=True,ah=True)
change('C04','Raised live une in the C\'est revision',
       'une propriété sym.',r'\add{\ill{}} \ill{}',r'\inserted{une} propriété sym.',
       'The live low u-n-e run is raised above the crossed old phrase, with a clear gap above the heavy strike. Propriété continues to its right on the surrounding main line. The insertion scope is une, not the entire following phrase.',
       'property_inner','high','insertion or placement',6,ac=True,ah=True,mh=True)
change('C05','Live propriété sym. after the raised article',
       'propriété sym.',r'\ill{}','propriété sym.',
       'The live word has descending p strokes, the dotted i, and the accented terminal té; the following sym. has a long y descender, low m and a separate stop. The crossed material to the left is not used to supply this live reading.',
       'property_revision','high',r'readable ink left as \ill{}',5,ah=True,mh=True)
change('C06','Canceled item after La plus petite bande contenant J est',
       r'\deleted{\unsure{notée}}',r'\struck{$\overline J\cap\widetilde J$}',
       r'$\deleted{\unsure{\bar J}\cap\widetilde J}$',
       'The raised terminal item is mathematical: an arch-shaped intersection sign and an angular J with a separate tilde remain visible under the strike. The first barred J is heavily overwritten and is kept narrowly uncertain. The visible tilde and second J exclude the word notée.',
       'bandes_parties','medium','misread symbol or index',1,ac=True,con=True)
change('C07','State of the two-line Toute intersection addition',
       r'\inserted{Toute intersection de bandes est une bande. La plus petite bande contenant $J$ est',
       'Toute intersection de bandes est une bande. La plus petite bande contenant $J$ est',
       r'\inserted{Toute intersection de bandes est une bande. La plus petite bande contenant $J$ est',
       'The two lines are smaller and crowded into the interline space between the C\'est sentence and Soient J,K. A brace-like leader at their left connects this added sentence to the oblique marginal formula. H transcribes the prose as ordinary main text.',
       'insertion_band','high','insertion or placement',6,ah=True)
change('C08','Position and attachment of formula (84)',
       packet['witness_C'][packet['witness_C'].index('\\[\n(84)'):packet['witness_C'].index('\\]}')+2],
       r'\marginal{(84) $\overline J\cap\widetilde J=\lbrace i\in I\mid \exists j,k\in J,\ j\le i\le k\rbrace\overset{\text{déf}}{=}B(J)$}',
       r'\margin{$\displaystyle(84)\quad\underbrace{\bar J\cap\widetilde J}_{\substack{\Vert\,\mathrm{déf}\\B(J)}}=\{i\in I\mid\exists j,k\in J\text{ tels que }j\leq i\leq k\}$}',
       'The number and formula run obliquely upward along the left margin. A large brace-like leader points to the small inserted sentence ending contenant J est. The tail passes the horizontal On dit line without becoming a separate insertion there. C\'s main-body display does not preserve this marginal status.',
       'margin84','high','insertion or placement',6,ac=True)
change('C09','Formula (84), vertical definition annotation below the first term',
       r'\underbrace{\bar J\cap\widetilde J}_{\substack{\Vert\,\mathrm{déf}\\B(J)}}',
       r'\lbrace i\in I\mid \exists j,k\in J,\ j\le i\le k\rbrace\overset{\text{déf}}{=}B(J)',
       r'\underbrace{\bar J\cap\widetilde J}_{\substack{\Vert\,\mathrm{déf}\\B(J)}}',
       'The underbrace lies beneath the first bar-J intersection tilde-J term. Directly below it are two upright parallel strokes with déf to their right; B(J) occupies the row underneath. H relocates this definition as a horizontal equals at the right end of the set expression.',
       'margin84','high','insertion or placement',6,ah=True)
change('C10','Formula (84), words before the marginal inequality',
       r'\exists j,k\in J\quad j\leq i\leq k',
       r'\exists j,k\in J,\ j\le i\le k',
       r'\exists j,k\in J\text{ tels que }j\leq i\leq k',
       'After the J-membership condition, the rotated crop shows tall t, low e, tall l and terminal s, then q with a long descending stroke followed by low u/e. Que crosses the canceled opening word of the main line but belongs to the oblique formula. Both marginal witnesses omit the words tels que.',
       'margin_tail','high','omission',3,ac=True,ah=True,mh=True)
change('C11','H extra illegible span after the canceled mathematical item',
       r'\deleted{\unsure{notée}}',
       r'\struck{$\overline J\cap\widetilde J$} \ill{}.',
       r'$\deleted{\unsure{\bar J}\cap\widetilde J}$',
       'The strike through the mathematical item terminates in white space; the nearby lower live word is parties, replacing bandes in the next main line. No additional word or separate final point follows the crossed mathematical item at the end of the small addition.',
       'insertion_band','high','text not on the page',9,ah=True,mh=True)
change('C12','Unstopped ens before the powerset symbol',
       "l'ens",r"l'ens.\ ", "l'ens",
       'The low ending of ens turns down and is followed by clear white space before the script P. There is no separate period. H adds a stop to this abbreviation.',
       'ens_P','high','abbreviation expanded or spelling modernised',8,ah=True)
change('C13','Unstopped L\'ens at start of quotient sentence',
       "L'ens",r"L'ens.\ ", "L'ens",
       'The first abbreviation ends in a reduced terminal return before ordonné. No independent dot follows it.',
       'ens_quotient','high','abbreviation expanded or spelling modernised',8,ah=True)
change('C14','Unstopped l\'ens before des bandes',
       "l'ens",r"l'ens.\ ", "l'ens",
       'The second ens in this line has a continuous low final stroke, then blank paper before des. No stop is present.',
       'ens_quotient','high','abbreviation expanded or spelling modernised',8,ah=True)
change('C15','Canceled l\'inclusion before domination',
       r"\deleted{\unsure{l'inclusion}}",r'\struck{\ill{}}',r"\deleted{\unsure{l'inclusion}}",
       'The canceled run retains an initial upright and dotted short stroke, low joined middle strokes and a terminal return. These permit C\'s narrow l\'inclusion candidate, but the strike merges with the middle letters and with the raised replacement. Every letter is not plain, so the doubt remains.',
       'canceled_inclusion','low',r'readable ink left as \ill{}',5,ah=True,mh=True)
change('C16','Raised replacement domination in the quotient sentence',
       'domination.', 'domination.', r'\inserted{domination}.',
       'The live d starts above the right-hand part of the crossed old word, before its strike ends. The remaining omination continues along the raised line to the right. The live word replaces the canceled term and is therefore marked as an insertion.',
       'canceled_inclusion','high','insertion or placement',6,ac=True,ah=True)
change('C17','Lower transition: enfin before canceled et',
       r'enfin \deleted{\unsure{et}}',r'\struck{et} en fait',r'enfin \deleted{\unsure{et}}',
       'The live left-hand word is a single connected en-fin: a tall f descender and a detached i dot occur in its second part. It precedes the centered crossed et. H changes the word to en fait and moves the cancellation before it. The canceled et itself remains narrowly uncertain.',
       'enfin_canceled_et','high','misread word',2,ah=True)
change('C18','Punctuation after K est ouvert dans I\'',
       r"$K$ est ouvert dans $I'$ enfin",r"$K$ est ouvert dans $I'$, \struck{et} en fait",
       r"$K$ est ouvert dans $I'$ enfin",
       'The prime of I\' is the last ink at the right end of this line. There is no comma after it; the next line begins enfin.',
       'formula87','high','text not on the page',9,ah=True)
change('C19','Lower first relation between I\' and bar K',
       r"I'\subset\bar K",r"I'=\overline K",r"I'\unsure{\subset|=}\bar K",
       'The two heavy horizontal arms have a substantial connected left curve, favoring subset. The same page\'s prose = has a left pen return, so the connection alone does not securely exclude an equals written continuously. Keep the ambiguity narrow, with subset first; no mathematical expectation is used to force the glyph.',
       'dense_sign','medium','misread symbol or index',1,ah=True,con=True,mh=True)
change('C20','Second lower canceled et, before the second i.e.',
       r'\deleted{\unsure{et}}',r'\struck{\ill{}}',r'\deleted{\unsure{et}}',
       'A looped initial stroke and an upright/crossing stroke remain at the start of the crossed short run. They permit et as a narrow candidate, but the long crossing stroke obscures its complete outline. The C doubt is not resolved.',
       'dense_formula','medium',r'readable ink left as \ill{}',5,ah=True,mh=True)
change('C21','Prose sign in on a = égalité!',
       r'on a $=$',r'on a \ill{}',r'on a $=$',
       'Two short parallel horizontal strokes are written between a and égalité. A small left return belongs to the pen motion. The sign is the prose abbreviation =; it is not an illegible word.',
       'egalite','high',r'readable ink left as \ill{}',5,ah=True,mh=True)
change('C22','Alleged underline of égalité',
       r'\uline{égalité}', 'égalité', 'égalité',
       'The low horizontal stroke is continuously joined to the descending stem of g and turns back left as that letter\'s foot. No independent underline exists under the word. C has counted the g descender as an underline.',
       'egalite','high','other',10,ac=True)
change('C23','Inversement clause, tel que',
       'tel que', 'telle que', 'tel que',
       'The word has one t, a low e transition and one tall l arch. It ends before the q of que; there is no second l or final e. The written agreement is preserved.',
       'tel','high','misread word',2,ah=True)
change('C24','Final phrase, ainsi',
       r'\unsure{ainsi|on a}', 'on a', 'ainsi',
       'One connected low word has an initial a-like loop, compressed internal strokes and a detached i dot. It contains no word gap separating on and a. The tail is distinct from the following comma. M0715 resolves to its first reading.',
       'ainsi_detail','high','misread word',2,ac=True,ah=True)
change('C25','Comma after final ainsi',
       r"\unsure{ainsi|on a} $I'=",r"on a $I'=",r"ainsi, $I'=",
       'A separate curved mark follows the word: its dark head is high at the right and its long tail descends toward the left. It is detached from the final letter and precedes I\'. Both witnesses omit this comma.',
       'ainsi_detail','high','omission',3,ac=True,ah=True)
change('C26','Thin lower-left foliation',r'\margin{89}','',r'\margin{89}',
       'The lower left has a thin grey 8 with two loops, followed by a looped 9 with a long descending tail. It is another hand\'s foliation, not an authorial page number; H omits it.',
       'folio89','high','omission',3,ah=True)
change('C27','Opening canceled word after que',
       r'\deleted{\unsure{pour}}',r'\struck{\ill{}}',r'\deleted{\unsure{pour}}',
       'The crossed baseline preserves a looped beginning and low connected run, but the heavy strike and the crossing marginal que make the individual letters insecure. C\'s pour is retained only as a narrow low-confidence candidate; this is not a resolution of the struck doubt.',
       'canceled_pour','low',r'readable ink left as \ill{}',5,ah=True,mh=True)
change('C28','Old canceled phrase after C\'est',
       r'\deleted{\unsure{une propriété}}',r'\struck{\ill{} \ill{}}',r'\deleted{\unsure{une propriété}}',
       'The old line is crossed very heavily. Low joined remnants and several projecting uprights remain, while the raised live une and live propriété are distinguishable by level. The old phrase is not fully legible: C\'s candidate is retained under a single narrow doubt rather than promoted to certainty.',
       'property_inner','low',r'readable ink left as \ill{}',5,ah=True,mh=True)

# This punctuation decision was made on the native lower half; formula87's crop
# includes only the top of the following line, so it is not cited as full evidence.
for row in changes:
    if row['id']=='C18':
        row['crop']=None
        row['box']=None
        row['source_half']='half2.png; right end of first prose line below (87)'

spec={
'D0451':('editorial-only',[],'Scan marker and H\'s introductory editorial folio note are not manuscript text; no authorial top number is present.'),
'D0452':('reading',['C27'],'The opening canceled candidate remains doubtful; the crop and overlap with marginal que are recorded.'),
'D0453':('reading',['C01','C10'],'H misassigns the tail of the oblique marginal formula to On dit. Its words are recovered in the one correct formula location.'),
'D0454':('reading',['C02'],'The manuscript has one alors followed by a comma, not dans ce cas.'),
'D0455':('reading',['C03','C04','C05','C28'],'Recover the live raised une and propriété sym.; keep the old crossed phrase doubtful and restrict the underline to C.'),
'D0456':('reading',['C06','C08','C11'],'The canceled item is mathematical, not notée; formula84 is marginal, and H\'s extra illegible word after the cancellation is unsupported.'),
'D0457':('reading',['C06','C08','C09','C10'],'The alignment conflates the canceled interline formula with the separate live marginal formula. Preserve the live formula once, its vertical definition stack, and tels que.'),
'D0458':('reading',['C12'],'The first ens has no stop.'),
'D0459':('macro-only',[],'Aligned environment versus a one-line formula layout; same mathematical text.'),
'D0460':('macro-only',[],'Aligned environment end; no distinct ink.'),
'D0461':('reading',['C13'],'Initial L\'ens in the quotient sentence is unstopped.'),
'D0462':('reading',['C14'],'Second l\'ens in that sentence is unstopped.'),
'D0463':('reading',['C15','C16'],'Keep the old canceled l\'inclusion candidate doubtful and mark the raised live domination as replacement.'),
'D0464':('reading',['C07','C08','C09','C10'],'H places its marginal transcription later in reading order; the source leader attaches it to the upper inserted sentence. H\'s explanatory note is editorial. Formula content and placement are logged at their actual sites.'),
'D0465':('macro-only',[],'Aligned environment versus one-line layout for (87); the actual two writing rows are retained.'),
'D0466':('macro-only',[],'Aligned environment terminator, no textual difference.'),
'D0467':('reading',['C17','C18'],'Live enfin begins the next line; no comma follows preceding I\'.'),
'D0468':('reading',['C17'],'The word is enfin and precedes the canceled et; H has en fait after it.'),
'D0469':('reading',['C19'],'The heavy connected sign favors subset but remains narrowly ambiguous with equals; only the glyph is transcribed, without a proof-driven correction.'),
'D0470':('reading',['C20'],'The short canceled et candidate remains uncertain where H leaves an illegible span.'),
'D0471':('reading',['C21'],'The prose = sign is readable.'),
'D0472':('macro-only',[],'H\'s tokenized comma is the TeX thin-space command before the exclamation point; no punctuation comma is being claimed.'),
'D0473':('reading',['C23'],'Only tel is written, with one l and no final e.'),
'D0474':('reading',['C24','C25'],'Resolve the supplied C choice to ainsi and preserve the separately written comma.'),
'D0475':('reading',['C26'],'Preserve the other-hand foliation89. H\'s final editorial discussion of the dense sign is excluded as source text.'),
}
coverage=[dict(diff_id=d['diff_id'],classification=spec[d['diff_id']][0],change_ids=spec[d['diff_id']][1],reason=spec[d['diff_id']][2]) for d in packet['differences']]

decisions=[dict(id='M0715',cote='150',scan='90',decision='first',reading='ainsi',ink='A single connected low word with a detached i dot; no on/a word gap. A separate comma follows. The first C reading is supported on the tight crop.',crop=f'crops/{PAGE}_ainsi_detail.png',box=cm['ainsi_detail'][1],confidence='high')]

def inv(element,kind,pos,words,hand='author'):
    return dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=pos,first_words_or_objects=words,transcribed='yes')
inventory=[
inv('Opening continuation and convexity condition','text','Top two main lines, x275–1645 y35–245',r'que ... (j,k in J et j<=i<=k) => i in J'),
inv('Opening crossed word','deletion','After que, x410–550 y40–150, crossed also by the separate marginal formula tail',r'\unsure{pour}'),
inv('Symmetry sentence with short underline under C','text','Third main line, x275–1640 y260–370',r"\uline{C}'est ... propriété sym. par passage de I à I^circ"),
inv('Old crossed phrase in symmetry sentence','deletion','Approximately x405–615 y300–350',r'\unsure{une propriété}'),
inv('Raised replacement article','insertion','Above crossed old phrase, approximately x445–540 y295–320','une'),
inv('Two-line added band-hull prose','insertion','Small writing between third and fourth main lines, x285–1630 y300–410','Toute intersection de bandes est une bande. La plus petite bande contenant J est'),
inv('Canceled mathematical ending of added prose','deletion','Approximately x865–1040 y325–370, above parties',r'\unsure{\bar J}\cap\widetilde J'),
inv('Oblique marginal formula and brace-like attachment','margin note','Left margin x15–565 y30–650, rising approximately44 degrees; leader beside upper inserted prose',r'(84) barJ cap tildeJ = {i in I | exists j,k in J tels que j<=i<=k}; vertical Vert déf and B(J) under first term'),
inv('Soient paragraph introducing domination','text','Main line around y380–420','Soient J,K deux ... de I, on écrit'),
inv('Canceled original bandes','deletion','x890–1045 y380–415',r'\unsure{bandes}'),
inv('Live replacement parties','insertion','Raised above canceled bandes, x905–1055 y355–390','parties'),
inv('Definition of domination','display','x225–1500 y440–595, label85 left',r'(85) J prec K iff J subset barK, K subset tildeJ'),
inv('Preorder and equivalence introduction','text','Three lines between85 and86, approximately x275–1560 y600–850','(relation de domination). C\'est une relation de préordre'),
inv('Equivalence formula with two lower labels','display','x245–1475 y815–1085, two main rows with B(K),B(J) under first row',r'(86) J sim K iff ... iff B(J)=B(K)'),
inv('Ordered quotient paragraph','text','Two lines x280–1600 y1095–1290',"L'ens ordonné quotient est l'ens des bandes de I"),
inv('Canceled old quotient relation term','deletion','x1125–1260 y1220–1260',r"\unsure{l'inclusion}"),
inv('Raised replacement relation term','insertion','Starts above right part of crossed old term, approximately x1200–1490 y1195–1245','domination'),
inv('Supposition for two bands','text','Three main lines x280–1630 y1300–1600','Supposons maintenant que J et K soient des bandes'),
inv('Added domination hypothesis and leader','insertion','x765–1100 y1320–1470; leader curves down to gap after bandes, before soit',r'avec J prec K,'),
inv('Generated band display','display','x265–1625 y1550–1755, two rows and left87 label',r'(87) I\prime={i in I | exists j in J,k in K t.q. j<=i<=k}=tildeJ cap barK'),
inv('Closed/open dense/codense paragraph and converse','text','Seven lower main lines, x270–1635 y1730–2345',r'et J est fermé dans I\prime, K est ouvert dans I\prime ... et ainsi, I\prime=tildeJ cap barK.'),
inv('First canceled lower et','deletion','After enfin and before K, approximately x620–680 y1865–1935',r'\unsure{et}'),
inv('Second canceled lower et','deletion','After I\prime subset tildeJ, approximately x1420–1525 y1930–1990',r'\unsure{et}'),
inv('Other-hand lower foliation','margin note','x20–105 y2285–2358','89','another hand; thin grey later foliation'),
]

def rev(item,state,bounds,attachment,crop):
    return dict(C_item=item,state=state,bounds=bounds,attachment=attachment,crop=f'crops/{PAGE}_{crop}.png',box=cm[crop][1])
revisions=[
rev(r'\deleted{\unsure{pour}}','canceled; narrow doubt retained','Heavy crossing stroke across short word after que; the diagonal que of formula84 also crosses this zone.','Opening main sentence; not part of the marginal formula.','canceled_pour'),
rev(r'\deleted{\unsure{une propriété}}','old phrase canceled; not securely resolved','Thick stroke crosses old baseline after C\'est; raised une remains above it and live propriété extends right.','Replacement has raised une and the following live property phrase.','property_inner'),
rev('une propriété sym.','une is a live raised insertion; propriété sym. live on continuation','Raised une occupies the space over the old cancellation.','Article replaces old wording after C\'est; only une receives insertion macro.','property_revision'),
rev(r'\inserted{Toute intersection ... (84) ...}','two-line prose insertion, with separately marginal attached formula','Small interline prose ends at the crossed mathematical item. Formula84 is not a main-body display.','Brace-like leader at left links the marginal formula to La plus petite bande contenant J est.','insertion_band'),
rev(r'\deleted{\unsure{notée}}',r'canceled mathematics: \unsure{\bar J}\cap\widetilde J','Separate upper strike, above parties; tilde and last J remain clear.','Canceled ending of the added contenant J est sentence, replaced by the larger marginal definition.','bandes_parties'),
rev(r'\deleted{\unsure{bandes}}','canceled old word; doubt retained','Lower strike through tall b, reduced middle and ending; distinct from the cancellation above.','Replaced by parties above it in Soient J,K deux ...','bandes_parties'),
rev(r'\inserted{parties}','live insertion','Raised p descender, dotted i and terminal es are visible between the two canceled levels.','Replaces bandes after deux.','bandes_parties'),
rev(r"\deleted{\unsure{l'inclusion}}",'canceled old word; doubt retained','Strike crosses the old low word after de.','Live domination begins above its right part and is marked inserted.','canceled_inclusion'),
rev('domination','live raised replacement','The d starts before the old strike ends, on a higher baseline; the remainder continues right.','Replaces canceled l\'inclusion in relation de ...','canceled_inclusion'),
rev(r'\inserted{avec $J\prec K$,}','live insertion with curved leader','Small phrase sits above soit; long lower rule curves down at left. It is not struck.','After bandes, before soit I\prime; comma follows K.','avec_insertion'),
rev(r'\deleted{\unsure{et}} (first)','canceled; narrow doubt retained','Centered short crossed form after the live word enfin.','Before K est dense, not before enfin.','enfin_canceled_et'),
rev(r'\deleted{\unsure{et}} (second)','canceled; narrow doubt retained','Small crossed run follows the second lower condition I\prime subset tildeJ.','Immediately before second i.e.','dense_formula'),
]

opening=r"que \deleted{\unsure{pour}} $(j,k\in J\text{ et }j\leq i\leq k)\Longrightarrow i\in J$. On dit aussi alors, que $J$ est une \uline{bande} de $I$."
property_text=r"\uline{C}'est \deleted{\unsure{une propriété}} \inserted{une} propriété sym. par passage de $I$ à $I^\circ$."
insertion=r'\inserted{Toute intersection de bandes est une bande. La plus petite bande contenant $J$ est $\deleted{\unsure{\bar J}\cap\widetilde J}$}'
margin84=r'\margin{$\displaystyle(84)\quad\underbrace{\bar J\cap\widetilde J}_{\substack{\Vert\,\mathrm{déf}\\B(J)}}=\{i\in I\mid\exists j,k\in J\text{ tels que }j\leq i\leq k\}$}'
formula85=r'(85)\qquad J\prec K\quad\overset{\mathrm{déf}}{\Longleftrightarrow}\quad J\subset\bar K,\ K\subset\widetilde J'
formula86=r'''(86)\qquad\begin{aligned}
J\sim K&\Longleftrightarrow J\subset\underbrace{\bar K\cap\widetilde K}_{B(K)},\ K\subset\underbrace{\bar J\cap\widetilde J}_{B(J)}\\
&\Longleftrightarrow B(J)=B(K)
\end{aligned}'''
formula87=r'''(87\unsure{)|]}\qquad\begin{aligned}
I'&=\{i\in I\mid\exists j\in J,k\in K\text{ t.q. }j\leq i\leq k\}\\
&=\widetilde J\cap\bar K
\end{aligned}'''
boxespec=[
('B01','Opening formula, cancellation and differing alors phrase',[275,35,1645,245],opening),
('B02','Full symmetry sentence: short underline, cancellation and raised article',[275,260,1640,370],property_text),
('B03','Whole two-line addition and its canceled mathematical ending',[285,300,1630,410],insertion),
('B04','Whole oblique marginal formula84, number, words and vertical definition stack',[15,30,565,650],margin84),
('B05','Lower revision within Soient: canceled bandes and live parties',[860,325,1070,420],r'\deleted{\unsure{bandes}} \inserted{parties}'),
('B06','Whole numbered formula85',[225,440,1500,595],formula85),
('B07','Unstopped ens and script powerset P',[625,665,1000,780],r"l'ens $\mathcal P(I)$"),
('B08','Whole numbered formula86 and B labels',[245,815,1475,1085],formula86),
('B09','Both quotient-line ens short forms and underline of bandes',[280,1095,1600,1205],r"L'ens ordonné quotient est l'ens des \uline{bandes} de"),
('B10','Canceled l\'inclusion and raised replacement domination',[1050,1190,1505,1270],r"de \deleted{\unsure{l'inclusion}} \inserted{domination}."),
('B11','Inserted hypothesis and curved attachment',[765,1320,1100,1470],r'\inserted{avec $J\prec K$,}'),
('B12','Whole formula87, number and doubtful closing delimiter, abbreviation stops',[265,1550,1625,1755],formula87),
('B13','Enfin and the first canceled lower et',[270,1830,825,1965],r'enfin \deleted{\unsure{et}} $K$'),
('B14','Whole lower ambiguous relation and neighboring condition, canceled et and i.e.',[810,1900,1635,2025],r"$I'\unsure{\subset|=}\bar K$ et $I'\subset\widetilde J$ \deleted{\unsure{et}} i.e."),
('B15','Prose equals abbreviation and g descender in égalité',[625,2010,1200,2140],r'(on a $=$ égalité!)'),
('B16','Written tel que',[755,2120,1035,2240],'tel que'),
('B17','Final ainsi, comma and concluding formula',[1010,2220,1635,2345],r"et ainsi, $I'=\widetilde J\cap\bar K$."),
('B18','Other-hand foliation89',[20,2285,105,2358],r'\margin{89}'),
]
second_boxes=[dict(box=n,kind=k,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=t) for n,k,b,t in boxespec]

notes=r'''## Content
The leaf continues the condition that a subset J of an ordered I contain every i lying between j,k in J, and calls such a subset a bande. It says this is symmetric under passage from I to I^circ. An added sentence says intersections of bands are bands and supplies the smallest band containing J. Its definition (84) is written obliquely in the left margin, attached by a brace-like leader to that sentence.

Definition (85) introduces domination J prec K by J subset bar K and K subset tilde J. The next text calls this a preorder on the collection of subsets. Formula (86) describes the associated equivalence by mutual containment in the band hulls and by B(J)=B(K); the quotient is identified with bands ordered by domination. The lower paragraph assumes J,K are bands with J prec K and gives (87) for the band they generate. It asserts closed/codense and open/dense properties in I', followed by a converse and the final formula I'=tilde J cap bar K.

## Formula rereading and mathematical limits
Every formula, not only disputed signs, was reread on the native halves. Formula84 was additionally rotated and enlarged, including its number, bar/tilde distinction, set braces, membership signs, existential quantifier, j,k, both inequalities, and the vertical definition annotation. The words tels que occur between the membership condition and the inequality. Que overlaps the main-line canceled pour. H's apparent extra insertion after On dit is this same marginal tail, not additional manuscript text. The definition Vert/déf and B(J) lie below the first intersection term, not at the right end of the formula.

The complete displays85–87 were cropped and their numbers, letters, relations, decorations, annotation labels and line transitions checked. The left-hand relation in85 and its later occurrences are prec. B(K) and B(J) occur under the appropriate intersections in86. The script powerset P has an angular upper bowl and descending stem; C's mathcal rendering is retained, with no distinct competing P alphabet established by this leaf. H's font choice alone is not treated as a new mathematical assertion.

The dense/codense prose prompted a whole-clause reread because C and H disagree about the heavy first relation between I' and bar K. The tight crop shows a substantial connected left curve, favoring subset, but the prose equals abbreviation elsewhere has a left pen return too. The candidate therefore retains \unsure{\subset|=} and does not force either sign from the mathematical argument. The subsequent I' subset tilde J and I' subset bar K cap tilde J are unambiguous. Formula87's closing number delimiter is unusually straight with a lower turn; no decisive upper square-bracket arm can be separated, so an added narrow )|] doubt is retained. The entire formula is covered by a blind box. This reader performed no proof check or computation; check_events is empty. A separate check reported by the root reader is not claimed here.

## Revisions and verbal findings
The initial pour and old une propriété remain low-confidence canceled candidates. The live raised une is separate from the live propriété sym. The underline at C'est is only under C. The smaller Toute intersection text is an addition. Its crossed ending is mathematics, with a clear intersection and tilde-J, not notée; the first barred J remains uncertain under heavy overstrike. In Soient J,K, the original bandes is crossed and parties is live above it; the old word's doubt stays. The live domination in the quotient sentence begins above the right portion of the crossed l'inclusion and is marked inserted.

Avec J prec K, has a curved leader into the gap after bandes and before soit. The lower live word is enfin, followed by a canceled et, not H's en fait after the cancellation. The second canceled et also remains tentative. All three ens forms lack a stop; sym. and t.q. have the stops shown, and both stops of t.q. were checked on a tight crop. The prose = before égalité is legible and retained as the abbreviation for même. The alleged underline of égalité is the g's continuous descending stroke and leftward foot, so no independent underline is supplied. Tel has only one l and no final e; it is not modernized to telle. The final word is ainsi, followed by a separately written comma omitted in both witnesses.

## Sheet and numbering
There is no authorial number at the head, no title and no date. The written numbered formulas are84,85,86,87. The thin grey89 at the lower-left edge is another hand's foliation and is preserved as \margin{89}, not an authorial mspage. H's comments about neighboring folios and its suggested correction to the dense sign are editorial text, not manuscript content. No other page was inspected. No authorial question mark or explicit stated uncertainty appears here; all retained doubt macros describe uncertainty in reading ink.'''

notation=[
dict(sign=r'\Vert déf over B(J)',reading='Vertical definition relation below the first term of84.',evidence='Rotated marginal crop shows paired upright strokes below the underbrace, déf at their right, B(J) below.'),
dict(sign=r'\prec',reading='Domination relation; retain curved less-than form.',evidence='85, raised avec hypothesis, and final sentence show the same shape.'),
dict(sign=r'\unsure{\subset|=}',reading='Heavy first lower relation remains ambiguous; subset favored.',evidence='Connected left curve in tight dense_sign; the separate prose equals has a pen return, limiting certainty.'),
dict(sign='=',reading='Prose abbreviation for même.',evidence='Two short horizontal strokes between on a and égalité.'),
dict(sign='script P',reading=r'\mathcal P retained as the collection-of-parts symbol; no second P alphabet established.',evidence='One angular upper bowl and a long descending stem in ens_P crop; H selects a different TeX font.'),
]
hand_log=[
dict(habit='The g descender can have a long horizontal left foot resembling an underline.',places='égalité near the foot',scope='This continuous stroke is not a separate underline; distinguish it from the independent short underline below C.',witness_errors='C underlines égalité; removed.'),
dict(habit='A very short underline may apply only to the first letter of a word.',places="C'est near the head",scope='Independent rule extends under C only.',witness_errors='C omits it; H emphasizes all of C\'est.'),
dict(habit='Small prose added between lines can overlap independently canceled material.',places='Raised une; Toute intersection addition; parties; domination',scope='Trace separate baselines and strike endpoints before assigning state.',witness_errors='C misses raised state of une/domination; H leaves much readable ink illegible and misplaces marginal tail.'),
dict(habit='Continuous pen returns can make a heavy relation resemble both subset and equals.',places='I\prime versus bar K; prose = before égalité',scope='No global equivalence is assumed; retain the local ambiguous sign.',witness_errors='C and H disagree; no definitive glyph correction forced.'),
dict(habit='Low word interiors are strongly reduced, with high letters and dots carrying the distinction.',places='alors, enfin, ainsi, tel',scope='Tall l supports alors; f and i dot support enfin; final dotted word is thus ainsi; single l in tel.',witness_errors='H expands these as dans ce cas, en fait, on a, telle.'),
dict(habit='ens is unstopped in all three occurrences on this page.',places='Before powerset P; first and second quotient-line occurrences',scope='Each occurrence inspected individually.',witness_errors='H adds stops at all three.'),
]
abbreviations=[dict(form='sym.',expansion='symétrique'),dict(form='ens',expansion='ensemble'),dict(form='déf',expansion='définition'),dict(form='t.q.',expansion='tel que'),dict(form='i.e.',expansion='id est'),dict(form='=',expansion='même')]
doubts=[
dict(place='Opening canceled word',reading=r'\deleted{\unsure{pour}}',alternatives=['pour','unresolved letters under crossing strokes'],confidence='low',reason='Heavy cancellation and diagonal marginal que overlap; no resolution is claimed.'),
dict(place='Old phrase after C\'est',reading=r'\deleted{\unsure{une propriété}}',alternatives=['une propriété','unresolved old wording'],confidence='low',reason='Strike hides most joins and some uprights. Live replacement is separable, old text is not fully legible.'),
dict(place='First term of canceled added mathematics',reading=r'\deleted{\unsure{\bar J}\cap\widetilde J}',alternatives=[r'\bar J','overwritten first symbol'],confidence='medium',reason='Later intersection and tilde-J are clear, first barred glyph is heavily overwritten.'),
dict(place='Canceled bandes in Soient sentence',reading=r'\deleted{\unsure{bandes}}',alternatives=['bandes','unresolved middle under strike'],confidence='medium',reason='Tall b and ending support the candidate, but every middle letter is not independently plain.'),
dict(place='Canceled l\'inclusion',reading=r"\deleted{\unsure{l'inclusion}}",alternatives=["l'inclusion",'unresolved crossed old word'],confidence='low',reason='Low run is obscured by strike and overlaps the live replacement.'),
dict(place='First canceled lower et',reading=r'\deleted{\unsure{et}}',alternatives=['et','unresolved crossed short form'],confidence='medium',reason='Short crossed form is compatible with et but not fully separable.'),
dict(place='First lower I\prime relation',reading=r"I'\unsure{\subset|=}\bar K",alternatives=[r'\subset','='],confidence='medium',reason='Connected heavy left curve favors subset; comparison with linked prose = prevents secure resolution.'),
dict(place='Second canceled lower et',reading=r'\deleted{\unsure{et}}',alternatives=['et','unresolved crossed short form'],confidence='medium',reason='Initial loop and upright remain, other joins merge with cancellation.'),
dict(place='Right delimiter of number87',reading=r'(87\unsure{)|]}',alternatives=[')',']'],confidence='medium',reason='Nearly straight downstroke and lower-left turn; no decisive upper bracket arm. Added doubt only.'),
]

data=dict(page=PAGE,cote='150',scan='90',reader='reader_a; GPT-6 Astra Pro; effort not exposed; run SP92',line_count=36,
line_count_note='Counted writing rows, not TeX lines: 19 main prose baselines; 6 raised/added prose rows (une, two-line Toute intersection addition, parties, domination, avec hypothesis); 1 row of85; 3 rows of86 including lower B labels; 2 rows of87; 4 marginal84 writing levels (main set expression, its wrapped inequality tail, vertical definition row, B(J)); 1 other-hand foliation row. Formula labels are counted with their displays, not as extra lines merely because vertically offset.',
half_review='Whole original viewed once for layout; both supplied native-resolution overlapping halves viewed and read line by line against C and H. All agreed text, mathematical symbols, numbers, revisions, underlines and punctuation were inspected. All25 saved crops were viewed, including the rotated marginal formula/tail and tight disputed signs/words. No OCR, external research, other-page witness inspection or TeX compilation was used.',
deletion_insertion_review=revisions,changes=changes,diff_coverage=coverage,decisions=decisions,inventory=inventory,notes=notes,check_events=[],notation=notation,hand_log=hand_log,abbreviations=abbreviations,doubts=doubts,second_boxes=second_boxes,
crops=[dict(path=f'crops/{PAGE}_{n}.png',box=b,rotation_degrees=r,output_width=w,inspected=True) for n,b,r,w in rows])
assert len(coverage)==len(packet['differences'])==25
assert [x['id'] for x in decisions]==[x['id'] for x in packet['marks']]
assert len(rows)==25
valid={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(c['kind'] in valid and (c['crop'] is None or (ROOT/c['crop']).exists()) for c in changes)
tex=(ROOT/'records'/f'{PAGE}.tex').read_text()
assert all(t in tex for t in [opening,property_text,insertion,margin84,formula85,formula86,formula87])
(ROOT/'records'/f'{PAGE}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=PAGE,changes=len(changes),differences=len(coverage),decisions=len(decisions),inventory=len(inventory),second_boxes=len(second_boxes),crops=len(rows),doubts=len(doubts))))
