from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path('/workspace/scratch/94548b74fbe0/out/readers/003/C')
crops = json.loads((ROOT / 'crop_index.json').read_text())
crop_by_name = {x['path']: x for x in crops}
differences = []

def add(id, location, C, H, reading, evidence, confidence='high', kind='other', diff_C=False, diff_H=True, status=None, crop=None, bbox=None, consequence=None):
    if bbox is None and crop is not None:
        bbox = crop_by_name[crop]['bbox']
    item = dict(id=id, location=location, C=C, H=H, reading=reading,
                evidence=evidence, confidence=confidence, kind=kind,
                diff_C=diff_C, diff_H=diff_H, C_doubt_status=status,
                readers_crop=crop, bbox={'image':'J81-01_81_scan003.jpg','xyxy':bbox})
    if consequence is not None:
        item['mathematical_consequence'] = consequence
    differences.append(item)

add('D01','Heading, inserted parenthesis',r'\inserted{(\unsure{orientée})}',r'\add{(orientée)}',r'\inserted{(orientée)}','The inserted word has o-r-i, a joined middle, a tall t, accented é and terminal e. The guide begins immediately after sphérique.', 'medium','other',True,False,'resolved','01_title_insertion.png')
add('D02','Heading, final word',r'\unsure{isotopique|isotopiques}','isotopiques',r'\unsure{isotopiques|isotopique}','After the descender of q, the low ending continues to a terminal downward curl. The final e/s division remains uncertain.','medium','other',True,True,'retained','02_title_category.png')
add('D03','The three left-hand separators',r'\rotatebox{90}{$\simeq$}',r'$\simeq$',r'\rotatebox{90}{$\simeq$}','Each separator has a wavy upright on the left and a straight upright on the right, at y about 150, 375 and 705.','high','misread symbol or index',False,True,None,None,[220,130,275,725])
add('D04','First text line, noun before projective lines',r'\unsure{morphisme}','morphismes',r'\unsure{morphisme|morphismes}','The opening m/o/r/p/h is retraced. The i dot and s-m-e continuation are visible; the terminal stroke does not separate a final s securely.','low','misread word',True,True,'retained','03_morphism.png')
add('D05','First formula, f-marked horizontal stroke',r'\overset{f}{\unsure{-|\longrightarrow}}',r'\xrightarrow{\ f\ }',r'\overset{f}{\unsure{-|\longrightarrow}}','A short horizontal stroke ends in a small raised thickening and downturned exit; a complete two-branch arrowhead cannot be separated.','medium','misread symbol or index',False,True,'retained','03_morphism.png')
add('D06','First formula, target subscript',r'\unsure{\mathrm C|\mathbb C}',r'\mathbb C',r'\mathrm C','The source subscript has a reinforced/doubled left stroke. The target is one open curved stroke, with no second downstroke.','high','misread symbol or index',True,True,'resolved','03_morphism.png')
add('D07','Quoted adjective after projective-line formula',r'``\unsure{spécial}''','“spécial”',r"``spécial''",'The quote ticks, p descender, accented é and final l are legible.','medium','other',True,False,'resolved','03_morphism.png')
add('D08','End of morphism line, i.e',r'i.e',r'i.e.',r'i.e','There is a dot between i and e; no terminal dot follows e in the visible line.','medium','other',False,True,None,'03_morphism.png')
add('D09','First conditions line, étale phrase','au dessus de','en dessus de','au dessus de','The small group preceding dessus is an a joined to u.','high','misread word',False,True,None,None,[1050,275,1510,355])
add('D10','Rational-function description, singular wording','fonction rationnelle ... telle que ... et telle que','fonctions rationnelles ... telles que ... et telles que','fonction rationnelle ... telle que ... et telle que','The noun and adjective have singular terminal strokes, and both occurrences of telle end with e before que.','high','misread word',False,True,None,None,[205,410,1725,555])
add('D11','Rational-function line, overwritten value of f(0)',r'f(0)=\deleted{\unsure{1}}0',r'f(0)=0',r'f(0)=\deleted{\unsure{1}}0','An older downstroke projects below and through the live oval 0; 1 remains a tentative reading of that predecessor.','low','omission',False,True,'retained','04_zero_value.png')
add('D12','Rational conditions, replacement of telle que',r'\deleted{telle que}\inserted{avec}',r'\struck{telle que}\uncertain{avec}',r'\deleted{telle que}\inserted{avec}','telle que has a through-stroke. The short word avec is written above it and reads a-v-e-c.','high','insertion or placement',False,True,None,'05_critical_conditions.png')
add('D13','Rational conditions, membership overwritten by exclusion',r'f(z)\deleted{\in}\notin\{0,\infty\}',r'f(z)\notin\{0,\infty\}',r'f(z)\deleted{\in}\notin\{0,\infty\}','Multiple older membership strokes remain below the heavily reinforced exclusion stroke.','medium','omission',False,True,None,'05_critical_conditions.png')
add('D14','Rational conditions, between finite-value set and f prime',r'\{0,\infty\}\ f\prime(z)=0',r'\{0,\infty\},\ f\prime(z)=0',r'\{0,\infty\}\ f\prime(z)=0','The closing brace is followed by the initial tall stroke of f prime; no comma occupies the gap.','high','other',False,True,None,None,[1360,510,1675,605])
add('D15','Rational conditions, before live value 1',r'f(z)\deleted{\in}=1',r'f(z)=1',r'f(z)\deleted{\in}=1','The original curved membership sign survives beneath the two horizontal equality strokes.','high','omission',False,True,None,'05_critical_conditions.png')
add('D16','Rational conditions, cancelled value set',r'\deleted{\unsure{\{0,1,\infty}}',r'\struck{\ill{}}',r'\deleted{\unsure{\{0,1,\infty}}','Diagonal cancellation strokes cross an opening brace and a compressed group with round, upright and infinity-like surviving parts. The entries remain tentative.','low',r'readable ink left as \ill{}',False,True,'retained','05_critical_conditions.png')
add('D17','Rational conditions, end of cancelled set',r'\unsure{$\}$|,}',r'within \struck{\ill{}}',r'\}','A tall final right brace remains clear to the right of the cancelled entries; its stroke is uncrossed.','high','deletion state (struck given live or live given struck)',True,True,'resolved','05_critical_conditions.png')
add('D18','Ramification parenthesis','en z','en un z','en z','The next physical line contains one en group followed immediately by z est 2.','high','misread word',False,True,None,'06_ramification.png')
add('D19','Polynomial description, opening noun','couple','couples','couple','The small final e ends the word immediately before the gap leading to P,Q; there is no additional s stroke.','high','misread word',False,True,None,None,[210,740,490,805])
add('D20','Polynomial description, f=P/Q insertion',r'couple P,Q \inserted{[f=P/Q !]} de',r'[f=P/Q !] couples P,Q',r'couple P,Q \inserted{[f=P/Q !]} de','The bracketed formula lies above de; its left guide curls down between Q and de.','high','insertion or placement',False,True,None,None,[420,675,875,810])
add('D21','Polynomial description, enclosure around de polynômes','de polynômes ...',r'(de polynômes ...)',r'de polynômes ...','The apparent left curve is the insertion guide for f=P/Q; no matching parenthesis encloses the phrase after C(z).','high','text not on the page',False,True,None,None,[515,725,1120,820])
add('D22','Polynomial description, argument delimiters',r'\mathbb C(z)',r'\mathbb C[z]',r'\mathbb C(z)','The left delimiter curves and the right delimiter is a bowed parenthesis. The written noun polynômes is preserved with this written notation.','high','misread symbol or index',False,True,'resolved',None,[900,745,1075,815], 'The transcription retains the visible round delimiters in the expression C(z).')
add('D23','Polynomial conditions, after P(0)=0',r'P(0)=0, (donc',r'P(0)=0 (donc',r'P(0)=0, (donc','A small comma-like curved downstroke occurs after the 0, before the opening parenthesis.','high','omission',False,True,None,None,[385,822,700,900])
add('D24','Degree parenthesis, respectivement abbreviation',r'\unsure{resp\textsuperscript{t}}',r'resp. !',r'resp\textsuperscript{t}','The descender of p is followed by one small raised t-like stroke; there is no separate baseline point and exclamation group.','medium','misread symbol or index',True,True,'resolved','07_respectivement.png')
add('D25','Degree parenthesis, punctuation after f(0)=0',r'f(0)=0, f(1)=1',r'f(0)=0 f(1)=1',r'f(0)=0, f(1)=1','A faint curved comma is visible below and to the right of the first 0; the second separator comma is darker.','medium','omission',False,True,None,'18_condition_punctuation.png')
add('D26','Beginning of normalization line',r'\unsure{normalisés}',r'normalisés',r'normalisés','The initial strokes remain legible beside the oblique note, and the ending is clearly -isés.','high','other',True,False,'resolved',None,[220,1015,460,1090])
add('D27','Oblique note, au lieu de cel(a)',r'\unsure{au lieu de cel|au lieu de cela}',r'\ill{}',r'\unsure{au lieu de cel|au lieu de cela}','au lieu de is separable after rotation. The last group has c-e and a tall final l-like stroke; a final a is not independently clear.','low',r'readable ink left as \ill{}',False,True,'retained','08_oblique_note.png')
add('D28','Oblique note, remaining readable wording',r'On pourrait aussi normaliser ... par Q(0)=1, ou P unitaire, ou Q unitaire\ldots',r'on pourrait \uncertain{aussi} normaliser \ill{} Q(0)=1 \ill{} \ill{}',r'On pourrait aussi normaliser ... par Q(0)=1, ou P unitaire, ou Q unitaire\ldots','The rotated lines show capital On, aussi normaliser, the linking par, and the two unitaire alternatives with P and Q. The final three dots are visible.','medium',r'readable ink left as \ill{}',False,True,None,'08_oblique_note.png')
add('D29','Normalization conditions, bracketed membership',r'f(z)\deleted{\in}\notin\{0,\infty\}',r'f(z)\notin\{0,\infty\}',r'f(z)\deleted{\in}\notin\{0,\infty\}','The bracketed f(z) condition has a retraced membership/exclusion sign, retaining the older curved membership strokes.','medium','omission',False,True,None,None,[745,1095,1010,1210])
add('D30','First fraction, cancelled Q(z)',r'\deleted{\unsure{Q(z)}}',r'no cancelled factor',r'\deleted{Q(z)}','A looped Q, curved parenthesis, z-like middle and closing parenthesis survive the slashes immediately beside P prime at numerator height. The fraction bar itself runs beneath P prime.','high','omission',True,True,'resolved','09_fraction_cancel.png')
add('D31','NB deduction, insertion anchor',r'donc si \inserted{pour ...} cette quantité',r'pour ... donc si cette quantité',r'donc si \inserted{pour ...} cette quantité','The guide begins in the gap immediately before cette; donc si remains to its left on the main baseline. The separator and trailing punctuation are recorded separately in D32–D33.','high','insertion or placement',False,True,None,'19_nb_insertion_punctuation.png')
add('D32','NB insertion, separator between P and Q',r'P(z);Q(z)\ne0',r'P(z),Q(z)\ne0',r'P(z);Q(z)\ne0','The separator has a distinct upper point and lower descending comma, forming a semicolon.','high','misread symbol or index',False,True,None,'19_nb_insertion_punctuation.png')
add('D33','NB insertion, trailing comma',r'pour P(z);Q(z)\ne0,',r'pour P(z),Q(z)\ne0,',r'pour P(z);Q(z)\ne0','After the zero there is blank space above the insertion guide; the right upturn belongs to that guide and is well below the line.','high','other',True,True,None,'19_nb_insertion_punctuation.png')
add('D34','NB deduction, punctuation after nulle',r'nulle, (i.e.',r'nulle (i.e.',r'nulle, (i.e.','A small descending comma follows the last e before the following parenthesis.','medium','omission',False,True,None,None,[980,1530,1285,1630])
add('D35','NB deduction, cancelled word after first P(z)=Q(z)',r'\deleted{\unsure{au|ou}}',r'\struck{\ill{}}',r'\deleted{\unsure{au|ou}}','The short crossed group has an initial oval and a following u-like sweep. The cancellation obscures the a/o distinction.','low',r'readable ink left as \ill{}',False,True,'retained','10_nb_cancel_word.png')
add('D36','NB deduction, i.e after cancelled word','i.e','i.e.','i.e','The abbreviation has its internal dot and a terminal e curve, with blank space before Q(z).','medium','other',False,True,None,'10_nb_cancel_word.png')
add('D37','NB deduction, emphasized condition',r'donc \uline{si}',r'donc si',r'donc \uline{si}','A separate short horizontal line lies directly below si.','high','other',False,True,None,None,[215,1825,430,1910])
add('D38','Question, parenthetic introduction',r'\unsure{d’où|donc}',r"d'où",r"d'où",'A separate apostrophe follows d; the following low ou group and its small raised accent are visible before aussi.','medium','other',True,False,'resolved','11_question_insert.png')
add('D39','Question, wording and anchor of inserted equality',r'Q\prime(z)=0) \inserted{avec P\prime(z)=Q\prime(z)}',r'P(z)=Q(z) \add{donc P\prime(z)=Q\prime(z)}. Mais ... \ill{}',r'Q\prime(z)=0) \inserted{avec P\prime(z)=Q\prime(z)}','The inserted word begins with a rounded a and low v-e-c continuation. Its guide descends to the question line immediately after the parenthetic Q prime equals 0; the main-baseline point after the earlier P=Q remains before Mais.','high','insertion or placement',False,True,None,'11_question_insert.png')
add('D40','Question, hook after inserted equality',r'\unsure{$\}$|)}',r'\ill{}',r'\unsure{\}|)}','A distinct curved descending stroke, with a middle cusp and lower rightward sweep, stands beside the insertion guide. Brace is strongest; a distorted parenthesis remains possible.','low',r'readable ink left as \ill{}',False,True,'retained','11_question_insert.png')
add('D41','Cancelled line before Prenons, verb',r'\deleted{\unsure{Réfléchissons}}',r'\struck{Prenons}',r'\deleted{\unsure{Réfléchissons}}','The cancelled first word includes a tall descending f-like stroke and a later ascender; several intervening letters are covered by the long cancellation.','low','misread word',False,True,'retained','12_cancelled_start.png')
add('D42','Cancelled line before Prenons, particle',r'\deleted{\unsure{à}}',r'no particle',r'\deleted{\unsure{à}}','A small loop-like group precedes Q(T), adjoining its left stroke; à remains tentative.','low','omission',False,True,'retained','12_cancelled_start.png')
add('D43','Prenons line, polynomial argument',r'Q(\unsure{T})=1',r'Q=1',r'Q(T)=1','The parenthesis and crossbar/upright of T survive the reinforced equality area.','medium','omission',True,True,'resolved','13_example_opening.png')
add('D44','Prenons line, conditions abbreviation',r'\unsure{cond\textsuperscript{ns}}',r'conditions',r'cond\textsuperscript{ns}','The short word has cond followed by a compressed raised ns ending.','medium','abbreviation expanded or spelling modernised',True,True,'resolved','13_example_opening.png')
add('D45','Degree-condition insertion, singular word',r'(conséquence des deux précédentes)',r'(conséquences des deux précédentes)',r'(conséquence des deux précédentes)','The word ends at the final e sweep before des; the plural -s stroke is absent.','medium','misread word',False,True,None,'14_degree_and_factor.png')
add('D46','Degree-condition insertion, anchor',r'\deg P\ge1 \inserted{(conséquence des deux précédentes)}',r'\inserted{(conséquences des deux précédentes)} P(0)=0, P(1)=1, \deg P\ge1',r'\deg P\ge1 \inserted{(conséquence des deux précédentes)}','The left end of the long insertion guide curls down just after the written 1 and before the comma introducing donc.','high','insertion or placement',False,True,None,'14_degree_and_factor.png')
add('D47','Factorization after donc, purported extra cancellation',r'P(T)=\unsure{T}P_0(T)',r'\struck{P(T)=} P(T)=T P_0(T)',r'P(T)=\unsure{T}P_0(T)','The available space contains one P(T)= group followed by one heavily retraced factor and P_0(T). There is no second complete P(T)= group.','medium','text not on the page',False,True,None,'14_degree_and_factor.png')
add('D48','Factorization after donc, reinforced factor',r'\unsure{T}',r'T',r'\unsure{T}','A top bar and upright remain in the dark reinforced sign before P_0(T). T is the supported candidate, but the overtracing prevents a fully secure reading.','medium','other',False,True,'retained','14_degree_and_factor.png')
add('D49','Last question, insertion pour P(z) nonzero',r'on peut avoir \inserted{(pour P(z)\ne0)} P\prime(z)=0',r'où on a \add{(pour P(z)\ne0)} P_0(1)=1',r'on peut avoir \inserted{(pour P(z)\ne0)} P\prime(z)=0','The guide extends over the end of on peut avoir and descends at that line end, before the following-line P prime equals 0.','high','insertion or placement',False,True,None,None,[1195,2220,1555,2320])
add('D50','Last paragraph, certes',r'certes',r'\uncertain{certes}',r'certes','The c, joined er, tall t and terminal es can be followed without cancellation.','high','other',False,True,None,'15_example_ending.png')
add('D51','Bottom line, cancelled trial polynomial',r'\deleted{P(T)=T^2}',r'omitted',r'\deleted{P(T)=T^2}','The crossed expression shows P(T), an equality, T and raised 2 before the live si.','high','omission',False,True,None,'15_example_ending.png')
add('D52','Sideways note, text after derivative',r'P\prime(T)=2aT+b qui est nul ... pour z=...',r'P\prime(T)=2aT+b, z=...',r'P\prime(T)=2aT+b qui est nul ... pour z=...','The upright crop clearly exposes qui est nul and pour on the first baseline; the witness commas replace these words.','high','omission',False,True,None,'16_sideways_note.png')
add('D53','Sideways note, a nonzero insertion',r'qui est nul \inserted{(supposons a\ne0)} pour',r'after the value calculation: (a\ne0,b\ne0)',r'qui est nul \inserted{(supposons a\ne0)} pour','The parenthetic supposons a nonzero is written above pour, with a guide whose left end descends immediately before pour.','high','insertion or placement',False,True,None,'16_sideways_note.png')
add('D54','Sideways note, cancelled sera',r'\deleted{\unsure{sera}}',r'omitted',r'\deleted{\unsure{sera}}','The crossed short word after -b/(2a) has an s-like beginning and an era-like continuation; the strike remains too heavy for certainty.','low','omission',False,True,'retained','16_sideways_note.png')
add('D55','Sideways note, two-zero condition',r'\ne\{0;-b/a ... les deux zéros de P si b\ne0,',r'omitted except a displaced b\ne0',r'\ne\left\{\begin{smallmatrix}0\\-\frac ba\end{smallmatrix}\right. ... les deux zéros de P si b\ne0,','A visible not-equals precedes a left brace with stacked 0 and -b/a. The following words les deux zéros de P and si b nonzero are legible.','high','omission',False,True,None,'16_sideways_note.png')
add('D56','Sideways note, blacked word before les deux zéros',r'\deleted{\illegible{1}}',r'omitted',r'\deleted{\illegible{1}}','A dense wedge and one projecting downstroke cover one word-sized space. No continuous letter sequence survives.','low','omission',False,True,'retained','16_sideways_note.png')
add('D57','Sideways note, lead-in to concluding condition',r'qui \deleted{\unsure{peut être}} est \ne1',r'; prenons une valeur \ill{}',r'qui \deleted{\unsure{peut être}} est \ne1','The next baseline starts qui, followed by a struck group with p and t/être-like strokes, then live est and not-equals 1.','low','misread word',False,True,'retained','17_sideways_continuation.png')
add('D58','Sideways note, cancelled phrase before si',r'\deleted{\unsure{en prenant}}',r'\ill{}',r'\deleted{\unsure{en prenant}}','Two word-sized traces lie under the long strike before si; the second retains a descending stroke and a sequence consistent with prenant. Crossing main-text strokes prevent certainty.','low',r'readable ink left as \ill{}',False,True,'retained','17_sideways_continuation.png')
add('D59','Sideways note, last condition and dash',r'si b^2\ne-4a\unsure{---}.',r'\ill{}',r'si b^2\ne-4a---','The lowest baseline shows si, b with raised 2, not-equals, minus, 4a, and a separated horizontal dash. No following full stop is visible.','high','other',True,True,'resolved','17_sideways_continuation.png')
add('D60','Sideways note, connective before value calculation',r'si b\ne0, et P(-b/(2a))=...',r'z=-b/(2a), P(-b/(2a))=...',r'si b\ne0, et P(-b/(2a))=...','The next baseline begins si b nonzero, followed by a comma and the word et before P.','high','omission',False,True,None,'16_sideways_note.png')

