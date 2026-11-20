import json
from pathlib import Path
base=Path('out/readers/H162-01_162-1_scan004/R1')
Ctext=Path('packets/H162-01_162-1_scan004/C.tex').read_text()
Htext=Path('packets/H162-01_162-1_scan004/H.tex').read_text()
Rtext=(base/'reading.tex').read_text()
crops={}
for line in (base/'crops/crop_manifest.jsonl').read_text().splitlines():
 d=json.loads(line); crops[d['dest'].removesuffix('.jpg')]=d
D=[]
def add(id,place,C,H,reading,evidence,confidence,kind,c_changed,h_changed,crop=None,bbox=None,marked=False):
 if C and C not in Ctext: raise ValueError('C substring '+id+': '+repr(C))
 if H and H not in Htext: raise ValueError('H substring '+id+': '+repr(H))
 if crop: bbox=crops[crop]['box']
 D.append(dict(id=id,place=place,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked,c_changed=c_changed,h_changed=h_changed,crop=('readers/H162-01_162-1_scan004/R1/crops/'+crop+'.jpg') if crop else None,bbox=bbox,bbox_source='whole image, 1681 x 2138 pixels'))
def rpart(start,end):
 return Rtext[Rtext.index(start):Rtext.index(end,Rtext.index(start))].strip()
add('D01','Raynaud title, word following Theta',r'\unsure{function|fonction}',r'foundations',r'\unsure{fonction|function}',
 'The crop shows a tall f, a closed first vowel loop and a short joined middle, then dotted i and a low ending. The closed loop favours o; the compressed joins leave function possible. The longer sequence foundations is not present.', 'medium','misread word',True,True,'01_theta_function')
add('D02','Raynaud title, circled I and following II',r'\textcircled{\scriptsize $\overline{\underline{\mathrm I}}$}, $\overline{\underline{\mathrm{II}}}$',r'\add{I}, II',
 rpart(r'\node (ri)',r'\node (kiehl)'),
 'One upright has independent head/foot rules and is enclosed by an elongated oval; the following two uprights share upper/lower rules. There is a comma between them. The oval is an enclosure, without an insertion leader. C already records the circle and rules; the new coordinates only render their shape.', 'high','drawing or diagram',False,True,'01_theta_function')
add('D03','Raynaud third item, Artin',r'\unsure{Artin}',r'Artin',r'\unsure{Artin}',
 'A tall A and final in-like strokes survive, but the r/t region contains overlapping dark uprights. The crop does not justify removing the local C doubt.', 'medium','other',False,True,'02_artin')
add('D04','Illusie first item, surname pair',r'\unsure{Monsky-Washnitzer}',r'Monsky--Washnitzer',r'\unsure{Monsky-Washnitzer}',
 'M and W are definite, the first name has a descended final y, and the second has a tall h and descending z-like turn. Several low joined letters of the second name remain compressed. Retained uncertainty, not a demonstrated lexical error in H.', 'medium','other',False,True,'03_monsky')
add('D05','Illusie first item, ruled Roman numerals',r'$\overline{\underline{\mathrm{I}}},\overline{\underline{\mathrm{II}}}$',r'I, II',r'$\overline{\underline{\mathrm I}},\overline{\underline{\mathrm{II}}}$',
 'Separate top and bottom strokes accompany the one-upright and two-upright forms; the comma descends between them. These are ordinary handwritten Roman letters, not bold or double-struck characters.', 'high','misread symbol or index',False,True,'03_monsky')
add('D06','Illusie, slash before Hartshorne letters',r'/\quad \unsure{lettres|lettre} Hartshorne',r'Lettres Hartshorne',r'\draw[line width=.3pt] (452,606) -- (507,553);',
 'Half a shows a single oblique stroke rising to the upper-right beside the letter entry, with its lower end beside the next row. H omits it. C has the slash; the drawing supplies its position.', 'high','omission',False,True,bbox=[446,545,514,614])
add('D07','Illusie, letters to Hartshorne',r'\unsure{lettres|lettre}',r'Lettres Hartshorne',r'\unsure{lettres|lettre} Hartshorne',
 'The first stroke is a tall simple l/L-like descent; after double t the final low loop and long hooked terminal do not securely distinguish a plural s from the end of e. The C doubt is retained, including its lower-case first candidate.', 'medium','other',False,True,'04_lettres_hartshorne')
add('D08','Illusie, Hartshorne title separator',r'Hartshorne : Affine duality',r'Hartshorne, \emph{Affine duality}',r'Hartshorne : Affine duality',
 'Half a shows two separated vertically arranged points immediately after Hartshorne. Affine duality was read word by word from the ink. H gives a comma at this same title separator.', 'high','misread symbol or index',False,True,bbox=[517,574,1088,628])
add('D09','Illusie, slash before Quillen letters',r'/\quad \unsure{Lettres|Lettre} Quillen',r'Lettre Quillen',r'\draw[line width=.3pt] (457,730) .. controls (473,712) and (497,684) .. (511,680);',
 'Half a shows a separate curved oblique stroke at the left of this entry, rising toward Lettre. H omits it; C records a slash.', 'high','omission',False,True,bbox=[450,674,516,735])
add('D10','Illusie, Lettre(s) Quillen',r'\unsure{Lettres|Lettre}',r'Lettre Quillen',r'\unsure{Lettre|Lettres} Quillen',
 'The crop gives L-e-tt-r and a final long low stroke with a downturned end. No independent final s is resolved; singular is preferred, while the hooked end leaves plural possible. H has no local doubt marker.', 'medium','other',True,True,'05_lettre_quillen')
add('D11','Illusie, extensions adjective',r'\unsure{infinitésimales}',r'infinitésimales',r'\unsure{infinitésimales}',
 'The i/n opening, tall f, dotted short strokes and final tall l are visible. The central pale joins and accent area remain insufficiently separated to remove the whole-word doubt.', 'medium','other',False,True,'06_infinitesimales')
