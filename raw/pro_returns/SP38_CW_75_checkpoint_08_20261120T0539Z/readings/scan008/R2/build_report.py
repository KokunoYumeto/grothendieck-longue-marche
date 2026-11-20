from pathlib import Path
from datetime import datetime, timezone
import json, re
root=Path('out/readings/scan008/R2')
manifest=json.loads((root/'crop_manifest.json').read_text())
byid={m['id'].split('_')[0]:m for m in manifest}
findings=[]
doubt_coverage=[]
def add(id,place,c,h,final,evidence,confidence,kind,diff_c,diff_h,bbox,crop='',doubt_action='',marked=False,math_note='',c_doubt=''):
    findings.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked,diff_c=diff_c,diff_h=diff_h,bbox=bbox,crop=(f'readings/scan008/R2/crops/{byid[crop]["id"]}.png' if crop else ''),doubt_action=doubt_action,s_id='',math_note=math_note))
    if c_doubt: doubt_coverage.append(dict(c_doubt=c_doubt,finding=id,action=doubt_action))
add('F01','Opening: word after pour',r'\unsure{tte|les|toute}','toute','tte','Two adjacent tall stems followed by a short e-like exit; no intervening ou and no les shape.','high','abbreviation expanded or spelling modernised',True,True,[507,140,571,197],'01','resolve',c_doubt='tte|les|toute')
add('F02','Opening: overwritten origin sign',r'\deleted{\unsure{o|\omega}}\sigma(a)',r'\sigma(a)',r'\deleted{\unsure{o|\omega}}\sigma(a)','Live sigma has a long top stroke; blue loops beneath it remain undecidable between the supplied o and omega readings.','low','omission',False,True,[451,209,541,261],'02','retain',c_doubt=r'o|\omega')
add('F03','Opening: quotation marks around orientation de a',r'``orientation de $a$\'\'','« orientation de a »',r'``orientation de $a$\'\'','The half shows paired short quotation ticks, not angled guillemets.','high','misread symbol or index',False,True,[992,150,1336,215])
add('F04','Slanted margin: canceled quantifier before the relation',r'\deleted{\unsure{\exists1|\exists}}','No quantifier transcribed; note says some crossed words are illegible',r'\deleted{\unsure{\exists1|\exists}}','Rotated crop shows the existential bars beneath the cancellation and a possible separate upright, still crossed.','low','readable ink left as \\ill{}',False,True,[134,266,179,323],'03','retain',True,c_doubt=r'\exists1|\exists')
add('F05','Slanted margin: canceled lower sentence',r'\deleted{\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,}','No text transcribed; note says some crossed words are illegible',r'\deleted{\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,}','After rotation, the lower line yields the quantifiers and A; the first small variable is crossed too heavily to choose s or a.','low','readable ink left as \\ill{}',False,True,[30,307,219,527],'03','retain',True,c_doubt=r'\forall s\in S|\forall a\in S')
add('F06','Condition label',r'(\unsure{O|0})','(O)',r'(\unsure{O|0})','A nearly round, open-topped loop does not decide letter O versus numeral zero.','medium','misread symbol or index',False,False,[288,280,368,329],'04','retain',c_doubt='O|0')
add('F07','Main condition: uniqueness mark',r'\exists1\ a\in R\{s\}',r'\exists !\, a\in R\{s\}',r'\exists1\ a\in R\{s\}','The full-resolution half shows a single uninterrupted upright after the existential, with no detached exclamation dot.','high','misread symbol or index',False,True,[1307,299,1536,365],math_note='Both conventions may express uniqueness, but the diplomatic glyph here is 1.')
add('F08','First proposition: orientation name',r'\unsure{\omega|w}',r'\omega',r'\omega','Two rounded lower lobes and curled ends are clear in the half; the later small indices use the same form.','high','misread symbol or index',True,False,[1185,541,1375,591],doubt_action='resolve',c_doubt=r'\omega|w')
add('F09','Slanted marginal diagram and separator',r'A\xrightarrow{\substack{\sigma\\\sim}}S; margin macro with no side selection or rule',r'A\xrightarrow{\sigma}S; note describes left diagonal placement and a separating line',r'Left margin: A\xrightarrow{\substack{\sigma\\\sim}}S, followed by the relation and crossed sentence; separate rule below','Rotated crop distinguishes sigma high above a separate tilde and the arrow, with a long independent separator under the note.','high','drawing or diagram',True,True,[27,112,312,546],'03')
add('F10','Second proposition: singular du contour',r'orientation du contour',r'orientation des contours',r'orientation du contour','Half shows du followed by singular contour; neither a separate es after d nor terminal s after contour.','high','misread word',False,True,[746,652,1272,721])
add('F11','Canceled first expression before live u_omega(s)',r'\deleted{\unsure{\omega(s)|w(s)}}',r'\struck{\ill{}}',r'\deleted{\unsure{\omega(s)|w(s)}}','Low initial double lobe and following parenthesis/s forms remain partly visible through the horizontal cancellation; alphabet is unresolved.','low','readable ink left as \\ill{}',False,True,[632,753,729,790],'05','retain',True,c_doubt=r'\omega(s)|w(s)')
add('F12','Canceled second expression before live u_omega(s)',r'\deleted{\unsure{u_{\omega}|u}}',r'\struck{\ill{}}',r'\deleted{\unsure{u_{\omega}|u}}','The second dark canceled unit has a u-like top and lower overlapping ink; its subscript cannot be securely recovered.','low','readable ink left as \\ill{}',False,True,[750,750,820,791],'05','retain',True,c_doubt=r'u_{\omega}|u')
add('F13','Definition at s: raised replacement and underline',r'\inserted{u_{\omega}}(s), l\'\uline{extrémité}',r'u_\omega(s), l\'extrémité',r'\inserted{u_{\omega}}(s), l\'\uline{extrémité}','Replacement u with omega index sits above the canceled unit while (s) stays on the baseline; extrémité has a separate underline in the half.','high','insertion or placement',False,True,[752,727,1162,810],'05')
add('F14','After qui ait: canceled comme',r'\deleted{\unsure{comme}}',r'arête \struck{\ill{}} \sigma^{-1}(s) qui ait s comme origine',r'arête \inserted{\sigma^{-1}(s)} qui ait \deleted{\unsure{comme}} s comme origine','The heavy short rule is after qui ait, over several low humps; sigma inverse is above the earlier gap after arête and has an insertion leader.','low','deletion state (struck given live or live given struck)',False,True,[274,801,1219,918],'06','retain',True,c_doubt='comme')
add('F15','Definition at a: arc de S',r'\unsure{arc|ar} de S','arc de S','arc de S','The crop has a separate small final c after ar. The following capital has the two open bends of S.','high','misread word',True,False,[1059,924,1292,976],'07','resolve',math_note='S is preserved despite the edge-domain issue; see check M01.',c_doubt='arc|ar')
add('F16','Three oriented-arc drawings: placement',r'Three centered \figure blocks',r'Left-margin drawing marker plus H_drawings/01-3.tex',r'Three left-margin TikZ drawings, preserving arrowheads, dots and all labels','Both halves show all three at the left of their corresponding propositions/definitions. The supplied H redraw contains the expected three geometries; no substantive topology difference was found.','high','drawing or diagram',True,False,[62,499,374,1114])
add('F17','Alors map: overwritten second entry of first pair',r'(S,\deleted{\unsure{R|B}}A)',r'(S,A)',r'(S,\deleted{\unsure{R|B}}A)','Overlapping loops and a diagonal remain in the first pair; an underlying R or B is still possible beneath the final A.','low','omission',False,True,[515,1107,632,1173],'09','retain',c_doubt='R|B')
add('F18','Alors map: connecting mark',r'\unsure{-|\to}',r'\to',r'\unsure{-|\to}','A short shaft ends in a downward thickening; no separate upper arrow wing is resolved.','medium','misread symbol or index',False,True,[642,1123,686,1154],'09','retain',c_doubt=r'-|\to')
add('F19','Brace left of Alors paragraph',r'\margin{$\big\}$}',r'No brace',r'\reversemarginpar\margin{$\big\}$}\normalmarginpar','The pale brace is on the left at the page fold; C does not select a side and H omits it.','high','insertion or placement',True,True,[245,1147,283,1289])
add('F20','First autom abbreviation',r'un autom du graphe',r'un automorphisme du graphe',r'un autom du graphe','The half shows the short autom form and a gap before du; no full orphisme ending.','high','abbreviation expanded or spelling modernised',False,True,[931,1122,1307,1183])
add('F21','Second autom abbreviation and punctuation',r'Les autom $u_{\omega},u_{\omega}^{-1}$',r'Les autom. $u_\omega,u_\omega^{-1}$',r'Les autom $u_{\omega},u_{\omega}^{-1}$','No separate point occurs after autom before the formulas in the lower half.','high','other',False,True,[1062,1205,1538,1271])
add('F22','Canceled words before conditions équivalentes',r'\deleted{fait que}',r'\struck{faits que}',r'\deleted{fait que}','Crop shows f, a, i, and t before an empty gap; no separate final s before que.','high','misread word',False,True,[839,1300,1058,1373],'10')
add('F23','Order sentence: end after n',r'est $n$',r'est $n$. Donc',r'est $n$ followed by a new line/paragraph beginning the doubtful fleche word','The half has no written period after the final n of the order sentence.','high','other',False,True,[1420,1539,1577,1597])
add('F24','Word before u_omega not equal u_minusomega',r'\unsure{flèche|et}','Donc',r'\unsure{fleche|flèche|et}','Long looped opening and another upright exclude a secure Donc. The compressed remainder and presence/absence of an accent remain unresolved; unaccented fleche is now the primary literal candidate.','low','misread word',True,True,[282,1620,396,1692],'11','retain',c_doubt='flèche|et')
add('F25','Equivalence shorthand after inequality','sss','ssi','sss','The lower half shows three short s-like returns with no detached i dot.','high','abbreviation expanded or spelling modernised',False,True,[723,1619,776,1673])
add('F26','Connective between bound and map',r'\unsure{donc|alors}','donc',r'\unsure{donc|alors}','Tall initial return favors d, but the remaining letters are a near-horizontal trace; the alternative is retained.','low','misread word',False,False,[1145,1623,1246,1678],'12','retain',c_doubt='donc|alors')
add('F27','Name of orientation set',r'\unsure{\operatorname{or}|{\rm Or}}',r'\operatorname{Or}',r'\operatorname{or}','The o is a low oval, smaller than the following capital S; its connected r has the ordinary short shoulder.','high','misread symbol or index',True,True,[641,1714,696,1766],'13','resolve',c_doubt=r'\operatorname{or}|{\rm Or}')
add('F28','Link after or(S,A,R)',r'\unsure{avec|sur}','avec',r'\unsure{avec|sur}','A closed first oval favors avec, but the flattened intervening and final groups do not securely decide the complete word.','low','misread word',False,False,[910,1719,1001,1766],'14','retain',c_doubt='avec|sur')
add('F29','l’ens abbreviation','l\'ens','l\'ens.','l\'ens','The following word begins after a clear space; no separate abbreviation point is visible.','high','other',False,True,[1064,1708,1198,1768],'14')
add('F30','After the two condition numbers: enclosing mark',r'\unsure{$1^{\circ}$ ou $2^{\circ}\big\}$|$1^{\circ}$ ou $2^{\circ})$}',r'1°, 2°\}',r'$1^{\circ}$ \unsure{ou|$-$} $2^{\circ}\big\}$','The closing mark has a distinct inward mid-cusp, resolving it as a right brace. The connector between the numbers remains separately uncertain.','high','misread symbol or index',True,False,[1161,1793,1364,1879],'15','resolve',c_doubt=r'1° ou 2° with right brace|1° ou 2° with closing parenthesis')
add('F31','Connector between condition numbers; unmatched opening brace in H','ou',r'\{ g\in\operatorname{Aut}(S,A,R) ... 1°, 2°\}',r'g\in\operatorname{Aut}(S,A,R) ... $1^{\circ}$ \unsure{ou|$-$} $2^{\circ}\big\}$','Between the numbers are two short near-horizontal traces rather than a comma. No opening brace precedes g in the half; the written closing brace is left unmatched.','medium','text not on the page',True,True,[1196,1707,1404,1880],'15',math_note='The closing brace is preserved without silently supplying an opening brace.')
add('F32','Et after the brace','Et','et','Et','A large overwritten capital E precedes the separate t.','high','misread word',False,True,[1419,1788,1500,1851],'15')
add('F33','Group abbreviation before cyclique',r'\unsure{gpe|grpe}','groupe',r'\unsure{gpe|grpe}','Long g descent, low connecting shoulder and p/e ending support a contraction; a separate r is not securely distinguishable.','medium','abbreviation expanded or spelling modernised',False,True,[307,1900,438,1973],'16','retain',c_doubt='gpe|grpe')
add('F34','Canceled word after est',r'\deleted{\unsure{formé|form}}',r'\struck{\ill{}}',r'\deleted{formé}','Long f, low or/m traces, and a detached acute at the end survive the rule; the accent excludes bare form.','high','readable ink left as \\ill{}',True,True,[1520,1893,1622,1981],'17','resolve',True,c_doubt='formé|form')
add('F35','Replacement le and added group name',r'\inserted{le}\inserted{gpe $G^0$}',r'le ... groupe $G^0$ (note says group name is marginal)',r'\inserted{le}\inserted{gpe $G^{\unsure{0|\circ}}$}','le is written above the canceled word; the left insertion has the short gpe form, with a curved leader before des. H expands the contraction.','high','insertion or placement',False,True,[200,1885,1636,2065],'18')
add('F36','Superscript on inserted G',r'G^{\unsure{0|\circ}}',r'G^0',r'G^{\unsure{0|\circ}}','A small closed raised oval cannot decide numeral zero versus circle; later recurrence follows the primary 0 by the stated convention.','medium','misread symbol or index',False,False,[298,1959,366,2010],'18','retain',c_doubt='0|circle on G')
add('F37','autom before orientés','autom','automorphismes','autom','The base line has only the short autom form; orientés is an interlinear insertion with a caret.','high','abbreviation expanded or spelling modernised',False,True,[470,1959,742,2059],'19')
add('F38','Added gloss after tuple',r'\inserted{\unsure{lire|les} de $S,A,R;\omega)$}',r'(i.e. de $(S,A,R;\omega)$) before de $(S,A,R,\omega)$',r'\inserted{\unsure{lire|les|i.e.} de $S,A,R;\omega)$}','The short first group remains unreadable enough to allow lire/les and possibly i.e.; the long leader starts after the baseline tuple. No opening parenthesis is visible before the added S.','low','insertion or placement',True,True,[976,1934,1298,2059],'19','retain',math_note='The inserted tuple’s unmatched closing parenthesis is retained.',c_doubt='lire|les')
add('F39','Canceled phrase above Torseur',r'\deleted{Se donner un}',r'\struck{La donnée d\'un}',r'\deleted{\unsure{Se|La} donner un}','The canceled phrase has three word groups. The middle ends in a r-like return and no separate d’ precedes un. Initial capital and following small letter remain compatible with Se or La.','medium','misread word',True,True,[437,2181,792,2230],'20')
add('F40','Added lower bound in last paragraph',r'\inserted{$(n\geq1)$}',r'($n\geq1$)',r'\inserted{$(n\geq1)$}','The parenthesized bound is above the baseline, connected by a sweeping insertion leader after Z/nZ.','high','insertion or placement',False,True,[891,2184,1056,2297])
add('F41','Darkened word after ensemble',r'\deleted{\unsure{où}} à','à',r'\unsure{\deleted{où} à|à}','Crop shows a single heavily retraced unit with a grave and a final à reading. A canceled où beneath it is possible, but an ordinary reinforced à cannot be excluded; the deletion state is now explicitly doubtful.','low','deletion state (struck given live or live given struck)',True,False,[1195,2247,1258,2287],'21','retain',c_doubt='où')
add('F42','Last paragraph: spelling and ending of elément',r'\unsure{élément|éléments}','éléments','elément','There is no separate initial acute over the first e. A mark is present over the second e. Final t has one curved exit and no separate s.','high','abbreviation expanded or spelling modernised',True,True,[1301,2243,1471,2291],'22','resolve',c_doubt='élément|éléments')
add('F43','Raised mark before circulaire',r'\unsure{$^{\times}$|$^{*}$}','« circulaire »',r'\unsure{$^{\times}$|$^{*}$} circulaire','Raised crossed strokes precede circulaire; their thick junction does not securely decide cross versus star. The end has a single written period, without a closing quotation mark.','medium','misread symbol or index',False,True,[632,2300,900,2349],'23','retain',c_doubt='raised times|star')
add('F44','Two bracketed formulas: line wrapping',r'Both bracketed formulas broken over two lines',r'Each bracketed formula on one line',r'First inequality on second line; second formula’s i.e. inequality on second line','The supplied halves show the two line arrangements and closing square brackets explicitly; the reading keeps those breaks.','high','insertion or placement',False,True,[779,820,1633,1125])