doubts = [
    dict(location='Heading final word',reading='isotopiques',alternatives=['isotopique'],confidence='medium',reason='The low terminal ending does not isolate a final s.',crop='02_title_category.png'),
    dict(location='Noun before projective-line formula',reading='morphisme',alternatives=['morphismes'],confidence='low',reason='Opening retracing and compressed terminal strokes.',crop='03_morphism.png'),
    dict(location='f-marked stroke between projective lines',reading='horizontal stroke',alternatives=['right arrow'],confidence='medium',reason='The right-end thickening does not give a complete arrowhead.',crop='03_morphism.png'),
    dict(location='Overwritten f(0) value in rational-function line',reading='deleted 1 before 0',alternatives=[],confidence='low',reason='Old downstroke survives but the numeral is overdrawn.',crop='04_zero_value.png'),
    dict(location='Cancelled value set after f(z)=1',reading='{0,1,infinity',alternatives=[],confidence='low',reason='Diagonal cancellation crosses the internal entries; final brace is clear separately.',crop='05_critical_conditions.png'),
    dict(location='Oblique normalization note',reading='au lieu de cel',alternatives=['au lieu de cela'],confidence='low',reason='No secure final a can be separated after l.',crop='08_oblique_note.png'),
    dict(location='Cancelled word after NB P(z)=Q(z)',reading='au',alternatives=['ou'],confidence='low',reason='The through-stroke obscures the initial oval.',crop='10_nb_cancel_word.png'),
    dict(location='Question close after inserted equality',reading='right brace',alternatives=['right parenthesis'],confidence='low',reason='The extra curved stroke intersects the insertion guide.',crop='11_question_insert.png'),
    dict(location='Cancelled line before Prenons, verb',reading='Réfléchissons',alternatives=[],confidence='low',reason='Long strike traverses the compressed letters.',crop='12_cancelled_start.png'),
    dict(location='Cancelled line before Prenons, particle',reading='à',alternatives=[],confidence='low',reason='Small loop is joined to the initial Q stroke.',crop='12_cancelled_start.png'),
    dict(location='Factor immediately before P_0(T)',reading='T',alternatives=[],confidence='medium',reason='Top bar and upright are heavily reinforced.',crop='14_degree_and_factor.png'),
    dict(location='Sideways note after z=-b/(2a)',reading='sera',alternatives=[],confidence='low',reason='The latter letters lie under a heavy cancellation.',crop='16_sideways_note.png'),
    dict(location='Sideways note before les deux zéros',reading='one physically unreadable cancelled word',alternatives=[],confidence='low',reason='Opaque wedge with no continuous surviving letter sequence.',crop='16_sideways_note.png'),
    dict(location='Sideways note after qui',reading='peut être',alternatives=[],confidence='low',reason='Cancellation and crossing main-text strokes obscure portions.',crop='17_sideways_continuation.png'),
    dict(location='Sideways note before final si',reading='en prenant',alternatives=[],confidence='low',reason='Long bar and perpendicular main-text writing cross the phrase.',crop='17_sideways_continuation.png'),
]