add('D12','Cancelled Notes entry, tapis/topis',r'\unsure{tapis|topis|topos}',r'tapis',r'\unsure{tapis|topis}',
 'There is a tall t, a p descender and a separate point over the following short upright. That point favours i and removes topos from my candidates; the first vowel remains crossed by the long cancellation.', 'medium','other',True,True,'07_notes_tapis')
add('D13','Cancelled Notes entry, parenthesis and following Quillen',r'(\unsure{pluriel|Gabriel}) Quillen',r'(Quillen)',r'(\unsure{pluriel|Gabriel}) Quillen',
 'A separate faint word lies inside parentheses, with an early descending/looped stroke, a tall loop and a dotted short stroke. The right parenthesis closes before the independently written Q of Quillen. H places Quillen inside the parentheses and omits the actual parenthetical word.', 'low','omission',False,True,'07_notes_tapis')
add('D14','Cancelled Notes entry, long strike geometry',r'\deleted{Notes sur \unsure{tapis|topis|topos} (\unsure{pluriel|Gabriel}) Quillen}',r'\struck{Notes sur tapis (Quillen)}',rpart(r'\draw[line width=.65pt] ([xshift=-1pt,yshift=2pt]tapis.base west)',r'\node (bourbaki)'),
 'A continuous dark cancellation crosses the entire row, rising slightly toward Quillen and extending past its last letters. The witnesses give deletion state but not the observed long path; both states are retained.', 'high','drawing or diagram',True,True,'07_notes_tapis')
add('D15','Bourbaki line, opening words and separators',r'Rapport Bourbaki calcul différentiel','R. Wood à Bourbaki,\ncalcul différentiel',r'R.\ \unsure{Wood} Bourbaki calcul différentiel',
 'The opening R has a separate low stop. A new W-shaped capital follows after a gap, with two compressed round strokes and a final high d-like return. No à is visible in the blank before Bourbaki, and no comma is visible after Bourbaki. Wood remains locally tentative; Rapport is not a continuous written word here.', 'medium','misread word',True,True,'08_bourbaki')
add('D16','Complexe entry, cot and low mark',r'Complexe cot$_{\unsure{*|+}}$ relatif de Quillen',r'Complexe cotangent relatif de Quillen',r'Complexe cot$_{\unsure{*|+}}$ relatif de Quillen',
 'After the c-o-t strokes there is a compact low intersecting sign with a short vertical and lateral arms. No letters angent occur. Star/plus is retained because the upper edge is filled and rounded.', 'medium','abbreviation expanded or spelling modernised',False,True,'09_cot')
add('D17','Atiyah entry, initial L of extension',r"L'extension",r"l'extension",r"L'extension",
 'Half a shows a tall upright with a firm lower horizontal foot followed by a separate apostrophe; I retain the capital L written in C.', 'high','misread word',False,True,bbox=[756,925,935,972])
add('D18','Atiyah entry, pour/par',r'\unsure{pour|par}',r'pour',r'pour',
 'The crop separates a long p stem, a small round o stroke, a shallow u trough and the following r-shaped rise. The extra trough distinguishes pour from par.', 'high','other',True,False,'10_pour_omega')
add('D19','Atiyah entry, tail after Omega-one',r'\unsure{..---|\ldots}','\\ill\\',rpart('% Two compact points',r'\node (koszul)'),
 'Two separate compact points precede one longer pale wavering horizontal trace with a dark endpoint. I render these observed marks directly rather than choose three hyphens or an ordinary three-dot ellipsis. H explicitly leaves this tail unread.', 'high','readable ink left as \\ill{}',True,True,'10_pour_omega',marked=True)
add('D20','Cancelled Borel name',r'\unsure{Borel}',r'Borel',r'Borel',
 'The crop resolves the B stem and paired bowls, a low o, the short r rise, the e loop below the strike, and a small tall terminal l. C uncertainty is removed.', 'high','other',True,False,'11_borel')
add('D21','Cancelled Borel title',r'Lecture Notes',r'lettre, notes',r'Lecture Notes',
 'The initial tall L and the c-t-u-r-e sequence can be followed around the strike. Notes has a capital N. There is no comma between these two source words.', 'high','misread word',False,True,'11_borel')
add('D22','Borel and Lecture Notes, separated cancellation runs',r'\deleted{\unsure{Borel}\qquad Lecture Notes}',r'\struck{Borel : lettre, notes}',rpart(r'\node (borel)',r'% Two separated portions'),
 'The left cancellation crosses Borel only; another begins in the blank before Lecture and continues past Notes. The gap between them is real. Both text groups remain deleted; the two paths are now distinct.', 'high','drawing or diagram',True,True,'11_borel')
add('D23','Thin divider between Illusie and Deligne',r'\draw[line width=.3pt] (0,0) .. controls (1.2,-.05) and (2.9,.13) .. (4.35,.17);'+'\n'+r'\draw[line width=.25pt] (4.52,.19) .. controls (5.5,.13) and (6.9,.26) .. (8.05,.30);','',rpart('% Two separated portions',r'\node[font=\small] (deligne)'),
 'The halves show two thin gray sections with a small break around x 713–735. The first starts over the left label area; the second ends below the Borel title. C records both sections and H omits the drawing.', 'high','omission',False,True,bbox=[240,1027,1102,1079])
add('D24','Deligne label, adjacent heavy mark',r'\unsure{1|2|?}','',r'\unsure{1|2|?}',
 'A dark upper hook, a lower loop and a nearly vertical heavy tail are superposed. The one crop does not separate a 1, a 2 or a question mark securely. H omits the mark rather than explicitly marking it unread.', 'low','omission',False,True,'12_deligne')
