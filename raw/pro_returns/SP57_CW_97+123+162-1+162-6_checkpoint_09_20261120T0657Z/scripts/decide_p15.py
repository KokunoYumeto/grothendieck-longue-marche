"""Root's crop-adjudicated consolidation; no recognition or autonomous reading."""
import json,copy,re
from pathlib import Path
O=Path('out');stem='H162-01_162-1_scan004';P=O/'readers'/stem
R={r:json.loads((P/r/'report.json').read_text()) for r in ['R1','R2','R3']}
T={r:(P/r/'reading.tex').read_text() for r in R}
r1=f'readers/{stem}/R1/crops/';r2=f'readers/{stem}/R2/crops/';r3=f'readers/{stem}/R3/crops/';root=f'crops/{stem}/'
t=T['R2']
def rep(a,b,count=1):
 global t
 assert t.count(a)==count,(a,t.count(a));t=t.replace(a,b)
def between(s,a,b):
 return s[s.index(a):s.index(b,s.index(a))].rstrip()
rep(r'{infinitésimales};',r'{\unsure{infinitésimales}};')
rep(r'{\deleted{(pluriel)}};',r'{\deleted{(\unsure{pluriel})}};')
rep(r'{R. Wood};',r'{R. W\unsure{oo}d};')
rep(r'\node[anchor=center] at (556,1030) {\unsure{\begin{tikzpicture}[x=.0075cm,y=-.0075cm]\draw[line width=.35pt] (-10,10)--(16,-12);\end{tikzpicture}}};',r'\node[anchor=base west] at (549,1042) {\unsure{\begin{tikzpicture}[x=.0075cm,y=-.0075cm,baseline={(0,0)}]\draw[line width=.35pt] (0,0)--(12,-9);\end{tikzpicture}}};')
marktracks=between(T['R3'],r'% Two dark overlapping tracks',r'\node at (242,1158)')
rep(r'\node at (406,1106) {\unsure{1|2|?}};',r'\node at (406,1106) {\unsure{1|2|?}};'+'\n'+marktracks)
rep(r'\node[rotate=2] at (243,1153) {\deleted{(\unsure{suite|suiten})}};',r'\node[rotate=2] at (243,1153) {\resizebox{.99cm}{!}{\deleted{(\unsure{questions|suite|suiten})}}};')
a=t.index('% Local hatching');b=t.index('\\node at (531,1146)',a)
mesh=r'''% Repeated low loops and oblique returns; exact pen-lift segmentation is uncertain.
\node[anchor=north west,inner sep=0pt] at (244,1127) {\unsure{\begin{tikzpicture}[x=.0075cm,y=-.0075cm]
\path[use as bounding box] (0,0) rectangle (124,40);
\draw[line width=.65pt] (0,19) .. controls (23,16) and (66,13) .. (124,12);
\draw[line width=.6pt,opacity=.65] (6,13) .. controls (1,32) and (9,35) .. (19,16)
  .. controls (9,38) and (25,35) .. (34,17)
  .. controls (27,37) and (39,33) .. (48,15)
  .. controls (43,33) and (55,32) .. (65,13)
  .. controls (57,32) and (75,27) .. (86,11);
\end{tikzpicture}}};

'''
t=t[:a]+mesh+t[b:]
rep(r'{\deleted{\unsure{:|.}}};',r'{\deleted{\unsure{.|:}}};')
rep(r'{\deleted{Ch.}};',r'{\resizebox{.60cm}{!}{\deleted{\unsure{Ch.|Coh.}}}};')
rep(r'{\deleted{Vect.}};',r'{\resizebox{.70cm}{!}{\deleted{\unsure{V|v}ect.}}};')
rep(r'{\deleted{abéliennes}};',r'{\resizebox{1.45cm}{!}{\deleted{\unsure{abéliennes}}}};')
rep(r'\node at (1515,1108) {\deleted{$p\unsure{\ne|>}0$.}};',r'\node at (1515,1108) {\resizebox{.57cm}{!}{\deleted{$p\unsure{\ne|>}0$}}};')
serreline=next(s for s in t.splitlines() if s.startswith('\\draw') and '(531,1140)' in s)
terminal=between(T['R3'],'% Three short downward tracks',r'\node at (525,1198)')
rep(serreline,serreline+'\n'+terminal)
rep(r'\node at (554,1296) {\deleted{Weil :}};',r'\node at (554,1296) {\deleted{Weil}};'+'\n'+r'\node at (657,1296) {\deleted{\unsure{.|:}}};')
rep(r'\node at (958,1274) {\deleted{\unsure{intermédiaires}.}};',r'\node at (958,1274) {\resizebox{2.40cm}{!}{\deleted{\unsure{intermédiaires}}}};'+'\n'+r'\node at (1292,1258) {.};')
rep(r'{\deleted{\unsure{arithmétiques}}};',r'{\resizebox{2.23cm}{!}{\deleted{arithm\unsure{è|é|e}tiques}}};')
rep(r'{\deleted{Harder,}};',r'{\resizebox{1.19cm}{!}{\deleted{Hard\unsure{er,|y}}}};')
lower=between(T['R3'],'% Detached lower-left point',r'\end{tikzpicture}}')
old=between(t,'% Isolated lower-left point',r'\end{tikzpicture}}')
# The marker ends at the outer picture close; extract the complete nested node explicitly.
old=next(s for s in t.splitlines() if s.startswith('\\node[anchor=center] at (245,1763)'))
new=r'''\node[anchor=center] at (246,1764) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]
\fill (0,0) ellipse (.8 and .65);
\draw[line width=.4pt] (-.55,.15)--(-1.25,.28);
\end{tikzpicture}}};'''
rep(old,new)
# Fit especially long editorial alternatives within their source columns without redefining macros.
rep(r'{\unsure{Monsky-Washnitzer}};',r'{\resizebox{2.55cm}{!}{\unsure{Monsky-Washnitzer}}};')
rep(r'{f\unsure{o|u}nction};',r'{\resizebox{1.60cm}{!}{f\unsure{o|u}nction}};')
rep(r'{\deleted{\unsure{Rietzly|Rietzley}}};',r'{\resizebox{1.16cm}{!}{\deleted{\unsure{Rietzly|Rietzley}}}};')
rep(r'{\deleted{\unsure{Que|Qui}}};',r'{\resizebox{.55cm}{!}{\deleted{\unsure{Que|Qui}}}};')
# The physical gray appearance is retained as an approximation, not a medium identification.
for start in ['(563,1287)','(555,1440)','(551,1511)']:
 line=next(s for s in t.splitlines() if s.startswith('\\draw') and start in s)
 rep(line,line.replace('line width=.8pt','line width=.8pt,opacity=.65'))
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
spec=dict(stem=stem,brief='reader_v15.md',base_reader='R1',text_edits=[dict(old=T['R1'],new=t)],exclude_difference_ids=['D50'],difference_overrides={},additional_differences=[],main_new_crops=5,check_events=[])
D={d['id']:copy.deepcopy(d) for d in R['R1']['differences']}
def ov(n,**kw):
 id=f'D{n:02d}';D[id].update(kw);spec['difference_overrides'].setdefault(id,{}).update(kw)