inventory=[]
def inv(element,kind,position,first):
    inventory.append(dict(sheet_kind='text',hand='his hand',element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('title','text','top, x235–785 y65–124',"Orientation d'un contour.")
inv('opening definition','text','upper block, x237–1590 y142–287','Choix pour tte arête a∈A')
inv('overwritten origin sign','deletion','opening, x451–541 y209–261','o/omega beneath sigma')
inv('slanted marginal note','margin note','upper left, x27–312 y112–546','∀a∈A … (sigma(a),a)∈R')
inv('slanted A to S diagram','diagram','within upper-left note','A, sigma, tilde, right arrow, S')
inv('canceled marginal uniqueness','deletion','within upper-left note, x134–179 y266–323','exists1/exists')
inv('canceled marginal lower sentence','deletion','within upper-left note, x30–219 y307–527','∀s∈S/∀a∈S, exists1 a∈A,')
inv('separator under slanted note','drawing','upper-left note lower edge after rotation','independent separating rule')
inv('orientation condition','display','x274–1657 y283–405','(O/0) Si … s∈S, exists1 a∈R{s} … s=sigma(a)')
inv('canceled condition antecedent','deletion','within condition, x636–1110 y283–337','R{s}={a,b}, alors exists')
inv('reduction line','text','x502–1091 y411–453','Réduction au cas connexe')
inv('first proposition','text','x484–1545 y456–598','Prop Si (S,A,R) est un contour connexe')
inv('two oriented arcs','drawing','left margin, x154–374 y499–572','horizontal arrow; joint dot; rising arrow')
inv('vertex-step sketch','drawing','left margin, x90–255 y646–754','s, sigma inverse s, u_omega(s)')
inv('second proposition','text','x275–1518 y647–727','deleted Prop; Prop Soit omega orientation du contour')
inv('canceled proposition label','deletion','x274–371 y647–712','Prop')
inv('definition of vertex successor','text','x262–1487 y744–902','∀s∈S, soit … l’extrémité de l’unique arête')
inv('canceled vertex notation','deletion','x632–820 y750–791','omega(s)/w(s); u_omega/u')
inv('raised vertex notation','insertion','x779–829 y733–768','u_omega before baseline (s)')
inv('inverse-sigma edge label','insertion','x388–478 y801–893','sigma inverse (s), with curved leader after arête')
inv('canceled comme','deletion','x650–790 y856–882','comme, after qui ait')
inv('vertex conditions','display','right of definition, x1230–1570 y820–927','[(u_omega(s),sigma inverse(s))∈R, u_omega(s)≠s]')
inv('edge-step sketch','drawing','left margin, x62–279 y924–1114','sigma a; a; joint sigma u_omega(a); outgoing u_omega(a)')
inv('definition of edge successor','text','x275–1614 y922–1046','∀a∈A, soit u_omega(a) l’unique arc de S')
inv('edge conditions','display','x779–1633 y984–1125','[(sigma u_omega(a),a)∈R, … i.e. u_omega(a)≠a]')
inv('automorphism paragraph','text','x284–1550 y1110–1383','Alors u_omega:(S,A)–(S,A) est un autom')
inv('first-pair correction','deletion','x555–596 y1110–1167','R/B overwritten by A')
inv('left margin brace','margin note','x245–283 y1147–1289','right brace at the fold')
inv('canceled fait que','deletion','x839–1058 y1300–1373','fait que')
inv('equivalent condition one','display','x389–897 y1390–1451','1°) ∀s∈S, s lié à gs')
inv('equivalent condition two','display','x398–931 y1456–1516','2°) ∀a∈A, a lié à ga')
inv('order sentence','text','x306–1567 y1527–1594','Si n=card S=card A, l’ordre … est n')
inv('inequality and bijection paragraph','text','x282–1612 y1620–1879','fleche/flèche/et … sss n≠2 … or(S,A,R)')
inv('cyclic group paragraph','text','x307–1625 y1890–2135','Et le gpe/grpe cyclique … des autom … torseurs')
inv('canceled formé','deletion','x1520–1622 y1893–1981','formé')
inv('inserted le','insertion','x1542–1597 y1890–1930','le above cancellation')
inv('inserted group name','insertion','left, x201–391 y1955–2033','gpe G raised zero/circle, leader before des')
inv('inserted orientés','insertion','x599–757 y1952–2038','orientés, caret after autom')
inv('inserted tuple gloss','insertion','x976–1298 y1934–2059','lire/les/i.e. de S,A,R;omega), leader after base tuple')
inv('canceled final lead-in','deletion','x437–792 y2181–2230','Se/La donner un')
inv('last paragraph','text','x301–1638 y2242–2349','Torseur sous Z/nZ = ensemble … Se donner un contour')
inv('added n bound','insertion','x891–1056 y2184–2297','(n≥1), curved leader after Z/nZ')
inv('possible overwritten où','deletion','x1195–1258 y2247–2287','où beneath à, or reinforced à; state kept doubtful')
inv('raised cross or star','insertion','x632–670 y2300–2325','times/star before circulaire')
inv('archive foliation comment','margin note','lower left, x38–79 y2285–2341','archive 7, recorded only as a comment')

outcomes={
'01':'Resolve tte; compressed abbreviation, not expanded toute.',
'02':'Retain o/omega beneath live sigma.',
'03':'Retain both crossed-line doubts; recover sigma/tilde/arrow separately and the separator.',
'04':'Retain O/zero.',
'05':'Retain both canceled-expression doubts; live u_omega is interlinear.',
'06':'Retain canceled comme; place it after qui ait and the sigma insertion after arête.',
'07':'Resolve arc; preserve literal S.',
'08':'Read plain lowercase a, reinforced in ink; no recoverable separate underlying glyph and no witness difference.',
'09':'Retain R/B and dash/arrow doubts.',
'10':'Read canceled fait que, without s.',
'11':'Retain uncertain word; add unaccented fleche as primary literal possibility.',
'12':'Retain donc/alors.',
'13':'Resolve lowercase or.',
'14':'Retain avec/sur; no period after ens.',
'15':'Resolve right brace; mark compressed connector ou/dash doubtful; capital Et.',
'16':'Retain gpe/grpe.',
'17':'Resolve canceled formé; note interlinear le.',
'18':'Retain G zero/circle; gpe is a contraction, with insertion leader.',
'19':'Retain gloss doubt and add i.e. as an allowed candidate; preserve its placement and missing opening parenthesis.',
'20':'Read donner un; add Se/La doubt on first word.',
'21':'Retain possible où, now with deletion state explicitly uncertain against reinforced à.',
'22':'Resolve singular elément; first e lacks a separate acute.',
'23':'Retain raised cross/star; reject quotation marks. A small gray diffuse spot left of the raised sign differs in color from blue ink and is not transcribed as punctuation.'}
for m in manifest: m['outcome']=outcomes[m['id'].split('_')[0]]
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(
 scan='008',reader='R2',start_utc='2026-11-20T01:07:05.336007Z',end_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
 images_viewed=[f'/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-01_75_scan008{s}.jpg' for s in ('','_a','_b')],
 reading_file='out/readings/scan008/R2/reading.tex',crop_count=len(manifest),findings=findings,inventory=inventory,
 notation=[
 {'sign':'sigma','reading':r'\sigma','ink':'Low loop with prolonged upper right stroke; distinct from the rounded omega.','place':'opening; slanted note; inverse labels and formulas'},
 {'sign':'omega','reading':r'\omega','ink':'Two rounded lobes and inward curls, shrinking to a low wave in indices.','place':'first proposition and every u subscript'},
 {'sign':'1 after existential','reading':r'\exists1','ink':'Separate unbroken upright; no detached exclamation dot in the main condition.','place':'main condition; canceled margin remains less secure'},
 {'sign':'O/zero','reading':r'\unsure{O|0}','ink':'Round open-topped loop; identity unresolved.','place':'condition label'},
 {'sign':'zero/circle above G','reading':r'G^{\unsure{0|\circ}}','ink':'Small closed raised oval; only first occurrence marked, subsequent primary zero by convention.','place':'inserted group name and sous G at paragraph end'},
 {'sign':'blackboard Z','reading':r'\mathbb{Z}','ink':'Parallel/doubled diagonal and bar traces; H declared bold macro is equivalent encoding, not an error.','place':'cyclic group and final torsor'},
 {'sign':'orientation set name','reading':r'\operatorname{or}','ink':'Low o and short attached r, smaller than following capitals.','place':'bijection sentence'},
 {'sign':'condition labels','reading':r'1^{\circ},2^{\circ}','ink':'Separate small raised loop next to each numeral.','place':'two listed conditions and later reference'},
 {'sign':'inverse exponent','reading':'-1','ink':'Separate short minus followed by upright 1.','place':'sigma inverse; u omega inverse'},
 {'sign':'raised cross/star','reading':r'\unsure{{}^{\times}|{}^{*}}','ink':'Crossed raised strokes with thick junction, not paired quote ticks.','place':'before circulaire'}],
 abbreviations=[
 {'written':'tte','expansion':'toute'}, {'written':'i.e.','expansion':'id est'}, {'written':'Prop','expansion':'Proposition'},
 {'written':'autom','expansion':'automorphisme or automorphismes according to occurrence'}, {'written':'sss','expansion':'si et seulement si'},
 {'written':'ens','expansion':'ensemble'}, {'written':'équiv.','expansion':'équivalentes'}, {'written':'gpe / grpe','expansion':'groupe'},
 {'written':'card','expansion':'cardinal'}],
 notes=[
 'Entirely handwritten mathematical text. Title: Orientation d’un contour. Internal line: Réduction au cas connexe. Two live underlined Prop labels, one canceled Prop. No manuscript date or own page number. Archive 7 is only a comment.',
 'Page defines an orientation and successors of vertices and edges, states the two-orientation proposition and automorphism/inverse/order claims, relates orientations to automorphisms, and begins a torsor description ending with Se donner un contour.',
 'There are three left-margin oriented-arc drawings and one slanted A-to-S diagram. The H drawing supplement for this page was read and compared; its schematic geometry has no substantive discrepancy. C’s drawings and marginal brace were assigned explicitly to the left.',
 'Every original C doubt has an explicit retain/resolve row. S.json is empty, so no sweep statements require adjudication. New doubts are separated from original C doubts in the coverage mapping and findings.',
 'The author writes no secure lexical doubt word such as peut-être or question in the read text. The doubtful fleche word is kept as ink, without assigning it an editorial role. The raised end mark is a cross/star candidate rather than a secure question mark.',
 'The formulas and claims were transcribed before checking limited consistency. The complete two-orientation theorem and graph-automorphism characterization were read, not proved from this isolated page.',
 'Written irregularities preserved include arc de S, the unmatched closing brace after the condition numbers, and the unmatched closing parenthesis of the added S,A,R;omega) gloss.',
 'The final singular elément is retained, including absence of a separate first acute, despite à n. The gray diffuse point just left of the raised cross/star differs from the blue ink and was treated as a surface spot, not inserted punctuation.',
 'marked_in_H records explicit H uncertainty/illegibility, not merely an ordinary struck-state macro. Macro-only H alphabet differences and archive marker numbering are not counted as collation differences.'
 ],
 checks=[
 {'statement':'a∈A and u_omega(a) is called an arc de S','event_type':'domain consistency check','reasoning':'The opening labels each arête a as an element of A, and the later map is on (S,A). The edge-successor sentence nevertheless names S. The crop clearly has S.','outcome':'Written domain mismatch retained; no correction to A.'},
 {'statement':'u_-omega=u_omega^{-1}, order n, and u_omega≠u_-omega sss n≠2 i.e. n≥3','event_type':'finite-order consistency check','reasoning':'For an element of finite positive order n, equality with its inverse is equivalent to u^2=1 and hence n dividing 2. The displayed equivalence excluding only n=2 therefore presupposes n≥2. This isolated page does not state that bound in the sentence; the final n≥1 pertains to torsors.','outcome':'Conditionally consistent for n≥2; no added hypothesis or altered inequality. The written n≠2 and n≥3 were checked against the half and retained.'},
 {'statement':'(u_omega(s),sigma^{-1}(s))∈R and (sigma u_omega(a),a)∈R','event_type':'local type check','reasoning':'The marginal diagram makes sigma a bijection from A to S. The first pair is vertex/edge; the second is also vertex/edge if u_omega acts on A as the following map states. The second entry of the second pair was an open visual locus and the crop settles it as a.','outcome':'The displayed entries are locally compatible; no notation was normalized and no proof of existence was inferred.'}
 ],
 unresolved=[
 {'place':'overwritten origin sign','reading':'o','alternatives':'omega','confidence':'low'},
 {'place':'slanted margin canceled uniqueness','reading':'exists1','alternatives':'exists','confidence':'low'},
 {'place':'slanted margin canceled first variable','reading':'forall s in S','alternatives':'forall a in S','confidence':'low'},
 {'place':'condition label','reading':'O','alternatives':'0','confidence':'medium'},
 {'place':'first canceled successor expression','reading':'omega(s)','alternatives':'w(s)','confidence':'low'},
 {'place':'second canceled successor expression','reading':'u_omega','alternatives':'u','confidence':'low'},
 {'place':'canceled word after qui ait','reading':'comme','alternatives':'no securely distinguishable alternative','confidence':'low'},
 {'place':'overwritten first-pair letter','reading':'R','alternatives':'B','confidence':'low'},
 {'place':'map connector after first pair','reading':'dash','alternatives':'right arrow','confidence':'medium'},
 {'place':'word before inequality','reading':'fleche','alternatives':'flèche; et','confidence':'low'},
 {'place':'connective before omega map','reading':'donc','alternatives':'alors','confidence':'low'},
 {'place':'link after or(S,A,R)','reading':'avec','alternatives':'sur','confidence':'low'},
 {'place':'connector between condition numbers','reading':'ou','alternatives':'dash','confidence':'medium'},
 {'place':'group contraction','reading':'gpe','alternatives':'grpe','confidence':'medium'},
 {'place':'inserted G superscript','reading':'0','alternatives':'circle','confidence':'medium'},
 {'place':'opening of added tuple gloss','reading':'lire','alternatives':'les; i.e.','confidence':'low'},
 {'place':'first word of bottom canceled phrase','reading':'Se','alternatives':'La','confidence':'medium'},
 {'place':'dark unit after ensemble','reading':'canceled où beneath à','alternatives':'reinforced à without an independently recoverable cancellation','confidence':'low'},
 {'place':'raised sign before circulaire','reading':'times cross','alternatives':'star','confidence':'medium'}
 ],
 doubt_coverage=doubt_coverage,
 protocol={'whole_image_dimensions':[1694,2366],'views':{'whole':1,'first_half':1,'second_half':1},'half_b_original_y_offset':1103,'crop_manifest':'out/readings/scan008/R2/crop_manifest.json','all_crops_visually_inspected':True,'other_pages_or_readers_consulted':False,'ocr_or_web_used':False,'S_rows':0},
 coverage={'C_and_H':'Every prose line, display, correction, marginal element, and supplied H drawing checked against the relevant half; only open loci cropped.','crop_08':'Plain a settled; agreement not inflated into a findings row.','original_C_doubts':24,'doubt_rows':len(doubt_coverage),'inventory_elements':len(inventory),'mathematical_check_events':3}
)
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Findings:',len(findings),'inventory:',len(inventory),'C doubt dispositions:',len(doubt_coverage),'crops:',len(manifest))