add('D25','Small parenthetical below Deligne, wording',r'\unsure{suite|suiten}',r'\emph{(suite)}',r'(\unsure{questions|suite|suiten})',
 'The beginning includes a loop with a descending return, followed by a longer run of small strokes than simple suite would require; a tall central t-like stem and terminal hooked strokes survive. Questions is a tentative first candidate, while the heavy meshing prevents exclusion of C\'s alternatives.', 'low','misread word',True,True,'12_deligne')
add('D26','Small parenthetical below Deligne, cancellation state',r'\deleted{(\unsure{suite|suiten})}',r'\emph{(suite)}',r'\deleted{(\unsure{questions|suite|suiten})}',
 'The word is crossed by a horizontal sweep and repeated gray oblique/looped passes. C correctly marks deletion; H prints the parenthetical live. This row compares state only; the revised lexical candidates are in D25.', 'high','deletion state (struck given live or live given struck)',False,True,'12_deligne')
add('D27','Small parenthetical below Deligne, meshed cancellation',r'\deleted{(\unsure{suite|suiten})}',r'\emph{(suite)}',rpart('% The small parenthetical note',r'\node (monskytwo)'),
 'The crossing is a mesh with repeated low loops and oblique returns, not one straight deletion bar. A separate wavy path records that geometry; decomposition into individual pen passes is uncertain.', 'medium','drawing or diagram',True,True,'12_deligne')
add('D28','Serre entry, separator after name',r'\uuline{Serre} :',r'Serre :',r'\uuline{Serre} \unsure{.|:}',
 'A detached lower point is visible after Serre. The long cancellation passes through the possible upper-point position, so a colon is not fully witnessed; the visible stop is the first candidate.', 'medium','misread symbol or index',True,True,'13_serre_coh')
add('D29','Serre entry, first abbreviation',r'\unsure{Coh.|Ch.}',r'cohomologie',r'\unsure{Ch.|Coh.}',
 'A broad C is followed immediately by a tall h-like stroke and a low stop. No independent o chamber is resolved below the cancellation. Ch. is preferred, but an occluded o remains possible. H expands the source abbreviation.', 'medium','abbreviation expanded or spelling modernised',True,True,'13_serre_coh')
add('D30','Serre entry, Vect. Witt',r'Vect. Witt',r'des vecteurs de Witt',r'Vect. Witt',
 'The crop has capital V, the short ect sequence, a discrete stop and then Witt. Neither des nor de is written in this interval.', 'high','abbreviation expanded or spelling modernised',False,True,'13_serre_coh')
add('D31','Serre entry, var. abéliennes',r'var. abéliennes',r'von Dieudonné',r'var. abéliennes',
 'Half b shows the compact v-a-r followed by a stop, then the initial a, tall b and l strokes, and the low ending of abéliennes. The letters do not give von Dieudonné.', 'high','misread word',False,True,bbox=[1053,1074,1349,1126])
add('D32','Serre entry, car and p condition',r'en car $p\unsure{\ne|>}0$.',r'en caractéristique $p$',r'en car $p\unsure{\ne|>}0$.',
 'The source has the short form car without an abbreviation stop. Following p, an intersected/angled cluster is crossed by the cancellation and is followed by a closed oval zero and a detached terminal stop. H expands car and omits the relation, zero and stop. The sign remains ne/greater-than doubtful.', 'low','abbreviation expanded or spelling modernised',False,True,'14_serre_relation')
add('D33','Serre name, two low rules',r'\uuline{Serre}',r'Serre',r'\uuline{Serre}',
 'The local crop shows two distinct gray rules beneath the name, separately below the dark cancellation. H gives no corresponding underlining macro.', 'high','omission',False,True,'13_serre_coh')
add('D34','Serre entry, long sloping cancellation',r'\deleted{\uuline{Serre} : \unsure{Coh.|Ch.} Vect. Witt et var. abéliennes en car $p\unsure{\ne|>}0$.}',r'\struck{Serre :'+'\n'+r'cohomologie des vecteurs de Witt et von Dieudonné en caractéristique $p$}',rpart(r'\draw[line width=.7pt] ([xshift=-1pt,yshift=2pt]serre.base west)',r'\node[rotate=2] (griffiths)'),
 'One long dark path rises from the lower part of Serre across the whole bibliographic row to the final condition. The schematic path is anchored to the deleted text rather than printed as an unrelated figure.', 'high','drawing or diagram',True,True,bbox=[525,1080,1610,1149])
add('D35','Griffiths title, quotation marks',r"``On monodromy \unsure{....|\ldots}''",r'« On monodromy \ldots »',r"``On monodromy ....''",
 'Half b shows two opening comma-like strokes; the local crop resolves two high closing strokes. They are paired quotation strokes, not angular guillemets. Dot count is separately recorded in D36.', 'high','misread symbol or index',False,True,bbox=[862,1127,1320,1193])
add('D36','Griffiths title, four trailing marks',r'\unsure{....|\ldots}',r'\ldots',r'....',
 'Four distinct marks occur before the closing quote: a short first mark, two small round points and a longer last point. The count four is resolved; an ordinary three-dot ellipsis would lose one.', 'high','other',True,True,'15_monodromy_points')
add('D37','Cancelled Lettre entry, first name',r'\unsure{Rietzly|Rietzley}','\\ill\\',r'\unsure{Rietzly|Rietzley}',
 'The first-name region has an R-like loop, dotted short stroke, e-like low bowl, tall t-like stem and later descender. Griffiths\' descending f and the cancellation overlap its middle. H\'s ill span occurs after Lettre and before chapitre and covers this first name; the tentative C candidates are retained.', 'low','readable ink left as \\ill{}',False,True,'16_lettre_name',marked=True)
add('D38','Cancelled Lettre entry, Chapin',r'Chapin',r'chapitre de'+'\n'+r'familles',r'Chapin,',
 'The crop shows capital C, a tall h, the p descender, dotted i and terminal n, followed by a separate descending comma. It does not have the additional t-r-e sequence of chapitre. H\'s ill marker is earlier, over the first-name span, not this directly transcribed word.', 'high','misread word',False,True,'16_lettre_name')