def choice(n,readers,evidence,**kw):ov(n,readers=readers,evidence=evidence,**kw)
def line(start):return next(s for s in t.splitlines() if s.startswith('\\draw') and start in s)
def snip(a,b):return between(t,a,b)
choice(1,r'R1: \unsure{fonction|function}; R2: f\unsure{o|u}nction; R3: \unsure{function|fonction}. Root uses the locally doubtful vowel with o first.',
 'The first small body after the tall f closes or nearly closes into a loop, favouring o, while the thick junction permits u. The shorter nction sequence is visible and does not supply the extra letters of foundations.',final=r'f\unsure{o|u}nction')
ov(2,final=snip(r'\node at (1047,108)',r'\node at (533,170)'),c_changed=True,crop=r3+'01_top_title.png',
 evidence='Separate head and foot rules are visible on both Roman numerals. The elongated loop enclosing I has two distinct upper ends, so it is open rather than C’s closed circle. No insertion caret is present. A comma separates I and II.',
 readers='All three draw an open elongated loop. R1 treats it as equivalent to C’s circle; R2/R3 flag the open contour as changed. Root confirms the opening in the complete top crop and adopts the latter graphic distinction.')
choice(3,r'R1/R2: \unsure{Artin}; R3: Ar\unsure{ti}n. Root retains the whole-name doubt.',
 'A and final n survive clearly, but the overlapping r/t/i cluster is not fully separated. Narrowing to only ti would assert too much about the joined middle.')
choice(4,r'R1/R2: \unsure{Monsky-Washnitzer}; R3: Monsky-Washni\unsure{tz}er. Root retains the wider local name uncertainty.',
 'The M, main tall strokes and final ending survive; the first vowel after W and pale joined middle are also compressed, not only the tz group.')
