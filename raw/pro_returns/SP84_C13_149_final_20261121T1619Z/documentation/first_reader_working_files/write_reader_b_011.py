import json
from pathlib import Path
base=Path('/workspace/scratch/4644e52611c0')
page='149_scan011'
tex=r'''\scanpage{11}
\mspage{5}
même, d'après Mike Artin, prendre pour $U_i$ des schémas ``élémentaires'' sur $K_0$, se dévissant en fibrations successives de courbes. \inserted{Notons que $\operatorname{Spec}K=\eta$ est le pt générique} \deleted{Ceci dit, le \unsure{pt}} commun des $U_i$, qui sont géom$^t$ conn. \inserted{(et $\unsure{\simeq|=}$ géom. intègres)} sur \deleted{$K_0$} $k$ (clôture alg. de $\mathbb Q$ dans $K$).

Le choix de $\bar K$ définit un pt géom. $\bar\eta$ sur les $U_i$, d'où des groupes $\pi_1(U_i,\bar\eta)=E_i$, et on a, en vertu des résultats bien connus
\[
\operatorname{Spec}K=\varprojlim U_i
\]
\[
(10)\qquad E_{\bar K/K}=\pi_1(\eta,\bar\eta)\xrightarrow{\sim}\varprojlim_i\deleted{\unsure{\pi}}E_i
\]
\margin{$(\Gamma_i=\pi_1(U_i,\bar\eta))$}
D'autre part, si on pose
\[
(11)\qquad\bar U_i=U_i\otimes_k\overline{\mathbb Q}
\]
on a \inserted{pour tt $i$} une suite exacte d'homotopie

\noindent (12)\quad\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
1\arrow[r]\&\underbrace{\pi_1(\bar U_i,\bar\eta)}_{=\pi_i}\arrow[r]\&\pi_1(U_i,\bar\eta)\arrow[r]\arrow[d,equal]\&\pi_1(k,\bar\eta)\arrow[r]\arrow[d,equal]\&1\\
{}\&{}\&E_i\&\Gamma_{\bar k/k}=\Gamma_{\overline{\mathbb Q}/k}=\Gamma'_{\deleted{\unsure{\overline{\mathbb Q}/k}}}\&{}
\end{tikzcd}}

\margin{\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
{}\&\operatorname{Spec}(K)=\eta\arrow[r,dash]\arrow[d]\&\eta_{\overline{\mathbb Q}}\arrow[r,dash]\arrow[d,dash]\&\bar\eta=\operatorname{Spec}(\bar K)\\
{}\&U_i\arrow[r,dash]\arrow[d,dash]\&U_{i\overline{\mathbb Q}}=\bar U_i\arrow[d,dash]\&{}\\
\mathbb Q\arrow[r,dash]\&k\arrow[r,dash]\&\overline{\mathbb Q}\&{}
\end{tikzcd}}}
qui forment un syst. projectif de suites exactes, ou d'extensions ayant toutes même quotient $\Gamma'$, et dont les noyaux
\[
\pi_i=\pi_1(\bar U_i,\bar\eta)
\]
\margin{10}
'''
(base/'edition/reviews'/f'{page}.tex').write_text(tex)
boxes=json.loads(Path('/tmp/reader_b_011_boxes.json').read_text())
boxes['c17']=[970,777,1660,898]
changes=[]
def ch(id,place,C,H,final,evidence,crop,confidence,ac,ah,kind,cat,marked=False,math=False):
 changes.append(dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/{page}_{crop}.png',box=boxes[crop],confidence=confidence,against_C=ac,against_H=ah,kind=kind,error_category=cat,marked_in_H=marked,mathematical=math))
ch('c01','Opening paragraph, second manuscript line: quotes around élémentaires',r'``élémentaires\'\'','« élémentaires »',"``élémentaires''",'Two short upright quote strokes appear at each end of the word; there are no sideways angle strokes. Literal double quotes retained.','c01','high',False,True,'other','Other')
ch('c02','Opening paragraph, second manuscript line: field after sur',r'$K_0$',r'$k$',r'$K_0$','A tall angular K is followed by a separate small oval zero below its baseline. The zero is not punctuation; a comma follows the complete expression.','c01','high',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c03','Insertion above de courbes / Ceci dit: initial curved stroke',r'\inserted{(Notons que ...}',r'\add{(Notons que ...}',r'\inserted{Notons que ...}','The curved stroke to the left of Notons continues rightward beneath the insertion and then down to the baseline attachment after courbes. It is one continuous insertion leader; no separate opening parenthesis is visible. Both witnesses have converted that leader into a parenthesis.','c02','high',True,True,'text not on the page','Text that is not on the page',True)
ch('c04','Attachment and relative order of the Notons insertion and the struck phrase',r'\deleted{Ceci dit, le \unsure{pt}} \inserted{(Notons que ...}',r'\add{(Notons que ...} \struck{Ceci dit, le \ill{}}',r'\inserted{Notons que ...} \deleted{Ceci dit, le \unsure{pt}}','The insertion leader reaches the baseline immediately after courbes. and before the start of the struck Ceci. The proposed order records that attachment, retaining the whole cancelled phrase at its own baseline position.','c02','high',True,False,'insertion or placement','Insertions put in the wrong place')
ch('c05','Struck phrase after courbes.: final abbreviation',r'\deleted{Ceci dit, le \unsure{pt}}',r'\struck{Ceci dit, le \ill{}}',r'\deleted{Ceci dit, le \unsure{pt}}','Ceci dit, le is readable through a horizontal cancellation. The final small cluster has a low bowl followed by a taller crossed stem, supporting pt, but cancellation crosses the bowl and its descending stroke is not secure. This remains a candidate reading, not a resolved recovery.','c02','low',False,True,'other','Struck text',True)
ch('c06','Opening paragraph: abbreviation after qui sont',r'géom$^t$','géométriquement',r'géom$^t$','The baseline ends after the compressed géom strokes and a separate raised t stands above the gap before conn. The full word written by H is not present.','c03','high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised')
ch('c07','Opening paragraph: word after géom raised t',r'conn.','(omitted)',r'conn.','Following the raised t, there is a separate c, rounded o, two low n strokes, and a terminal dot. The word is visibly present and remains abbreviated.','c03','high',False,True,'omission','Omissions')
ch('c08','Interlinear insertion before sur: conjunction',r'(et $\unsure{\simeq|=}$ géom. intègres)',r'(est $\Leftrightarrow$ géom. intègres)',r'(et $\unsure{\simeq|=}$ géom. intègres)','The small e joins directly to a tall crossed t. No separate s is visible between them. The parenthesis around this insertion is independently written, unlike the continuous Notons leader.','c04','high',False,True,'misread word','Words')
ch('c09','Interlinear insertion before sur: relation sign',r'$\unsure{\simeq|=}$',r'$\Leftrightarrow$',r'$\unsure{\simeq|=}$','There are two short roughly horizontal strokes with curvature in the upper stroke and the left end of the lower. Their terminals do not show secure opposed arrowheads. The ink does not decide between a loose similarity sign and an equals sign; H’s double arrow is considered but not adopted as certain.','c04','low',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c10','Opening paragraph: cancelled field immediately after sur',r'\deleted{$K_0$}',r'\struck{\ill{}}',r'\deleted{$K_0$}','The tall K stem and upper/lower arms remain separable from the diagonal strike, and a small low oval zero follows at the right. The live lower-case k is written farther right.','c04','high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True,True)
ch('c11','Second paragraph: en vertu des résultats',r'des',r'de',r'des','The joined d and e are followed by a long low continuation terminating in a distinct dark downturned s. This final stroke belongs to the word, not to a comma or to résultats.','c05','high',False,True,'misread word','Words')
ch('c12','Second paragraph: punctuation after bien connus',r'connus',r'connus,',r'connus','The final s ends in its normal downturned terminal. The space below and to the right is blank; no detached comma follows.','c06','high',False,True,'text not on the page','Text that is not on the page')
ch('c13','Display (10): cancelled symbol between projective limit and E_i',r'\deleted{\unsure{\pi}}',r'(omitted)',r'\deleted{\unsure{\pi}}','A cancelled compact character remains before E_i, with two descending strokes and a cap-like upper trace. These favor pi, but the cancelling strokes obscure the top construction. It must remain present and doubtful. The entire display is included in the audit.','c07','low',False,True,'omission','Struck text',math=True)
ch('c14','Display (12): label below the first underbrace',r'_{=\pi_i}',r'_{\pi_i}',r'_{=\pi_i}','Two parallel oblique short strokes are written before pi_i below the underbrace. They form an equality sign and are distinct from the brace itself. H omits them.','c11','high',False,True,'omission','Symbols and indices',math=True)
ch('c15','Display (12): first Gamma index beneath pi_1(k,bar eta)',r'\Gamma_{\bar k/k}',r'\Gamma_{\overline K/K}',r'\Gamma_{\bar k/k}','Both indexed letters have the compact small k shape used in the top pi_1(k,bar eta), with the bar only over the first. They are not the tall angular K shapes of display (10). The denominator is visibly the same small form.','c12','high',False,True,'misread symbol or index','Symbols and indices',math=True)
ch('c16','Display (12): last member of the lower Gamma chain',r'=\Gamma\prime_{\deleted{\unsure{\overline{\mathbb Q}/k}}}',r'(not transcribed; editorial note says final member is overloaded and illegible)',r'=\Gamma\prime_{\deleted{\unsure{\overline{\mathbb Q}/k}}}','After a clear equals sign, a Gamma stem and roof survive, and a raised prime sits at its upper right. Beneath it, a dense cancelled subscript has a rounded Q-like body, an oblique separator and a final k-like form, but their superposed strokes prevent certain recovery. The live Gamma-prime is retained and the subscript remains explicitly doubtful and struck.','c12','medium',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',True,True)
ch('c17','Lower-left marginal diagram: first horizontal edge',r'\arrow[r,dash]',r'\arrow[r]',r'\arrow[r,dash]','Between Spec(K)=eta and eta_Qbar the shaft is irregularly retraced, but its right end is a short blunt cap without two converging barbs. The downward edge from Spec(K)=eta has a distinct arrowhead and is kept as an arrow.','c13','high',False,True,'drawing or diagram','Drawings and diagrams',math=True)
ch('c18','Lower-left marginal diagram: index on middle-row right U',r'U_{i\overline{\mathbb Q}}',r'U_{i,\overline{\mathbb Q}}',r'U_{i\overline{\mathbb Q}}','The low dotted i is directly followed by Q under a separate overbar. No comma lies between them. The curved tail beneath Q is part of that letter rather than a separator after i.','c13','high',False,True,'text not on the page','Text that is not on the page',math=True)
ch('c19','Lower-left foliation',r'\margin{10}',r'(omitted)',r'\margin{10}','A thin small 1 with an entry stroke is followed by a closed oval 0 at the extreme lower left. Its scale and pen weight differ from the bold author’s 5 at the top; it is recorded as another or uncertain hand.','c16','high',False,True,'omission','Omissions')

inv=[]
def el(n,kind,pos,first,hand='main manuscript hand',transcribed='yes'):
 inv.append(dict(scan=11,sheet_kind='text',hand=hand,element=f'e{n:02}',kind=kind,position=pos,first_words_or_objects=first,transcribed=transcribed))
el(1,'text','top centre','5')
el(2,'text','upper body, six baseline lines',"même, d'après Mike Artin")
el(3,'insertion','above de courbes / cancelled Ceci; leader attaches after courbes.','Notons que Spec K = eta est le pt générique')
el(4,'deletion','upper body, baseline after de courbes.','Ceci dit, le doubtful pt')
el(5,'insertion','above sur, left of the body','(et doubtful relation géom. intègres)')
el(6,'deletion','after sur, before the live k','K_0')
el(7,'text','middle-upper body, three baseline lines','Le choix de Kbar définit un pt géom.')
el(8,'display','below the paragraph Le choix','Spec K = projective limit U_i')
el(9,'display','middle body, label (10)','E_{Kbar/K} = pi_1(eta,etabar) isomorphic to limit E_i')
el(10,'deletion','inside display (10), immediately before E_i','doubtful pi')
el(11,'margin note','right margin beside display (10)','(Gamma_i = pi_1(U_i,etabar))')
el(12,'text','middle body after display (10)',"D'autre part, si on pose")
el(13,'display','middle-lower body, label (11)','Ubar_i = U_i tensor_k Qbar')
el(14,'text','line above exact sequence (12)',"on a une suite exacte d'homotopie")
el(15,'insertion','above on a une; curved leader enters between a and une','pour tt i')
el(16,'diagram','lower body, two rows, label (12)','1 to pi_1(Ubar_i,etabar) to pi_1(U_i,etabar) to pi_1(k,etabar) to 1; lower labels and vertical equalities')
el(17,'deletion','lower row of (12), subscript after final Gamma-prime','doubtful Qbar/k')
el(18,'diagram','lower-left margin, three rows','Spec(K)=eta — eta_Qbar — etabar=Spec(Kbar); U_i — U_{i Qbar}=Ubar_i; Q — k — Qbar')
el(19,'text','lower-right body continuing below the diagram','qui forment un syst. projectif de suites exactes')
el(20,'display','bottom body','pi_i = pi_1(Ubar_i,etabar)')
el(21,'text','extreme lower-left corner','10','another or uncertain hand; thin small foliation')

# Readings name complete source units. Incidental clipped adjacent ink at a rectangular edge
# is not extended or guessed. The full (12) box intentionally spans both adjacent crop areas.
aud=[]
def ab(n,kind,box,reading):
 aud.append(dict(box=f'b{n:02}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
ab(1,'number',boxes['c15'],r'\mspage{5}')
ab(2,'prose',boxes['c01'],r'''``élémentaires'' sur $K_0$,''')
ab(3,'insertion/deletion',[295,327,1631,463],r'''de courbes. \inserted{Notons que $\operatorname{Spec}K=\eta$ est le pt générique} \deleted{Ceci dit, le \unsure{pt}}''')
ab(4,'prose',boxes['c03'],r'qui sont géom$^t$ conn.')
ab(5,'insertion/deletion',[253,549,1650,701],r'\inserted{(et $\unsure{\simeq|=}$ géom. intègres)} sur \deleted{$K_0$} $k$ (clôture alg. de $\mathbb Q$ dans $K$).')
ab(6,'prose',boxes['c05'],'des')
ab(7,'prose',boxes['c06'],'connus')
ab(8,'formula',boxes['c07'],r'(10)\qquad E_{\bar K/K}=\pi_1(\eta,\bar\eta)\xrightarrow{\sim}\varprojlim_i\deleted{\unsure{\pi}}E_i')
ab(9,'margin',[1414,1082,1681,1201],r'\margin{$(\Gamma_i=\pi_1(U_i,\bar\eta))$}')
ab(10,'formula',boxes['c09'],r'(11)\qquad\bar U_i=U_i\otimes_k\overline{\mathbb Q}')
ab(11,'insertion',[465,1490,665,1590],r'\inserted{pour tt $i$}')
seq=tex[tex.index(r'\noindent (12)'):tex.index('\n\n\\margin{\\diagram')]
ab(12,'diagram',[279,1627,1657,1843],seq)
margin=tex[tex.index(r'\margin{\diagram'):tex.index('\nqui forment')]
ab(13,'diagram',boxes['c13'],margin)
ab(14,'formula',boxes['c14'],r'\pi_i=\pi_1(\bar U_i,\bar\eta)')
ab(15,'number',boxes['c16'],r'\margin{10}')
ab(16,'formula',[1324,785,1658,895],r'$\pi_1(U_i,\bar\eta)=E_i$,')

coverage=[]
def cv(row,classification,change,reason):
 coverage.append(dict(row=row,classification=classification,change_id=change,reason=reason))
cv(1,'editorial-only',None,'Scan header versus H’s editorial author-page note; only the source 5 is an author page number.')
cv(2,'editorial-only',None,'de l’auteur is H’s description, not manuscript text.')
cv(3,'material','c01','Source upright double quotes, not guillemets.')
cv(4,'material','c02','The source has capital K with subscript zero; H writes k.')
cv(5,'material','c04','Source leader attaches the insertion before the cancelled phrase. The doubtful final abbreviation, absent as a reading from H, is separately recorded in c05.')
cv(6,'material','c04','Same relative-order difference; H’s order follows the attachment, and the entire cancellation remains.')
cv(7,'material','c06','Written géom raised t is retained without expansion. The separately omitted conn. is recorded in c07.')
cv(8,'material','c08','The word is et, not est. The relation-sign disagreement is separately recorded in c09 and M0977 remains undecided.')
cv(9,'material','c10','Readable cancelled K_0 is retained where H uses illegibility.')
cv(10,'editorial-only',None,'The paragraph-final period agrees. H’s unclosed-parenthesis note is editorial; inspection of the continuous leader is separately recorded in c03 against both witnesses.')
cv(11,'material','c11','The final s in des is visible.')
cv(12,'material','c12','There is no detached comma after connus.')
cv(13,'material','c13','Cancelled pi-like ink is present and kept doubtful.')
cv(14,'macro-only',None,'Display closing syntax differs because H includes the right-side note in the same display.')
cv(15,'editorial-only',None,'H’s explanation of Gamma_i versus E_i is editorial. Both source forms remain; margin placement is represented by the margin macro.')
cv(16,'macro-only',None,'Display wrapper only.')
cv(17,'macro-only',None,'tikzcd serialization versus H’s single displayed expression; source two-row relationships are retained.')
cv(18,'macro-only',None,'Both encode the visible rightward first arrow in (12).')
cv(19,'material','c14','The equality sign before the underbrace pi_i is visible.')
cv(20,'macro-only',None,'Reordered serialization of the same arrow and the vertical equality to E_i.')
cv(21,'macro-only',None,'The diagram nodes and vertical equalities are serialized differently. The separate lower-case k versus H’s capital K index is a real additional discrepancy recorded in c15.')
cv(22,'material','c16','The final equals Gamma-prime is readable; the diff has misaligned its neighboring nodes.')
cv(23,'material','c16','The cancelled final subscript is retained as a doubtful reading, not replaced by neighboring top-row text.')
cv(24,'material','c16','The last lower-row member is source ink; H’s editorial illegibility note does not transcribe it. Remaining tokens are diagram/display wrappers.')
cv(25,'macro-only',None,'ampersand replacement is TeX syntax only.')
cv(26,'material','c17','The first horizontal marginal connector has no secure arrowhead.')
for row in [27,28,29,30]:
 cv(row,'macro-only',None,'dash and no head encode the same visible bare connector.')
cv(31,'material','c18','No comma is written between i and Qbar in the subscript.')
for row in [32,33,34]:
 cv(row,'macro-only',None,'dash and no head encode the same visible bare connector.')
cv(35,'material','c19','The small lower-left foliation 10 is visible and omitted by H.')

report=dict(
 scan=11,reader='/root/reader_b',lines_read=30,changes=changes,
 decisions=[dict(id='M0977',decision='undecided',reading=r'\unsure{\simeq|=}',evidence='Two slightly curved short bars are visible after et. A loose similarity sign and equals sign remain plausible; definite opposed arrowheads required by H’s double arrow are not separable. The original two-way doubt is retained.',crop=f'crops/{page}_c04.png',box=boxes['c04'],confidence='low')],
 inventory=inv,
 notes=[
  'Run SP84_C13_149; reader GPT-6 Astra Pro, effort not exposed. Full image inspected once for layout, then each supplied half once; every baseline word, display, margin item and insertion was read against the ink. Seventeen enlarged crops were personally inspected. No OCR, outside research, TeX compilation, or mathematical proof check was used.',
  'Page continues the construction with elementary schemes U_i, states the projective-limit identification (10), defines Ubar_i in (11), and writes the homotopy exact sequences (12), followed by a three-row marginal diagram and the beginning of the discussion of their kernels. These are source assertions, not independently checked mathematical claims.',
  'The source has bold author page 5 at the top and thin small foliation 10 at the bottom left. The latter is recorded with margin and attributed to another or uncertain hand. There is no date or title on this leaf.',
  'The curved mark before Notons is continuous with its attachment leader. It is not transcribed as an opening parenthesis; the insertion attaches immediately after courbes. and before the crossed phrase. H’s editorial comment about an unclosed parenthesis is therefore not carried into source text.',
  'The manuscript alternates the main E_i with the parenthetical marginal Gamma_i; both are retained literally. The vertical equalities in (12) remain vertical, and the short connectors in the marginal diagram remain bare shafts except for the clear downward arrow from Spec(K)=eta to U_i.',
  'Four doubts are retained: the cancelled pt, the interlinear similarity/equality sign, the cancelled pi in (10), and the crossed Qbar/k-like subscript following the live Gamma-prime in (12). Only the relation-sign doubt was listed in marks.tsv; the three additional C doubt macros were not silently resolved.',
  'The E_i in the prose formula is heavy and locally retraced. Its extra stroke does not maintain a separately bounded doubled stem, so ordinary E is retained, with the full inline formula included in the audit. E in (10) and under (12), and the Gamma forms, likewise remain ordinary capitals; Q has the characteristic internal/doubled stroke and is rendered double-struck.',
  'Rectangular audit boxes identify complete source units; unrelated clipped edge fragments are not extended or guessed. One full-span audit box covers all of (12), including both adjacent crops, its formula number, numeric indices, vertical equalities, and the doubtful cancelled subscript. The isolated pair of tiny dark specks near the marginal diagram has no clear syntactic attachment and is not promoted to punctuation.',
  'The count of 30 inspected manuscript line units includes the three separate insertions, the separate marginal formula, three rows of the marginal diagram, two rows of (12), and both foliation numbers; it is not a TeX source-line count.'
 ],
 checks=[],
 hand=[
  dict(habit='Curved insertion leaders continue beneath inserted words to a baseline attachment; their curves need not be parentheses.',pages=[11],consistency='Locally verified in Notons (c02) and pour tt i (c10). The parenthesis around et ... intègres in c04 is separately written.',misread='Both C and H treated the initial Notons leader as an opening parenthesis; C also ordered the insertion after its cancelled predecessor.'),
  dict(habit='Abbreviations use raised final t and short baseline forms.',pages=[11],consistency='géom raised t, conn., pt, géom., alg., tt and syst. are locally visible; abbreviations remain literal.',misread='H expands géom raised t and drops the separate conn.'),
  dict(habit='A small downturned terminal often supplies final s.',pages=[11],consistency='The final s in des can be distinguished from detached punctuation by its continuous attachment; knowns/connus ends similarly.',misread='H gives de and supplies a comma after connus, despite the word terminal and following blank space.'),
  dict(habit='Arrowheads, bare shafts and vertical equalities are graphically distinct.',pages=[11],consistency='Clear arrowheads in the main exact sequence and Spec(K) down to U_i; blunt shafts elsewhere in the marginal diagram; two upright strokes above lower E_i and Gamma-chain.',misread='H adds a head to the first marginal horizontal edge. Equality before the underbrace label is omitted by H.'),
  dict(habit='Local retracing can thicken ordinary E and must be distinguished from deliberate alphabet doubling.',pages=[11],consistency='The prose E_i has overlapping strokes without a continuous separate doubled stem; Q shows an internal stroke repeatedly. Other E forms in (10)/(12) do not require a changed alphabet.',misread='No alphabet change adopted from darkness or overlap alone; the inline formula is preserved for independent inspection.')
 ],
 notation=[
  dict(written='K with low oval zero',rendering=r'K_0',meaning='Field named in the opening discussion; later cancelled in favor of k.',evidence='c01 has an uncancelled clear zero; c04 retains K and zero through the strike.'),
  dict(written='Q with an internal/doubled stroke, sometimes under an overbar',rendering=r'\mathbb Q,\ \overline{\mathbb Q}',meaning='Rational field and its algebraic closure as named in the source.',evidence='Opening paragraph, (11), lower row of (12), and all relevant marginal diagram nodes; c04, c09, c12, c13.'),
  dict(written='E_i and marginal Gamma_i',rendering=r'E_i,\ \Gamma_i',meaning='Both locally equated to pi_1(U_i,bar eta); source variation retained.',evidence='Inline formula c17 and marginal parenthesis c08.'),
  dict(written='E with first K barred and oblique/near-upright extension separator',rendering=r'E_{\bar K/K}',meaning='Left member of identification (10).',evidence='Entire formula c07; the bar is over the first K only.'),
  dict(written='Lower Gamma index small kbar/k, then Qbar/k, then Gamma-prime',rendering=r'\Gamma_{\bar k/k}=\Gamma_{\overline{\mathbb Q}/k}=\Gamma\prime_{\deleted{\unsure{\overline{\mathbb Q}/k}}}',meaning='Lower label connected vertically to pi_1(k,bar eta) in (12).',evidence='c12; first pair of small k forms differs from H’s capital K; last crossed index remains uncertain.'),
  dict(written='pi_i beneath first underbrace and in bottom definition',rendering=r'\pi_i=\pi_1(\bar U_i,\bar\eta)',meaning='Kernels named in the final prose.',evidence='c11 and c14; equality sign below the brace is written and retained.'),
  dict(written='lim with a left-pointing arrow underneath',rendering=r'\varprojlim',meaning='Projective-limit notation used in the two middle displays.',evidence='The separate lower left arrow is visible in the Spec K display and in c07; only (10) has a written i below it.')
 ],
 abbreviations=[
  dict(form='pt',expansion='point',place='Notons insertion and Le choix paragraph; a cancelled candidate also follows Ceci dit, le'),
  dict(form=r'géom$^t$',expansion='géométriquement',place='qui sont géom raised t conn.'),
  dict(form='conn.',expansion='connexes',place='end of the baseline qui sont'),
  dict(form='géom.',expansion='géométriquement',place='interlinear et ... géom. intègres'),
  dict(form='géom.',expansion='géométrique',place='un pt géom. in Le choix paragraph'),
  dict(form='alg.',expansion='algébrique',place='clôture alg. de Q dans K'),
  dict(form='tt',expansion='tout',place='pour tt i insertion'),
  dict(form='syst.',expansion='système',place='qui forment un syst. projectif')
 ],
 doubts=[
  dict(place='cancelled phrase after courbes.',reading=r'\deleted{Ceci dit, le \unsure{pt}}',alternatives=['unreadable final short word'],confidence='low',reason='The p-like bowl and taller crossed final stem favor pt, but the cancellation obscures part of the first letter and its descender.'),
  dict(place='M0977, interlinear et ... géom. intègres',reading=r'\unsure{\simeq|=}',alternatives=[r'\simeq','=',r'\Leftrightarrow (H)'],confidence='low',reason='Two curved/irregular short bars are visible; neither precise similarity construction nor plain equals is secure, and opposed arrowheads are not plain.'),
  dict(place='display (10), before final E_i',reading=r'\deleted{\unsure{\pi}}',alternatives=['unreadable cancelled symbol'],confidence='low',reason='Two lower strokes and an obscured cap favor pi, but the cancellation covers the decisive upper junction.'),
  dict(place='display (12), crossed subscript after Gamma-prime',reading=r'\deleted{\unsure{\overline{\mathbb Q}/k}}',alternatives=['partly unreadable crossed subscript'],confidence='low',reason='Rounded first body, oblique separator and final k-like strokes remain, but multiple diagonal cancellation strokes prevent secure recovery of every component.')
 ],
 audit_boxes=aud,diff_coverage=coverage
)
(base/'edition/reviews'/f'{page}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':page,'changes':len(changes),'inventory':len(inv),'audit_boxes':len(aud),'diff_rows':len(coverage),'doubts':len(report['doubts']),'crops':len(boxes)},ensure_ascii=False))