add('D39','Cancelled Lettre entry, class field thy',r'\unsure{class} field th\unsure{y|.}',r'de'+'\n'+r'familles',r'\unsure{class} field th\unsure{y|.}',
 'After Chapin and its comma, cl-shaped strokes and compressed following letters precede a looped f and the i-e-l-d sequence. The ending has t/h stems and a short descending terminal that may be y or a cancelled stop. H\'s direct words de familles do not match this English phrase; its earlier ill marker does not scope over this phrase.', 'low','misread word',False,True,'16_lettre_name')
add('D40','Cancelled Lettre entry, low wavy rule',r'\uwave{\unsure{Rietzly|Rietzley} Chapin}',r'\struck{Lettre \ill\ chapitre de'+'\n'+r'familles}',rpart('% The separate low wavy rule',r'\node (qui)'),
 'A separate thin wavering rule runs under the two names, below the long rising cancellation. C records a wavy underline; H gives only the cancellation. The path preserves the independent lower trace.', 'high','omission',False,True,'16_lettre_name')
add('D41','Short cancelled start before Weil',r'\deleted{\unsure{Qui|Que}}','',r'\deleted{\unsure{Qui|Que}}',
 'A capital looped Q followed by low u-like and final compressed strokes is crossed separately above Weil. The last letter remains i/e doubtful. H does not transcribe this short cancelled start; its later ill follows Jacobiennes and belongs to a different source locus.', 'medium','omission',False,True,'17_qui')
add('D42','Weil entry, name and title separator',r'Weil : Jacobiennes',r'Work, Jacobiennes',r'Weil : Jacobiennes',
 'Half b shows the W followed by e, a short dotted i and a tall l; after the name is a two-point separator. The long cancellation crosses all three words, which were checked independently.', 'high','misread word',False,True,bbox=[549,1258,938,1312])
add('D43','Weil entry, final adjective',r'\unsure{intermédiaires}',r'\ill\ ;',r'\deleted{\unsure{intermédiaires}.}',
 'A rising t-like stem, compressed middle, dotted short letters and the final s/stop survive around the gray strike, but several medial letters remain covered. H\'s ill immediately after the struck Jacobiennes covers this adjective; I retain a tentative reading and its visibly cancelled state.', 'medium','readable ink left as \\ill{}',False,True,'18_intermediaires',marked=True)
add('D44','Papiers d Artin, double underline beneath 13',r'(\uuline{13})',r'(13)',r'(\uuline{13})',
 'Half b resolves the upright 1 and double-arc 3 inside parentheses, with two distinct short blue rules below the number. H omits those rules.', 'high','omission',False,True,bbox=[884,1314,993,1381])
add('D45','Papiers d Artin, two cancellation lines',r"\deleted{Papiers d'Artin (\uuline{13})}",r"\struck{Papiers d'Artin (13)}",rpart(r'\draw[line width=.6pt] ([yshift=2pt]artinpapers.base west)',r'\node[scale=.94,rotate=2] (lichtenbaum)'),
 'Half b shows two near-parallel dark traversals through this entry, distinct from the two low rules beneath 13. Two explicit path commands preserve the paired cancellation geometry.', 'high','drawing or diagram',True,True,bbox=[539,1326,992,1383])
add('D46','Lichtenbaum entry, name',r'Lichtenbaum,',r'bibliothèque,',r'Lichtenbaum,',
 'Half b shows a tall initial L, the i-c-h-t-e-n sequence, then b-a-u-m, followed by a comma. Its tall middle and final forms do not support bibliothèque.', 'high','misread word',False,True,bbox=[546,1406,829,1466])
add('D47','Lichtenbaum entry, surfaces',r'surfaces',r'\ill\ arithmétiques',r'surfaces',
 'Half b shows s-u-r, a tall descending f, then a-c-e-s before the last adjective. H\'s undivided ill span before arithmétiques covers this word; it is not treated as a definite omission.', 'high','readable ink left as \\ill{}',False,True,bbox=[837,1400,1063,1469],marked=True)
add('D48','Lichtenbaum entry, arithmétiques doubt',r'\unsure{arithmétiques}',r'arithmétiques',r'\unsure{arithmétiques}',
 'The initial low letters, high crossed t, q descender and final joined ending can be followed, but the gray cancellation covers portions of the middle and accent. The C doubt is retained. H\'s ill precedes this word and does not itself mark arithmétiques uncertain.', 'medium','other',False,True,'19_arithmetiques')
add('D49','Final entry, surname',r'\unsure{Harder|Hardy}',r'\ill\ sur conjecture de Weil',r'\unsure{Harder|Hardy}',
 'The crop gives H-a-r-d, then a shallow bowl and a short rise crossed by the cancellation. Those can be e-r; the descending terminal leaves Hardy possible. H\'s ill before sur covers the surname region.', 'medium','readable ink left as \\ill{}',False,True,'20_harder',marked=True)
add('D50','Final entry, possible comma after surname',r'\unsure{Harder|Hardy} sur',r'\ill\ sur',r'\unsure{Harder|Hardy}\unsure{,} sur',
 'A separate-looking descending hook lies between the apparent last letters and sur. It may be a comma, or belong to a terminal y; the comma doubt is kept local. H\'s surname ill span is undivided, so its treatment of this separator cannot be separated from that unread span.', 'low','misread symbol or index',True,True,'20_harder',marked=True)
add('D51','Lower block, long cancellation paths not otherwise itemized',r'\deleted{Weil : Jacobiennes \unsure{intermédiaires}.}',r'\struck{Work, Jacobiennes}',rpart(r'\node[rotate=2.7] (weil)',r'% Isolated points'),
 'Half b and the local crops show rising long cancellations through Weil, Lichtenbaum, Manin and the final entry. Their endpoints extend into neighboring blank space. The saved text anchors each schematic path to its own deleted row. This row concerns geometry only; verbal readings and the separate Artin pair are itemized elsewhere.', 'high','drawing or diagram',True,True,bbox=[539,1237,1428,1609])