for n,path,coords in [(6,'21_first_slash_hartshorne.png','(455,608)'),(9,'22_second_slash.png','(454,733)')]:
 ov(n,final=line(coords),crop=root+path,c_changed=True,kind='insertion or placement',
 evidence='A long independent diagonal rises from beside the following row to the start of the letter entry. The drawing preserves its spanning height and lower endpoint, which C’s baseline slash does not retain. H has no corresponding stroke.',
 readers='All three retain one rising stroke. R1/R3 call C’s slash equivalent; R2 distinguishes its spanning position. Root retains the R2 source-coordinate extent. For the second stroke R1 uses a shallow curve; root uses the nearly straight visible course.')
choice(7,r'R1: \unsure{lettres|lettre}; R2/R3: lettres. Root resolves lowercase plural.',
 'A small e turn after r is followed by a separate extended, down-hooked terminal s. The initial narrow l differs from the broad-footed capital L of the later entry.',final='lettres Hartshorne',c_changed=True,confidence='medium')
ov(8,crop=root+'21_first_slash_hartshorne.png',evidence='Two vertically separated small points follow Hartshorne. The source separator is a colon, not H’s comma; Affine duality remains unchanged.')
choice(10,r'R1: \unsure{Lettre|Lettres}; R2/R3: Lettres. Root resolves plural.',
 'After the tall t strokes and low r/e joins a further elongated hooked s is present. The initial L has a broad lower foot.',final='Lettres Quillen',c_changed=True,confidence='medium')
choice(11,r'R1/R3 retain \unsure{infinitésimales}; R2 resolves it. Root retains the doubt.',
 'The outer letters and long f/t survive, but pale central joins and the accent region are still reduced. The complete word cannot be given unqualified certainty.',final=r'\unsure{infinitésimales}',c_changed=False,h_changed=True)
choice(12,r'R1: \unsure{tapis|topis}; R2/R3: t\unsure{a|o}pis. Root localizes to a/o.',
 'The p descender and separate i dot exclude the second o of topos. The first vowel meets the cancellation and stays a/o.',final=r't\unsure{a|o}pis',c_changed=True)
choice(13,r'R1 keeps pluriel/Gabriel; R2 resolves pluriel; R3 has tentative pluriel. Root adopts R3’s uncertainty.',
 'An initial descender inside the parenthesis favours p, with a tall following loop; the covered inner joins keep pluriel tentative. A separate closing parenthesis precedes Quillen.',final=r'(\unsure{pluriel}) Quillen',c_changed=True,confidence='low')
ov(14,final=line('(527,779)'),readers='All three retain a continuous slightly rising path crossing the full Notes entry; root uses source-coordinate endpoints from R2, not R1’s typeset-node anchors.')
choice(15,r'R1: R. \unsure{Wood}; R2: R. Wood; R3: R. W\unsure{oo}d. Root localizes the two compressed round traces.',
 'A separate R and point precede W, two small round traces, and d. The two inner traces remain doubtful. No à occurs before Bourbaki and no comma follows it.',final=r'R. W\unsure{oo}d Bourbaki calcul différentiel',confidence='medium')
ov(17,crop=root+'23_extension_case.png',evidence='A tall upright and a broad square lower foot form capital L before the apostrophe. H’s lowercase form is not retained.')
choice(19,'R1 draws the first unit as an ellipse; R2/R3 as a short dash. R1/R2 separately darken the connected terminal endpoint; R3 does not. All have three disconnected units. Root adopts R2’s three-unit drawing.',
 'A short dark horizontal dash precedes a compact point and a longer pale shallow bow with a darker connected endpoint. These physical shapes do not establish an ellipsis or a sequence of three hyphens.',final=snip(r'\draw[line width=.45pt] (1332,947)',r'\node at (537,1007)'))
choice(21,r'R1/R2: Lecture Notes; R3: \unsure{Lecture} Notes. Root resolves Lecture and retains the blank separator.',
 'The tall L, low e/c, one t ascender and u/r/e continuation can be followed around the strike. Notes has capital N and there is no internal comma. The wide gap after Borel contains no colon.',
 C=r'\qquad Lecture Notes',H=': lettre, notes',final='Lecture Notes',place='Cancelled Borel title and preceding separator',confidence='high')
choice(22,'All three draw two separated main cancellation runs. R2 alone preserves an additional doubtful lower oblique trace at Borel. Root retains that trace but shortens it to the visible interval (549,1042)–(561,1033).',
 'The Borel cancellation ends near x621; the title cancellation begins near x688, leaving a gap. A small lower oblique trace is also visible beneath Borel; its affiliation with lettering or cancellation is uncertain.',
 final=snip(r'\draw[line width=.65pt] (535,1032)',r'% The divider'),confidence='medium',marked_in_H='no')