inventory = []
def inv(element,kind,position,first,hand='his hand',sheet='text'):
    inventory.append(dict(sheet_kind=sheet,hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))

inv('Heading','text','top, x190–1630 y65–180','Carte sphérique ... avec repère')
inv('Heading parenthesis','insertion','top, x580–770 y20–80; attached after sphérique','(orientée)')
inv('First separator','display','left x225 y140–165','vertical equivalent-like separator')
inv('Morphism description','text','x190–1135 y175–270','morphisme ... P^1_C ... spécial i.e')
inv('Morphism conditions','display','x355–1755 y280–355','f(0)=0, f(1)=1, f(infinity)=infinity')
inv('Second separator','display','left x225 y355–390','vertical equivalent-like separator')
inv('Rational-function description','text','x210–1760 y415–690','fonction rationnelle f(z) telle que')
inv('Old f(0) value','deletion','x1340–1390 y440–515','tentative 1 below live 0')
inv('Old telle que','deletion','x1040–1235 y505–560','telle que')
inv('avec replacement','insertion','x1150–1235 y500–525','avec')
inv('First old membership','deletion','x1370–1400 y520–575','membership below exclusion')
inv('Old membership before 1','deletion','x650–695 y585–625','membership below equality')
inv('Old finite-value set','deletion','x735–895 y570–630','{0,1,infinity')
inv('Surviving right brace','text','x900–920 y570–640','right brace after cancelled set')
inv('et de plus','insertion','x935–1230 y540–625','et de plus, attached before f double prime')
inv('Third separator','display','left x225 y690–725','vertical equivalent-like separator')
inv('Polynomial pair and conditions','text','x210–1760 y750–1005','couple P,Q de polynômes')
inv('Quotient identification','insertion','x530–850 y680–795','[f=P/Q !], attached after P,Q')
inv('Common-zero explanation','insertion','x1220–1750 y695–795','(i.e. sans zéros communs), attached after entre eux')
inv('Oblique normalization note','margin note','left x15–420 y950–1335; slanted','On pourrait aussi normaliser ...')
inv('Normalization and critical-point conditions','text','x210–1660 y1030–1210','normalisés (par exemple) par P(1)=Q(1)=1')
inv('Second old membership','deletion','x875–915 y1120–1175','membership below exclusion within brackets')
inv('P(z) nonzero','insertion','x1350–1550 y1095–1190','P(z) nonzero, attached before Q(z) nonzero')
inv('First logarithmic-derivative equation','display','x210–795 y1230–1365','P prime/P minus Q prime/Q equals 0')
inv('Cancelled Q(z) factor','deletion','x315–400 y1245–1300','Q(z) at numerator height')
inv('Condition after first equation','text','x840–1705 y1280–1390','on ait P(z)=Q(z), et de plus')
inv('Second-derivative condition','display','x410–1170 y1360–1435','P double prime/P minus Q double prime/Q nonzero')
inv('NB opening','text','x195–470 y1435–1490','[ NB on a')
inv('NB identity','display','x545–1740 y1430–1525','Q(z)P prime(z)-P(z)Q prime(z)=')
inv('Original right-hand side','deletion','x1040–1730 y1450–1525','Q(z)[P prime(z)-P(z)]+P(z)(Q(z)-Q prime(z))')
inv('Replacement right-hand side','insertion','x1030–1735 y1395–1470','(Q(z)-P(z))P prime(z)+P(z)(P prime(z)-Q prime(z))')
inv('NB deductions','text','x215–1675 y1540–1905','donc si cette quantité est nulle ...')
inv('Nonzero restriction','insertion','x430–800 y1500–1565','pour P(z);Q(z) nonzero, attached after donc si')
inv('Cancelled connective','deletion','x430–515 y1660–1700','au/ou')
inv('Underlining of si','underlining','x360–410 y1870–1895','si')
inv('Author question','text','x225–1660 y1860–2010','Mais peut-on avoir P prime(z)=0 ... ?')
inv('Equality qualification','insertion','x875–1215 y1905–2010','avec P prime(z)=Q prime(z), attached in the question')
inv('Question closing stroke','text','x1040–1085 y1940–2000','right brace/right parenthesis')
inv('Cancelled initial attempt','deletion','x230–640 y2055–2110','Réfléchissons à Q(T)=')
inv('Polynomial example','text','x230–1550 y2090–2445','Prenons p.ex. Q(T)=1 ...')
inv('Degree explanation','insertion','x775–1365 y2135–2220','(conséquence des deux précédentes), after degree at least 1')
inv('Last nonzero restriction','insertion','x1200–1550 y2235–2320','(pour P(z) nonzero), after on peut avoir')
inv('Cancelled quadratic trial','deletion','x235–455 y2390–2440','P(T)=T squared')
inv('Sideways calculation','margin note','left x20–255 y1500–2440; written from bottom toward top','P prime(T)=2aT+b qui est nul ...')
inv('a nonzero assumption','insertion','sideways note, x20–95 y1660–1940','(supposons a nonzero), before pour')
inv('Cancelled sera','deletion','sideways note, x90–125 y2160–2270','sera')
inv('Blacked marginal word','deletion','sideways note, x90–145 y1900–1975','one unreadable word')
inv('Cancelled peut être','deletion','sideways note, x190–240 y2130–2310','peut être')
inv('Cancelled en prenant','deletion','sideways note, x210–250 y1790–2100','en prenant')
inv('Archive sheet number','text','left x40–70 y1415–1455','2, recorded only as a comment',hand='another unnamed hand')