add('D52','Detached point at far right beside Griffiths level','','',r'\node[anchor=center] at (1608,1155) {\unsure{\begin{tikzpicture}\fill (0,0) circle (.35pt);\end{tikzpicture}}};',
 'Whole and half b show a tiny isolated dark point to the right of the list. It is retained graphically without assigning punctuation or an authorial function; ink versus surface mark remains uncertain.', 'low','drawing or diagram',True,True,bbox=[1603,1150,1614,1161])
add('D53','Detached point below list, left side','','',r'\node[anchor=center] at (246,1763) {\unsure{\begin{tikzpicture}\fill (0,0) ellipse (.55pt and .35pt);\end{tikzpicture}}};',
 'Whole and half b show a dark isolated flattened point below the left label column. The graphic retains it with uncertainty about ink/surface status and without a character assignment.', 'low','drawing or diagram',True,True,bbox=[239,1757,251,1768])

cd=[]
def doubt(place,C,decision,evidence,confidence,crop=None,bbox=None):
 if C not in Ctext and C not in Path('packets/H162-01_162-1_scan004/C_questions.md').read_text():
  raise ValueError('C doubt substring '+repr(C))
 if crop: bbox=crops[crop]['box']
 cd.append(dict(place=place,C=C,decision=decision,evidence=evidence,confidence=confidence,crop=('readers/H162-01_162-1_scan004/R1/crops/'+crop+'.jpg') if crop else None,bbox=bbox,bbox_source='whole image, 1681 x 2138 pixels'))
doubt('Raynaud title, Theta',r'$\Theta$',r'Retain $\Theta$ without doubt.','The upper half shows a closed oval crossed by a horizontal median stroke; the same form is visible as context in crop 01.','high','01_theta_function')
doubt('Raynaud and Illusie Roman numerals',r'$\overline{\underline{\mathrm{II}}}$','Retain ordinary I/II with their separate upper and lower rules; retain the Raynaud oval.','Each group was inspected separately; top I has an enclosing oval, lower I does not.','high','01_theta_function')
doubt('Illusie two left strokes',r'/','Retain both as separately positioned drawn slashes.','Both are single oblique strokes at the left, not textual fraction signs or insertion arrows.','high',bbox=[446,545,516,735])
doubt('Complexe cot small mark',r'cot$_{\unsure{*|+}}$',r'Retain cot$_{\unsure{*|+}}$.','A low compact intersection has lateral arms and a short vertical; its filled upper region prevents star/plus resolution.','medium','09_cot')
doubt('Atiyah symbol',r'$\Omega^{1}$',r'Retain $\Omega^{1}$.','The symbol is open at the bottom with two feet; the upright 1 is raised at its upper right.','high','10_pour_omega')
doubt('Griffiths quotation marks',r"``On monodromy",'Retain paired opening and closing quotation strokes.','Opening pair was read in half b; the closing pair has two separate high curved uprights in crop 15.','high','15_monodromy_points')
doubt('Papiers d Artin number',r'(\uuline{13})',r'Retain (\uuline{13}).','Two discrete lower rules are visible below 13 and separate from the two long cancellation paths.','high',bbox=[884,1314,993,1381])
doubt('Serre p relation',r'p\unsure{\ne|>}0',r'Retain p\unsure{\ne|>}0.','The relation cluster has intersecting and angled strokes under the strike; zero is closed and distinct. Mathematical expectations do not decide the relation.','low','14_serre_relation')
doubt('Raynaud title word',r'\unsure{function|fonction}',r'Prefer \unsure{fonction|function}.','The first vowel is a closed loop, favouring o; the reduced joined middle keeps the alternative open.','medium','01_theta_function')
doubt('Raynaud third item',r'\unsure{Artin}',r'Retain \unsure{Artin}.','Overlapping uprights remain in the r/t region.','medium','02_artin')
doubt('Illusie first surname pair',r'\unsure{Monsky-Washnitzer}',r'Retain \unsure{Monsky-Washnitzer}.','Several second-name joins remain too compressed for unqualified certainty.','medium','03_monsky')
doubt('Illusie Hartshorne letters',r'\unsure{lettres|lettre}',r'Retain \unsure{lettres|lettre}.','The terminal hooked line could carry s or be the terminal of e.','medium','04_lettres_hartshorne')
doubt('Illusie Quillen letters',r'\unsure{Lettres|Lettre}',r'Prefer \unsure{Lettre|Lettres}.','No independent last s is separated, although the terminal hook permits it.','medium','05_lettre_quillen')
doubt('Extensions adjective',r'\unsure{infinitésimales}',r'Retain \unsure{infinitésimales}.','Central faded joins and the accent area remain locally reduced.','medium','06_infinitesimales')
doubt('Cancelled Notes, tapis',r'\unsure{tapis|topis|topos}',r'Narrow to \unsure{tapis|topis}.','The detached point over the short stroke supports i rather than the second o in topos; the first vowel is crossed.','medium','07_notes_tapis')
doubt('Cancelled Notes, parenthetical',r'\unsure{pluriel|Gabriel}',r'Retain \unsure{pluriel|Gabriel}.','The first downward stroke and tall loop favour pluriel but the long cancellation obscures joining letters.','low','07_notes_tapis')
doubt('Atiyah preposition',r'\unsure{pour|par}',r'Resolve as pour.','Small o and a following separate u trough can both be seen.','high','10_pour_omega')
doubt('Atiyah terminal marks',r'\unsure{..---|\ldots}','Replace the alternatives by a direct drawing of two points and one wavering short stroke.','Three discrete units are visible; the last is elongated and has a dark endpoint.','high','10_pour_omega')
doubt('Borel',r'\unsure{Borel}',r'Resolve as Borel.','Both B bowls and the o-r-e-l sequence survive around the crossing.','high','11_borel')
doubt('Deligne adjacent mark, including recovered question-mark metadata',r'\unsure{1|2|?}',r'Retain \unsure{1|2|?}.','The hooked top, lower loop and heavy tail overlap; the recovered C note adds no separate source locus.','low','12_deligne')
doubt('Deligne small parenthetical',r'\unsure{suite|suiten}',r'Use \unsure{questions|suite|suiten}, still cancelled.','An early descending loop and the longer run of small strokes admit questions; the overlying mesh prevents a decisive reading.','low','12_deligne')
doubt('Serre first abbreviation',r'\unsure{Coh.|Ch.}',r'Prefer \unsure{Ch.|Coh.}.','The C bottom joins the tall h-like stem without an independently resolved o chamber.','medium','13_serre_coh')
doubt('Griffiths trailing points',r'\unsure{....|\ldots}',r'Resolve as four points: ....','The crop separates four units, although the first and fourth are elongated.','high','15_monodromy_points')
doubt('Letter first name',r'\unsure{Rietzly|Rietzley}',r'Retain \unsure{Rietzly|Rietzley}.','The upper-line descender and long strike cross the name\'s medial strokes.','low','16_lettre_name')
doubt('Letter English first word',r'\unsure{class}',r'Retain \unsure{class}.','The cl opening is strong; the remaining short strokes merge with the crossing.','low','16_lettre_name')
doubt('Letter final abbreviation',r'th\unsure{y|.}',r'Retain th\unsure{y|.}.','The final descending terminal is separate from the long endpoint but its letter-versus-stop identity remains uncertain.','low','16_lettre_name')
doubt('Cancelled short start',r'\unsure{Qui|Que}',r'Retain \unsure{Qui|Que}.','Q and a low u-like form are visible; the last small cell is crossed.','medium','17_qui')
doubt('Weil adjective',r'\unsure{intermédiaires}',r'Retain \unsure{intermédiaires}.','Some ascending/dotted strokes survive, but the heavy gray line covers several medial letters.','medium','18_intermediaires')
doubt('Lichtenbaum adjective',r'\unsure{arithmétiques}',r'Retain \unsure{arithmétiques}.','A high crossed t and q descender are distinct, while the middle and accent meet the gray strike.','medium','19_arithmetiques')
doubt('Last surname',r'\unsure{Harder|Hardy}',r'Retain \unsure{Harder|Hardy}; add a separate local comma doubt.','The final shallow bowl/rise and descending hook do not establish whether the hook is part of y or punctuation.','medium','20_harder')