ov(23,final=snip(r'\draw[line width=.25pt] (244,1072)',r'% Deligne group'),crop=r2+'11_borel_separator.jpg',evidence='Two thin wavering runs are separated by a real gap near x713–735. C already records both; H omits the divider.')
choice(24,'R1/R2 retain only the same uncertain 1/2/? candidates; R3 additionally draws two overlapping tracks. Root retains the candidates plus both tracks, without chronology.',
 'A hooked/looped left track overlaps a taller nearly vertical dark track. These do not settle 1, 2 or question mark. Both physical tracks are retained. The recovered C prose note concerns this same question-mark alternative.',
 final=r'\node at (406,1106) {\unsure{1|2|?}};'+'\n'+marktracks,c_changed=True)
choice(25,r'R1 adds questions before suite/suiten; R2/R3 retain suite/suiten. Root keeps \unsure{questions|suite|suiten}.',
 'The early descending bowl and length of the covered run admit questions, but the mesh prevents a secure word. All alternatives remain tentative and the parenthesis remains below Deligne.',final=r'\unsure{questions|suite|suiten}',c_changed=True,confidence='low')
ov(26,readers='All three retain the parenthesis as deleted and below the Deligne heading; the word alternatives are separately adjudicated in D25.')
choice(27,'R1 draws a sweep and continuous looped mesh with about five low returns; R2 draws six schematic obliques plus terminal return inside an unsure graphic; R3 draws four obliques plus a sweep. Root retains the visible R1-type low loop contour with local graphic uncertainty, not a definite pen-lift count.',
 'Repeated low loops and oblique returns cross the small parenthesis, separately from its word. Their intersections do not securely establish individual passes or chronology; the approximate mesh is locally marked unsure.',final=mesh.rstrip(),confidence='medium')
choice(28,r'R1/R3 prefer .|:; R2 prefers :|. Root uses \unsure{.|:}.',
 'The low point is exposed; any upper punctuation falls on the heavy cancellation. A colon cannot be distinguished from a single point.',final=r'\unsure{.|:}',confidence='low')
choice(29,r'R1/R3: \unsure{Ch.|Coh.}; R2: Ch. Root retains both with Ch. first.',
 'C joins a tall h-like stem and a separate stop. No independent o chamber is secure, but a covered o is possible. H expands the abbreviation.',final=r'\unsure{Ch.|Coh.}')
choice(30,r'R1/R2: Vect.; R3: \unsure{V|v}ect. Root retains the local case doubt.',
 'The initial broad rounded V/v form is partly crossed. The remaining ect and stop precede Witt, with no written des or de.',final=r'\unsure{V|v}ect. Witt',c_changed=True,confidence='medium')
choice(31,r'R1/R2 give abéliennes without doubt; R3 has \unsure{abéliennes}. Root retains the whole-word doubt.',
 'The compact var. is followed by the abéliennes-like outline, tall stems and a high accent, but several inner joins meet the strike. The visible word does not give von Dieudonné.',
 final=r'var. \unsure{abéliennes}',c_changed=True,confidence='medium',crop=r3+'14_serre_right.png')
ov(32,C=r'en car $p\unsure{\ne|>}0$',final=r'en car $p\unsure{\ne|>}0$',
 evidence='The source has only car, without an abbreviation stop, before p. The crowded intersecting/angled relation and closed zero survive under cancellation. The relation remains ne/>; H expands car and stops at p. The terminal point’s state is recorded separately.',
 readers='All three retain car without a stop and the same ne/> alternatives plus zero. No mathematical expectation resolves the crossed sign.')
ov(34,final=serreline,crop=r3+'13_serre_left.png',evidence='One dark line rises through the whole Serre entry. R3 crops 13 and 14 jointly show its continuation through the word spaces and final condition; the terminal point lies separately below/right. Extra terminal tracks are recorded in ROOT-D59.',readers='All three retain one spanning rising path; root uses R2’s source-coordinate course. R1’s typeset-node anchor form is replaced by the actual coordinate path.')
choice(35,'All three use paired opening and closing quote strokes. R1 keeps them inline in a rotated whole node; R2/R3 place them independently high, especially the closing pair. Root retains the independent positions.',
 'The opening pair comprises two small curved strokes, and the closing pair is visibly raised above/right of the four continuation points. They are not guillemets. The title rises across the row; D36 separately records the four-point count.',
 final=snip(r'\node at (525,1200)',r'% An isolated point'),crop=r1+'15_monodromy_points.jpg',c_changed=True)