notes = {
    'page_content':'One handwritten page giving successive descriptions of a spherical map with a repère, followed by polynomial restrictions, an NB identity and deduction, an author question, and a quadratic example continued sideways in the left margin.',
    'author_own_uncertainty':[
        r"Mais peut-on avoir $P'(z)=0$ (d'où aussi $Q'(z)=0$) \inserted{avec $P'(z)=Q'(z)$}$\unsure{\}|)}$ sans avoir $P(z)=Q(z)$ ?",
        r"la question devient si on peut avoir \inserted{(pour $P(z)\ne0$)} $P'(z)=0$ sans avoir $P(z)=1$"
    ],
    'title_date_page_counts':{'heading':'Carte sphérique (orientée) avec repère (dans cat. isotopiques|isotopique)','date':'none visible','manuscript_page_number':'none visible','archive_sheet_number':'2','pages_read':1,'whole_image_views':1,'half_a_views':1,'half_b_views':1,'margin_notes':2,'drawings_or_diagrams':0},
    'mathematics_led_reading_decisions':[
        'The round delimiters in C(z) are retained even though the adjacent noun is polynômes.',
        'Every prime and second prime in the two derivative tests and in the NB was read separately; the written expressions are retained.',
        'Both visible right-hand sides of the NB expand to the same left-hand side. The cancelled predecessor and its inserted replacement are both preserved.',
        'The sideways rational expression ends in -b^2/(4a), matching its visible factors. The written question and restrictions remain the author’s text.'
    ],
    'layout_and_state':[
        'The cancellation through the finite-value set stops before the clear final right brace; reading.tex preserves that uncovered brace.',
        'The cancelled Q(z) sits immediately to the right of P prime at numerator height. The source fraction bar runs only below P prime; the semantic numerator transcription follows the supplied convention.',
        'The NB replacement is physically above the crossed RHS; reading.tex places predecessor immediately before replacement and records the vertical placement in a comment.',
        'The NB has a written opening square bracket. No matching closing square bracket is visible on this page.',
        'The curly stroke after the question insertion remains explicit doubt, separate from the preceding parenthesis and insertion guide.',
        'H’s explanatory note about the NB contains the cancelled RHS and describes its placement; its macro packaging adds no separate reading difference.',
        'The bottom main-text line reaches the damaged page edge. The final on a is legible, and the adjacent sideways note supplies the continued calculation.',
        'Reader label C here is an independent reader label, distinct from witness C.'
    ]
}