I=[]
def inv(element,kind,position,first,hand='handwritten, dark blue/black ink'):
 I.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('Raynaud left label','text','x 224–415, y 64–123','Raynaud')
inv('Mumford title and Theta word','text','x 528–1006, y 64–129','Mumford . Theta fonction/function')
inv('Top ruled numerals and oval','drawing','x 1025–1138, y 39–133','oval around I; comma; II')
inv('Kiehl entry','text','x 529–805, y 128–179','Papiers Kiehl')
inv('Artin-Winters entry','text','x 538–868, y 183–238','Artin-Winters','handwritten, darker retraced strokes')
inv('Illusie label and numeral','text','x 245–445, y 477–516','Illusie 1')
inv('First Monsky-Washnitzer entry and ruled numerals','text','x 506–943, y 463–510','Monsky-Washnitzer I, II')
inv('Hartshorne letters entry','text','x 510–889, y 526–568','lettres/lettre Hartshorne')
inv('Slash by Hartshorne letters','drawing','x 452–508, y 552–607','single oblique stroke','handwritten thin gray/dark stroke')
inv('Hartshorne title entry','text','x 520–1082, y 575–630','Hartshorne : Affine duality')
inv('Quillen letters entry','text','x 524–843, y 641–686','Lettre/Lettres Quillen')
inv('Slash by Quillen letters','drawing','x 457–511, y 679–731','curved oblique stroke','handwritten thin gray/dark stroke')
inv('Extensions entry','text','x 528–1220, y 698–746','Notes sur extensions infinitésimales')
inv('Cancelled Notes entry, all words retained','deletion','x 528–1214, y 754–797','Notes sur tapis/topis (pluriel/Gabriel) Quillen')
inv('Long cancellation across Notes entry','drawing','x 529–1212, y 770–783','continuous slightly rising strike')
inv('Bourbaki entry','text','x 529–1284, y 817–866','R. Wood Bourbaki calcul différentiel')
inv('Complexe entry','text','x 521–1151, y 878–930','Complexe cot with low star/plus; relatif de Quillen')
inv('Atiyah entry, slightly rising baseline','text','x 532–1319, y 911–974','Notes sur L\'extension d\'Atiyah pour Omega-one')
inv('Two points and final short trace after Omega-one','drawing','x 1331–1391, y 940–951','two compact points; one wavering line and endpoint')
inv('Koszul entry','text','x 532–914, y 975–1013','Koszul 2 articles')
inv('Cancelled Borel name','deletion','x 532–628, y 1007–1044','Borel')
inv('Cancelled Lecture Notes title','deletion','x 687–1016, y 999–1037','Lecture Notes; separate extended strike')
inv('Divider in two separated portions','drawing','x 243–1096, y 1029–1077','first gray section; gap; second gray section','handwritten thin gray line')
inv('Deligne left label','text','x 240–399, y 1072–1125','Deligne')
inv('Heavy adjacent numeral/question mark','text','x 402–433, y 1067–1114','1/2/?','handwritten dark retraced mark')
inv('Cancelled parenthetical below Deligne','deletion','x 239–372, y 1125–1165','(questions/suite/suiten)')
inv('Meshed cancellation of small parenthetical','drawing','x 243–368, y 1130–1167','horizontal sweep and low looped zigzag','handwritten gray/dark overwriting')
inv('Second Monsky-Washnitzer entry','text','x 522–913, y 1052–1101','Monsky-Washnitzer')
inv('Cancelled Serre title, full abbreviated wording','deletion','x 529–1609, y 1080–1152','Serre ./: Ch./Coh. Vect. Witt et var. abéliennes en car p ... 0')
inv('Two low rules beneath Serre','drawing','x 543–623, y 1147–1164','two short rules','handwritten gray rules')
inv('Long rising Serre strike','drawing','x 529–1602, y 1089–1143','dark cross-row line')
inv('Griffiths preprint entry and quotation','text','x 525–1318, y 1128–1209','Preprint Griffiths : paired quotes, On monodromy, four points')
inv('Cancelled letter entry','deletion','x 530–1198, y 1174–1235','Lettre Rietzly/Rietzley Chapin, class field thy')
inv('Letter entry long strike','drawing','x 530–1198, y 1182–1230','rising dark cancellation')
inv('Independent low wavy rule beneath names','drawing','x 669–934, y 1224–1244','wavering rule under first name and Chapin','handwritten thin gray line')
inv('Short cancelled start above Weil','deletion','x 524–603, y 1235–1271','Qui/Que')
inv('Weil entry and long strike','deletion','x 550–1292, y 1239–1306','Weil : Jacobiennes intermédiaires.')
inv('Papiers d Artin entry','deletion','x 545–990, y 1317–1380','Papiers d\'Artin (13)')
inv('Two rules beneath Arabic 13','drawing','x 921–963, y 1357–1373','two short blue underlines')
inv('Paired cancellations across Artin entry','drawing','x 546–987, y 1335–1374','two near-parallel traversals')
inv('Lichtenbaum entry and gray strike','deletion','x 551–1389, y 1381–1465','Lichtenbaum, surfaces arithmétiques','handwritten ink with broad gray crossing')
inv('Manin entry and gray strike','deletion','x 548–1421, y 1455–1523','Manin, variétés rationnelles (2 articles)','handwritten ink with broad gray crossing')
inv('Final surname and Weil-conjecture entry','deletion','x 558–1315, y 1539–1605','Harder/Hardy, sur conjecture de Weil')
inv('Detached far-right point','drawing','x 1603–1614, y 1150–1161','isolated small point; writing versus surface uncertain','uncertain ink/surface mark')
inv('Detached point below left label column','drawing','x 239–251, y 1757–1768','isolated flattened point; writing versus surface uncertain','uncertain ink/surface mark')
inv('Archive number, recorded as required comment only','text','lower left, x 64–99, y 2050–2092','3','handwritten archive notation, not treated as authorial page number')