ov(38,H='chapitre',C='Chapin},',marked_in_H='no')
choice(39,r'R1: \unsure{class} field th\unsure{y|.}; R2/R3: \unsure{class} field thy. Root resolves y while retaining class.',
 'The initial cl survives but following small letters meet the strike. Field is readable. A real descending terminal after th is separate from the long cancellation, resolving y rather than a stop. H’s de familles is the corresponding undivided phrase.',
 final=r'\unsure{class} field thy',c_changed=True,confidence='medium',marked_in_H='no')
choice(40,'R1 starts the wave near x670 under the whole first name; R2/R3 start inside it near x698/702. Root adopts the latter placement.',
 'The separate thin wave starts inside the first name and continues under Chapin, below the independent long cancellation. C’s uwave spans the whole first name, and H omits the wave.',
 final=line('(698,1244)'),c_changed=True,kind='drawing or diagram',marked_in_H='no')
choice(41,r'R1/R3: Qui|Que; R2: Que|Qui. Root gives \unsure{Que|Qui}.',
 'The low final loop favours e and no secure separate i dot survives. The short word is independently cancelled; H has no corresponding entry. Its simple local stroke is covered here by the deletion state.',
 final=r'\deleted{\unsure{Que|Qui}}',c_changed=True,confidence='low')
choice(42,r'R1/R2: Weil :; R3: Weil \unsure{.|:}. Root retains R3’s local punctuation doubt.',
 'W, low e/i and a final tall l loop are readable. A low detached point follows; any upper point coincides with the strike. The rounded low point does not support H’s comma.',
 final=r'Weil \unsure{.|:} Jacobiennes',c_changed=True,crop=r2+'18_weil_jacobiennes.jpg',confidence='medium')
ov(43,final=r'\deleted{\unsure{intermédiaires}}',H='\\ill\\',confidence='low',evidence='Tall t/d-like strokes, dotted short letters and the ending survive but many body letters remain covered by the gray cancellation. The word remains doubtful and deleted. H leaves its corresponding unread tail outside the struck wrapper; the final point’s separate live state is recorded in ROOT-D58.',readers='All three retain the word uncertainty. R1/R2 include its following period in deletion; R3 separates the live point, adjudicated in ROOT-D58.')
ov(44,crop=root+'24_lower_paths.png',evidence='Upright 1 and two-lobed 3 sit within parentheses, with two distinct short lower rules. These are separate from the two long crossing paths.')
ov(45,final=line('(548,1368)')+'\n'+line('(548,1375)'),crop=root+'24_lower_paths.png',readers='All three preserve two principal long cancellation runs; their weights and endpoints differ schematically. Root uses the two visible R2 source-coordinate runs, independently of the short numeral underlines.')
ov(46,crop=root+'24_lower_paths.png',evidence='Initial L, the i/ch/t/en sequence and the low baum ending survive under the crossing. They do not give bibliothèque.')
ov(47,H='\\ill\\',crop=root+'24_lower_paths.png',evidence='The s/u/r group, long descending f and a/c/e/s are readable. H’s ill between bibliothèque and arithmétiques is this local unread word, not a doubt on the following adjective.')
choice(48,r'R1/R2: \unsure{arithmétiques}; R3: arithm\unsure{è|é|e}tiques. Root adopts R3’s local accent alternatives.',
 'The body sequence can be followed around the gray stroke. A short upper down-right trace favours grave, but could be acute or part of the adjacent tall loop, leaving è/é/e. H’s adjective itself is unmarked.',final=r'arithm\unsure{è|é|e}tiques',c_changed=True,marked_in_H='no')
choice(49,r'R1: \unsure{Harder|Hardy}\unsure{,}; R2: Harder,; R3: Hard\unsure{er,|y}. Root adopts the coupled R3 alternatives and merges R1 D50.',
 'Hard is readable; the following shallow bowl/rise and descending tail admit er with comma or a joined y. The comma is not independent of the ending choice. H’s undivided unread surname span can include that tail.',
 final=r'Hard\unsure{er,|y}',place='Final entry, surname and adjacent tail',H='\\ill\\',c_changed=True,confidence='medium')