notation = [
    dict(location='Three left separators',sign='wavy upright left, straight upright right',latex=r'\rotatebox{90}{$\simeq$}'),
    dict(location='First formula',sign='two-stem projective P and raised 1',latex=r'\mathbb P^1'),
    dict(location='First formula source; later fields',sign='reinforced/doubled left side of C',latex=r'\mathbb C'),
    dict(location='First formula target',sign='single curved C',latex=r'\mathrm C'),
    dict(location='First formula arrow position',sign='short f-marked horizontal stroke with uncertain head',latex=r'\overset f{\unsure{-|\longrightarrow}}'),
    dict(location='Throughout equations',sign='z with straight or rounded lower exit; individually raised primes',latex=r'z, f\prime(z), f\prime\prime(z), P\prime(z), Q\prime(z)'),
    dict(location='Polynomial pair',sign='round delimiters around z',latex=r'\mathbb C(z)'),
    dict(location='Degree conditions',sign='resp with small raised t',latex=r'resp\textsuperscript{t}'),
    dict(location='Example opening',sign='cond with contracted raised ns',latex=r'cond\textsuperscript{ns}'),
    dict(location='Example factorization',sign='small lowered 0 after P',latex=r'P_0(T)'),
    dict(location='Sideways zero comparison',sign='not-equals followed by an open left brace and two stacked entries',latex=r'\ne\left\{\begin{smallmatrix}0\\-b/a\end{smallmatrix}\right.'),
    dict(location='Throughout prose',sign='abbreviations retained as written',latex=r'cat.; i.e / i.e.; NB; p.ex.; \deg'),
]