RD=[]
def rem(place,reading,alternatives,confidence): RD.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence))
rem('Raynaud title',r'\unsure{fonction|function}',['fonction','function'],'medium')
rem('Artin-Winters first name',r'\unsure{Artin}',['Artin; medial strokes not fully separated'],'medium')
rem('First Monsky-Washnitzer',r'\unsure{Monsky-Washnitzer}',['Monsky-Washnitzer; compressed joined letters'],'medium')
rem('Hartshorne letters',r'\unsure{lettres|lettre}',['lettres','lettre; initial l/L not fully diagnostic'],'medium')
rem('Quillen letters',r'\unsure{Lettre|Lettres}',['Lettre','Lettres'],'medium')
rem('Extensions adjective',r'\unsure{infinitésimales}',['infinitésimales; pale medial joins and accent'],'medium')
rem('Cancelled Notes noun',r'\unsure{tapis|topis}',['tapis','topis'],'medium')
rem('Cancelled Notes parenthesis',r'\unsure{pluriel|Gabriel}',['pluriel','Gabriel'],'low')
rem('Bourbaki line second word',r'\unsure{Wood}',['Wood; two compressed round strokes not fully separated'],'medium')
rem('Low mark after cot',r'\unsure{*|+}',['star','plus'],'medium')
rem('Deligne adjacent mark',r'\unsure{1|2|?}',['1','2','question mark'],'low')
rem('Parenthetical below Deligne',r'\unsure{questions|suite|suiten}',['questions','suite','suiten'],'low')
rem('Serre separator',r'\unsure{.|:}',['period','colon with upper point obscured'],'medium')
rem('Serre abbreviation',r'\unsure{Ch.|Coh.}',['Ch.','Coh.'],'medium')
rem('Serre characteristic condition',r'p\unsure{\ne|>}0',['not equal','greater than'],'low')
rem('Cancelled letter first name',r'\unsure{Rietzly|Rietzley}',['Rietzly','Rietzley'],'low')
rem('Cancelled letter English phrase',r'\unsure{class}',['class; final short letters crossed'],'low')
rem('Cancelled letter final abbreviation',r'th\unsure{y|.}',['thy','th.'],'low')
rem('Short cancelled start',r'\unsure{Qui|Que}',['Qui','Que'],'medium')
rem('Weil adjective',r'\unsure{intermédiaires}',['intermédiaires; several medial cells hidden'],'medium')
rem('Lichtenbaum adjective',r'\unsure{arithmétiques}',['arithmétiques; medial cells and accent partly crossed'],'medium')
rem('Final surname',r'\unsure{Harder|Hardy}',['Harder','Hardy'],'medium')
rem('Final surname separator',r'\unsure{,}',['comma','terminal y descender rather than punctuation'],'low')
rem('Two isolated points',r'\unsure{\begin{tikzpicture}\fill (0,0) circle (.35pt);\end{tikzpicture}}',['deliberate or accidental ink','surface/scan mark'],'low')
report=dict(page='H162-01_162-1_scan004',reader='R1',
 viewed={'whole':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan004.jpg','a':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan004_a.jpg','b':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan004_b.jpg'},
 reading_file='out/readers/H162-01_162-1_scan004/R1/reading.tex',differences=D,c_doubts=cd,inventory=I,remaining_doubts=RD,
 notes=[
  'This is a handwritten bibliographic/document list in three spatial blocks labelled Raynaud, Illusie 1 and Deligne with a heavily retraced adjacent mark. The top block lists Mumford, Kiehl and Artin-Winters; the middle contains letter/title entries and two cancelled items; the lower block contains many cancelled entries and a live Griffiths preprint title.',
  'No date, explicit overall title or authorial page number is visible. The lower-left 3 is treated as archive numbering and preserved only in the required comment. The source explicitly gives 2 articles by Koszul and 2 articles by Manin; the double-underlined 13 in the Artin entry is not interpreted as a page count.',
  'No prose hesitation or mathematical question is written out. The uncertain mark after Deligne may itself be a question mark; the remaining uncertainty marks in reading.tex are editorial, not claims that the source expresses doubt.',
  'The first word in the cancelled small parenthetical below Deligne is materially uncertain. I admit questions from the initial descending loop and length of the run while retaining suite/suiten; this is not a confident replacement.',
  'H uses semicolons and dashes to concatenate list items. Those editorial joins were not treated as physical source punctuation errors. Its direct misread title separators and its explicitly unread spans were scoped individually.',
  'The first-name span in the letter entry, the surfaces span in the Lichtenbaum entry and the adjective after Jacobiennes are not declared wholly absent from H: each has a corresponding literal ill span. H\'s ill before arithmétiques does not mark arithmétiques itself doubtful.',
  'All agreement passages were read from the halves, including Papiers Kiehl, Hartshorne, Affine duality, the main extension wording, Koszul, the second Monsky-Washnitzer entry, the Manin entry and both article counts. No named work or surname was checked against an external edition.'
 ],
 notation=[
  {'form':'Theta','reading':r'\Theta','evidence':'closed oval with a horizontal median stroke'},
  {'form':'Roman I and II, both title groups','reading':r'\overline{\underline{\mathrm I}},\overline{\underline{\mathrm{II}}}','evidence':'ordinary pen uprights with separate common upper/lower rules; top I alone has an enclosing oval'},
  {'form':'Low sign after cot','reading':r'\unsure{*|+}','evidence':'small intersecting mark below the word baseline, not expanded to letters'},
  {'form':'Atiyah object','reading':r'\Omega^{1}','evidence':'open-bottom capital with two feet; separately raised numeral 1'},
  {'form':'Serre condition','reading':r'p\unsure{\ne|>}0','evidence':'ordinary lowercase p, crowded relation cluster and closed oval zero; no semantic normalization'},
  {'form':'13','reading':r'\uuline{13}','evidence':'ordinary Arabic numerals with two separate short lower rules'},
  {'form':'Page alphabets','reading':'ordinary handwritten letters throughout','evidence':'no independently observed double-struck, script or Fraktur alphabet is required; darkness of retraced names is not a mathematical alphabet'}
 ],
 abbreviations=[
  {'form':'R.','expansion':'Editorial: unresolved; no expansion is asserted.'},
  {'form':'cot with low star/plus','expansion':'Editorial proposed expansion of cot: cotangent. The low sign is not expanded.'},
  {'form':'Ch. / Coh.','expansion':'Editorial conditional suggestion: cohomologie if the cohomological abbreviation is intended; the literal abbreviated candidates remain.'},
  {'form':'Vect.','expansion':'Editorial: vecteurs.'},
  {'form':'var.','expansion':'Editorial: variétés.'},
  {'form':'car','expansion':'Editorial: caractéristique; the source has no stop after car.'},
  {'form':'thy / th.','expansion':'Editorial proposed expansion: theory, conditional on the English abbreviation reading.'}
 ],
 math_checks=[
  {'check':'No proof or numerical computation is present on this bibliographic list.','performed':'No theorem was verified and no calculation was claimed.'},
  {'check':'Position of the two small mathematical marks','performed':'I compared the visible baselines: the mark after cot is low, whereas 1 is raised to the right of Omega. This is a symbol/placement check, not a proof.'},
  {'check':'Possible characteristic condition','performed':'I considered both ne and > as readings of the crossed sign and did not choose between them from the meaning of characteristic p. The source relation stays unresolved.'},
  {'check':'Abbreviations against H expansions','performed':'I checked the written extent of cot, Ch./Coh., Vect., var. and car. No missing letters were supplied to make a familiar mathematical title.'}
 ],crop_count=len(crops),
 workflow_feedback=[
  'Viewed the original whole image once for layout and dimensions (1681 x 2138), then each supplied half once. Half a begins at source y=0; half b corresponds to y=989 through 2138. No whole-half reload or enlargement was used.',
  'Created and viewed 20 tight crops, one per unresolved local region. Nearby doubts sharing one narrow line region use the same crop; no decided locus was recropped. The crop manifest is saved alongside the crops.',
  'Complete reading.tex was saved before report assembly. The parent requested a rendering/schema correction after that save: remove a local redefinition of the supplied deleted macro. It was removed, leaving the original PREAMBLE state wrapper plus schematic anchored cancellation paths. No ink reading or image observation changed.',
  'Graphic coverage was checked against the text: two divider commands, separate Borel and Lecture cancellation paths, a parenthetical mesh path, separate Serre underlining and cross-row strike, the independent names underline, two Artin cancellation paths, two low rules under 13, and both isolated-point drawings are present. Source path descriptions are schematic; no inferred chronology is assigned to overlapping strokes.',
  'The recovered C question-mark note for Deligne is covered by the existing 1/2/? locus and crop. No extra image view was made for it.',
  'No OCR, recognition engine, external source, other page, other reader file, optional compilation or further agent was used. Witness strings in the report were checked as literal substrings before saving.'
 ])
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(D),'c_doubts':len(cd),'inventory':len(I),'remaining_doubts':len(RD),'crop_count':len(crops)},ensure_ascii=False))