ov(51,place='Weil entry, long curved cancellation',final=line('(563,1287)'),H=R['R2']['differences'][47]['H'],crop=root+'24_lower_paths.png',evidence='One broad gray line rises across Weil and Jacobiennes, flattens across part of the last word, then rises toward its right end. R1 crop 18 shows the complete terminal region. This row records only the Weil path; Artin and each following row have separate geometry entries.',readers='All three preserve one long Weil path. Root uses R2’s source-coordinate course with reduced opacity for the observed broad gray appearance; this does not identify the writing medium.',marked_in_H='no')
ov(52,final=next(s for s in t.splitlines() if s.startswith('\\node[anchor=center] at (1608,1156)')),crop=r3+'14_serre_right.png',evidence='A compact dark point near (1608,1156) is separate from the Serre stop and quotation marks. Its function and ink-versus-surface status remain uncertain.',readers='All three preserve one uncertain far-right point; their schematic sizes differ. Root retains the R2 position and compact mark.')
choice(53,'R1 draws a flattened ellipse; R2 a circle; R3 an ellipse with a short connected left spur. Root retains the visible spur with the oval.',
 'The lower-left crop shows a dark oval with a connected short left projection. Both are drawn together, without assigning a character, function, or deliberate-ink status.',final=new,crop=r3+'22_low_point.png')

def add(id,place,C,H,final,evidence,crop,kind='drawing or diagram',confidence='high',c_changed=True,h_changed=True,readers='All three agree; root confirms in the cited crop.',marked='no'):
 spec['additional_differences'].append(dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=crop,kind=kind,confidence=confidence,c_changed=c_changed,h_changed=h_changed,readers=readers,marked_in_H=marked))
add('ROOT-D54','Raynaud, separator after Mumford','Mumford .','Mumford,','Mumford .','One low detached point follows Mumford, with no descending comma tail. This is an internal separator, not an editorial list join.',r1+'01_theta_function.jpg',kind='misread symbol or index',c_changed=False)
add('ROOT-D55','Illusie, gap after Koszul',r'Koszul\quad 2 articles','Koszul, 2 articles','Koszul 2 articles','A blank interval separates the final l from 2 articles; no comma appears.',root+'25_koszul_separator.png',kind='text not on the page',c_changed=False)
x=R['R2']['differences'][42]
add('ROOT-D56','Lettre entry, long rising cancellation',x['C'],x['H'],line('(535,1227)'), 'A dark line rises across the whole Lettre entry and projects beyond thy. It is distinct from the thin low wave under the names; both witnesses encode state without this spanning geometry.',r1+'16_lettre_name.jpg',marked='no',readers='All three draw the long Lettre path. R1 does not separately report it; R2 does. Root retains the R2 source-coordinate extent.')
for id,ridx,place,crop in [('ROOT-D57',34,'Serre, terminal point outside cancellation',r1+'14_serre_relation.jpg'),('ROOT-D58',49,'Weil, terminal point outside cancellation',r1+'18_intermediaires.jpg')]:
 x=R['R3']['differences'][ridx]
 add(id,place,x['C'],x['H'],x['reading'],x['evidence'],crop,kind='deletion state (struck given live or live given struck)',confidence='medium',readers='R1/R2 put the point inside deleted text; R3 gives a separate live point. Root confirms the point beyond/below the crossing endpoint and adopts R3.',marked='yes' if id.endswith('58') else 'no')
x=R['R3']['differences'][33]
add('ROOT-D59','Serre, short overlapping terminal tracks',x['C'],x['H'],between(terminal,'% Three short downward tracks',r'\node at (1598,1110)'), 'Three short overlapping tracks remain at the relation/cancellation junction. They are reproduced as physical tracks without deciding which belong to the relation or cancellation, or their chronology.',r1+'14_serre_relation.jpg',confidence='medium',readers='R1/R2 omit separate terminal tracks; R3 draws three. Root retains the visible R3 tracks alongside the still-doubtful mathematical relation.')
for id,idx,coords,place in [('ROOT-D60',53,'(555,1440)','Lichtenbaum, long cancellation'),('ROOT-D61',54,'(551,1511)','Manin, long cancellation'),('ROOT-D62',56,'(563,1587)','Final entry, long cancellation')]:
 x=R['R2']['differences'][idx]
 add(id,place,x['C'],x['H'],line(coords),x['evidence'],root+'24_lower_paths.png',readers='All three preserve a spanning path at this row. Root uses the R2 source-coordinate course; its graphic distinction is separate from lexical readings and deletion state.',marked='no')

# Metadata is separately reconciled by a text-only auditor from root's stated decisions,
# then reviewed by root before finalization. No independent image authority is delegated.
mp=O/'decisions'/f'{stem}_metadata_proposed.json'
if mp.exists():
 meta=json.loads(mp.read_text());spec.update({k:meta[k] for k in ['c_doubts','inventory']})