checks = [
    dict(statement=r'Q(P\prime-P)+P(Q-Q\prime)=QP\prime-QP+PQ-PQ\prime=QP\prime-PQ\prime; (Q-P)P\prime+P(P\prime-Q\prime)=QP\prime-PP\prime+PP\prime-PQ\prime=QP\prime-PQ\prime',location='NB cancelled and replacement right-hand sides',type='manual algebraic expansion',result='Both visible expressions yield the written left-hand side; both were retained.'),
    dict(statement=r'(-b/(2a))(-b/2+b)=-b^2/(4a)',location='Sideways quadratic calculation',type='manual rational-expression multiplication',result='The written product and final fraction agree as rational expressions; denominator 4a retained.')
]

report = dict(
    scan='003',reader='C',start_utc='2026-11-20 09:02:32 UTC',
    end_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    full_image_viewed=True,halves_viewed=True,complete_visual_read=True,
    differences=differences,doubts=doubts,inventory=inventory,notes=notes,
    notation=notation,check_events=checks,crops=crops,
    brief_feedback=[
        'The sideways continuation extends beyond the narrow marginal strip into the main text. Crop 16 exposed the first three baselines and clipped the lowest continuation; crop 17 covers those distinct lowest baselines. No settled locus was re-enlarged.',
        'The uncrossed final brace of a cancelled set, and the fraction-bar span beneath a cancelled adjacent factor, have no dedicated macro. Their visible state and placement are recorded explicitly above.',
        'Witness H has full text for its page 2. Its page label was treated as the supplied witness mapping, not as a manuscript page number.'
    ]
)
(ROOT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(differences),'doubts':len(doubts),'inventory_elements':len(inventory),'crops':len(crops),'end_utc':report['end_utc']},ensure_ascii=False))