else:
 spec['c_doubts']=copy.deepcopy(R['R1']['c_doubts']);spec['inventory']=copy.deepcopy(R['R1']['inventory'])
# Final evidence points to crops actually viewed by root; reader crops remain in their returns.
qcrops={1:r1+'01_theta_function.jpg',2:r3+'01_top_title.png',3:root+'21_first_slash_hartshorne.png',4:r1+'09_cot.jpg',5:r1+'10_pour_omega.jpg',6:r1+'15_monodromy_points.jpg',7:root+'24_lower_paths.png',8:r1+'14_serre_relation.jpg',9:r1+'01_theta_function.jpg',10:r1+'02_artin.jpg',11:r1+'03_monsky.jpg',12:r1+'04_lettres_hartshorne.jpg',13:r1+'05_lettre_quillen.jpg',14:r1+'06_infinitesimales.jpg',15:r1+'07_notes_tapis.jpg',16:r1+'07_notes_tapis.jpg',17:r1+'10_pour_omega.jpg',18:r1+'10_pour_omega.jpg',19:r1+'11_borel.jpg',20:r1+'12_deligne.jpg',21:r1+'12_deligne.jpg',22:r1+'13_serre_coh.jpg',23:r1+'15_monodromy_points.jpg',24:r1+'16_lettre_name.jpg',25:r1+'16_lettre_name.jpg',26:r1+'16_lettre_name.jpg',27:r1+'17_qui.jpg',28:r1+'18_intermediaires.jpg',29:r1+'19_arithmetiques.jpg',30:r1+'20_harder.jpg'}
for i,q in enumerate(spec['c_doubts'],1):
 q['crop']=qcrops[i]
 if i==28:q['evidence']='Root crop R1/18 shows the long cancellation across the tentative adjective and the final point beyond/below its endpoint. The word remains uncertain and deleted; the point remains live.'
for x in spec['inventory']:
 if 'detached point' in x['element'].lower():x['hand']='uncertain ink or surface mark; personal attribution not established'
 elif 'Archive numeral' in x['element']:x['hand']='unnamed archive annotator; personal attribution not established'
 else:x['hand']='principal manuscript hand; personal attribution not independently established'
 x['transcribed']='yes'
def ipos(x):
 m=re.search(r'\[(\d+),\s*(\d+),',x['position'])
 if m:return (int(m[2]),int(m[1]))
 if 'Borel' in x['element']:return (1033,549)
 return (9999,9999)
spec['inventory'].sort(key=ipos)
# Remaining doubts are expressed at the exact final scope, including separate graphic doubts.
rd=[]
def doubt(place,reading,alternatives,confidence='medium'):rd.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence))
for place,reading,alts,conf in [
('Raynaud title vowel',r'f\unsure{o|u}nction','o; u','medium'),('Artin-Winters first name',r'\unsure{Artin}','Artin; joined medial letters','medium'),('First Monsky-Washnitzer',r'\unsure{Monsky-Washnitzer}','candidate name; compressed joins','medium'),('Extensions adjective',r'\unsure{infinitésimales}','candidate adjective; pale middle and accent','medium'),('Cancelled Notes vowel',r't\unsure{a|o}pis','a; o','medium'),('Cancelled Notes parenthesis',r'\unsure{pluriel}','pluriel; covered joins','low'),('Bourbaki second word',r'W\unsure{oo}d','two compressed round traces','medium'),('Lower cot mark',r'\unsure{*|+}','star; plus','medium'),('Borel lower oblique trace','Short oblique inside an unsure graphic','letter trace; additional cancellation trace','low'),('Deligne adjacent mark',r'\unsure{1|2|?}','1; 2; question mark','low'),('Parenthesis below Deligne',r'\unsure{questions|suite|suiten}','questions; suite; suiten','low'),('Parenthetical mesh','Approximate looped mesh inside an unsure graphic','overlapping loops and oblique returns; exact pen lifts undetermined','medium'),('Serre separator',r'\unsure{.|:}','period; colon','low'),('Serre abbreviation',r'\unsure{Ch.|Coh.}','Ch.; Coh.','medium'),('Serre Vect initial',r'\unsure{V|v}ect.','capital V; lowercase v','medium'),('Serre adjective',r'\unsure{abéliennes}','abéliennes; crossed internal joins','medium'),('Serre condition',r'p\unsure{\ne|>}0','not equal; greater than','low'),('Lettre first name',r'\unsure{Rietzly|Rietzley}','Rietzly; Rietzley','low'),('Lettre English word',r'\unsure{class}','class; crossed middle','low'),('Short cancelled start',r'\unsure{Que|Qui}','Que; Qui','low'),('Weil separator',r'\unsure{.|:}','period; colon','low'),('Weil adjective',r'\unsure{intermédiaires}','intermédiaires; crossed middle','low'),('Lichtenbaum adjective accent',r'arithm\unsure{è|é|e}tiques','grave; acute; no accent','medium'),('Final surname and tail',r'Hard\unsure{er,|y}','Harder with comma; Hardy without separate comma','medium'),('Far-right detached point','Uncertain compact point near (1608,1156)','deliberate or accidental ink; surface mark','low'),('Lower-left detached point','Uncertain oval with connected left spur near (246,1764)','deliberate or accidental ink; surface mark','low')]:doubt(place,reading,alts,conf)
spec['remaining_doubts']=rd
spec['abbreviations']=copy.deepcopy(R['R3']['abbreviations'])
for x in spec['abbreviations']:
 if x['form']=='R.':x['expansion']='Unresolved initial or abbreviation; no full name or Rapport expansion is asserted.'
spec['notes']='''A handwritten list has three groups headed Raynaud, Illusie 1 and Deligne followed by an ambiguous 1/2/? mark. Entries name papers, letters and subjects; many are cancelled. The Griffiths preprint entry is live and ends in four physical continuation marks. No date or overall title is written. The archive numeral 3 is retained only in the required comment.

The source explicitly records I and II in two title entries, Koszul 2 articles and Manin (2 articles). Papiers d'Artin carries a doubly underlined (13), whose administrative or page-count meaning is not established. The top I is surrounded by an elongated open curve. The physical numeral rules, both left diagonals, the two-part divider, independent underlines, meshes and long cancellations are reproduced without inferring whether an item was returned or assigning stroke chronology.

C's doubts resolve to plural lettres and Lettres, pour, Borel, four continuation points after monodromy, and the terminal y of thy. The first vowel of fonction/function and the accent of arithmè/é/e-tiques remain local doubts. The crossed parenthesis below Deligne admits questions as well as suite/suiten. The final surname ending and comma remain coupled alternatives: Harder, or Hardy. The source's mark beside Deligne may itself be a question mark, but no definite authorial question or verbal hesitation is inferred from that uncertain mark.

The mathematical entries are titles or abbreviated subjects. Theta has a median bar; Omega has a raised 1; the intersecting mark after cot is lowered and remains star/plus. The Serre relation after p remains not-equal/greater-than, with a visible following zero. Neither a bibliographic expectation nor the meaning of characteristic selects the sign. These are glyph and placement decisions, not mathematical proof checks or computations.

Two terminal full stops, after the Serre condition and the Weil adjective, lie below/right of the cancelling strokes and remain live. H's unread span after Jacobiennes corresponds to the uncertain cancelled adjective and its tail, not to an absent whole entry. Its unread span before arithmétiques covers surfaces only. Editorial list-joining dashes and semicolons in H are excluded from source-punctuation differences; the actual separators after Mumford, Hartshorne, Koszul, Borel and Weil are compared individually. No external title, name, article count, or mathematical identity was researched.'''
spec['consequential']=[]
spec['workflow_note']='''Three fresh readers used v15 and each viewed the whole and both supplied halves once, then 20/21/22 tight crops respectively. Root compared all three complete texts and reports and the C questions, and used 20 existing R1 crops, two R2 crops, four R3 crops, and five new bounded crops. An oversized three-image output supplied no usable image evidence; all three images were subsequently displayed successfully one at a time. Text outputs that were truncated were reread in compact sections. Root did not view a whole image or half.

A fresh text-only auditor mapped all 169 reported difference rows to the consolidation scopes and checked literal witness fields and graphic inventory coverage; it had no image authority. It found missing apparatus scopes for common punctuation and the long Lettre cancellation, and highlighted local uncertainty and deletion-boundary differences. Root retained uncertain physical marks without assigning chronology. All C questions, including the recovered current-page prose sentence about the Deligne mark, receive dispositions.

R1 initially redefined the supplied deleted macro to suppress its standard strike. Root required removal before comparison; the final fragment uses the supplied macros unchanged and supplements state with source-coordinate paths. Structural validation now rejects page-level macro definitions. The next brief expressly forbids redefinition and requires state boundaries, local doubt and path counts to remain consistent between text, report and inventory. No mathematical proof event is claimed for visual reading of this list.'''
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
print(json.dumps(dict(preview=stem,base_loci=52,additional=len(spec['additional_differences']),remaining=len(rd),metadata_loaded=mp.exists())))
