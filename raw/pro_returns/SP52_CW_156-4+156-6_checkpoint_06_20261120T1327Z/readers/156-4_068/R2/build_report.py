from pathlib import Path
import json
from datetime import datetime, timezone

OUT = Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_068/R2')
SRC = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans')
whole = str(SRC/'J156-4-09_156-4_scan068.jpg')
a = str(SRC/'J156-4-09_156-4_scan068_a.jpg')
b = str(SRC/'J156-4-09_156-4_scan068_b.jpg')
manifest = json.loads((OUT/'crop_manifest.json').read_text())
by_num = {int(Path(x['path']).stem[:2]):x for x in manifest}
reading = (OUT/'reading.tex').read_text()

def figure_after(marker):
    start = reading.index('\\figure{', reading.index(marker))
    end = reading.index('\n}', start) + 2
    return reading[start:end]

m0_figure = figure_after('% R2-M0-leader')
points_figure = figure_after('% R2-realisations-points')
anti_figure = figure_after('% R2-anti-overwrite')

diffs = []
def diff(location,c,h,r,evidence,confidence='high',kind='other',change_c=False,change_h=True,crop=None,bbox=None,source=None,marked='no',math=False):
    spec = by_num.get(crop)
    if spec:
        source = spec['source'] if source is None else source
        bbox = spec['bbox'] if bbox is None else bbox
    assert source and bbox
    diffs.append(dict(id=f'R2-D{len(diffs)+1:02d}',location=location,c=c,h=h,reading=r,scan_shows=evidence,confidence=confidence,kind=kind,marked_in_h=marked,change_c=change_c,change_h=change_h,crop=spec['path'] if spec else None,bbox=bbox,bbox_image=source,source=source,math_consequential=math))

diff('Cancelled opening, unfinished quotation after de',r'\deleted{On a une notion de \unsure{``c|``C|``6}}',r'\struck{On a une notion de \ill{}}',r'\deleted{On a une notion de \unsure{``c|``C|``6}}','The cancelled line has the readable words On a une notion de, a small paired/connected opening quotation mark, and an inward-curling final glyph. The crossing stroke prevents a confident c/C/6 distinction.','low','readable ink left as \\ill{}',crop=1,marked='yes')
diff('Toute partie de, first family letter',r'$\mathcal F$',r'$\mathfrak{F}$',r'$\mathcal F$','One tall stem with curved/looped foot and broad upper arm; no Gothic letter construction. The family letter is calligraphic in this occurrence.',kind='misread symbol or index',source=a,bbox=[915,125,990,190])
diff('Parenthetical resp before M','resp','resp.','resp','No separate point follows resp before the M; the terminal descending stroke belongs to the abbreviation.',source=a,bbox=[1055,120,1240,205])
diff('Parenthetical M in the first sentence',r'$M$',r'$\mathcal{M}$',r'$M$','A plain two-peaked M with its ordinary curved entry stroke, rather than a separate calligraphic alphabet.',kind='misread symbol or index',source=a,bbox=[1240,120,1345,195])
diff('First paragraph, adjective before parenthesis',r'\unsure{minimale}','minimale',r'\unsure{minimale}','The initial min strokes are worked together; the final -ale is clearer. Enlargement does not resolve all medial letter strokes.','medium',crop=2)
diff('First paragraph, first word after parmi',r'\unsure{celles|telles}','celles',r'\unsure{telles|celles}','The first letter is unusually tall and has a short rightward tick, favouring t; an extended c cannot be excluded. The two following l loops and final e/s sweep are visible.','medium','misread word',change_c=True,crop=3)
diff('Cancelled phrase after qui',r'\deleted{s\'appelle \unsure{du|de}}',r'\struck{s\'appelle le}',r'\deleted{s\'appelle \unsure{du|de}}','The last short word has a low left loop and an ascending d stem. Its second letter is obscured by the strike; du/de remain, while le is not supported.','medium','misread word',crop=4)
diff('Low mark immediately before operator',r'\unsure{.} $\unsure{\operatorname{cosup}|\operatorname{cosupp}}$','cosupp',r'\unsure{.} $\operatorname{cosup}$','A separate small low dark dash/point precedes c. The mark is retained with doubt about its status as punctuation. Operator spelling is separately collated below.','medium','omission',crop=5)
diff('Operator following L’application',r'$\unsure{\operatorname{cosup}|\operatorname{cosupp}}$','cosupp',r'$\operatorname{cosup}$','The final group has one descending p stroke. The double descenders of the full cosupport in the adjacent line provide a local shape comparison, not a mathematical correction.','high','abbreviation expanded or spelling modernised',change_c=True,crop=5)
diff('Bijection, raised internal letter',r'\unsure{bij\inserted{e}ction}','bijection',r'\unsure{bij\inserted{e}ction}','The word has a separately raised looped/zigzag e-like sign over the junction after j. The full word remains uncertain because the small baseline letters coalesce.','medium','insertion or placement',crop=6)
diff('l’ens des parties in the upper paragraph',"l'ens", "l'ens.", "l'ens",'The reduced ens group ends in a plain exit stroke with no detached full stop.',source=a,bbox=[825,920,1020,1015])
diff('After des parties, final letters of saturées',r'\unsure{saturées|saturée}','saturées',r'\unsure{saturées|saturée}','The end is a nearly level sweep following short humps. A separate final s cannot be reliably distinguished from the exit stroke.','medium',crop=7)
diff('Small word preceding elles',r'\unsure{sur}','sur',r'\unsure{sur}','Three reduced separated traces can fit sur; the first is only a small open curve and the remaining letters are not fully formed.','medium',crop=8)
diff('After elles',r'elles \unsure{=|mêmes}',r'\ill{}',r'elles $=$','Two distinct approximately parallel horizontal strokes follow the clearly legible elles. No letters of mêmes are present at this location.','high','readable ink left as \\ill{}',change_c=True,source=a,bbox=[540,1020,880,1125],marked='yes')
diff('l’ens des supports after Sigma',"l'ens", "l'ens.", "l'ens",'The short group after l’ has no detached full stop before des.',source=b,bbox=[1200,95,1410,175])
diff('Inserted M0, alphabet and subscript',r'\inserted{$M_0$}',r'\add{$\mathcal{M}_0$}',r'\inserted{$M_0$}','The raised insertion is a plain M followed by a small low round zero. It is not the loop-and-tail sigma of the later display.',kind='misread symbol or index',crop=9)
diff('Distinct oblique leader after the inserted M0',r'\inserted{$M_0$} de $M$,',r'\add{$\mathcal{M}_0$} de $\mathcal{M}$,',m0_figure,'A separate curved oblique stroke runs down-left from beside the raised M0 toward the beginning of de. No arrowhead is visible. The local TikZ group transcribes the label, leader and adjoining words once.',kind='drawing or diagram',change_c=True,crop=9)
diff('M after the inserted M0 and de',r'$M$',r'$\mathcal{M}$',r'$M$','The two peaked plain M matches the nearby inserted capital; no special script form is present.',kind='misread symbol or index',crop=9,bbox=[495,335,605,410])
diff('Short word between de M, and cancelled de',r'\unsure{où|ou}','ou','où','A separate short downward-right stroke stands above the second vowel. It is retained as the written grave accent, despite the alternative favoured by syntax.','medium','misread word',change_c=True,crop=10)
diff('Cancelled de before F0',r'\deleted{\unsure{de}}',r'\struck{de}',r'\deleted{\unsure{de}}','The d stem and left loop survive, but the crossed second-letter area remains congested. The reading de is plausible rather than fully recovered.','medium',crop=10)
diff('F0 following cancelled de',r'$\mathcal F_0$',r'$\mathfrak{F}_0$',r'$\mathcal F_0$','A tall F with looped/bent top and curved foot, plus a separate small low round zero; no Gothic strokes.',kind='misread symbol or index',crop=10,bbox=[905,295,1015,390])
diff('M after F0 de',r'$M$',r'$\mathcal{M}$',r'$M$','Two plain upright peaks and a curved left entry are visible. The letter is M, and no substitution of F is made.',kind='misread symbol or index',source=b,bbox=[1135,295,1255,375])
diff('Cancelled words at the right end of the definition line',r'\deleted{On \unsure{définit}}',r'\struck{\ill{}}',r'\deleted{On \unsure{définit}}','The cancelled On is distinguishable; the following group preserves a d loop, long descending f and final upright/cross stroke. Several intervening strokes remain under multiple strike lines.','medium','readable ink left as \\ill{}',crop=11,marked='yes')
diff('Cancelled L’application line, short word before cosupport',r'\deleted{L\'application du cosupport de}',r'\struck{L\'application de cosupport d}',r'\deleted{L\'application \unsure{du|de} cosupport \unsure{d|de}}','The word after application has a d loop and a flattened second-letter trace; the cancellation stroke prevents a decisive u/e distinction. The last word is collated separately.','medium','misread word',change_c=True,crop=12)
diff('Cancelled L’application line, terminal group',r'\deleted{de}',r'\struck{d}',r'\deleted{\unsure{d|de}}','One terminal d-like stem and lower loop are distinguishable. The long horizontal line continuing right is the deletion stroke; an independent final e is not secure.','low','misread word',change_c=True,crop=12,bbox=[1260,415,1360,480])
diff('Live verb after On before Sigma',r'\unsure{désidentifie|délibérément identifie|identifie}',r'\ill{}',r'\unsure{désidentifie|identifie}','The ink occupies one continuous word-sized group, with an initial d-like loop, two high small marks, a medial stem and the final f/i group. It does not securely support two complete words délibérément identifie. The expanded first part of désidentifie remains uncertain.','low','readable ink left as \\ill{}',change_c=True,crop=13,marked='yes',math=True)
diff('Preposition following the second Sigma','de','à','de','A lower left oval joins an ascending loop and horizontal exit: it is the local d/e form, not an a with a separate grave accent.',kind='misread word',crop=13,bbox=[1040,470,1130,545],math=True)
diff('Cancelled capital before ses deux',r'\deleted{$\unsure{\mathcal F}$}',r'\struck{\ill{}}',r'\deleted{$\unsure{\mathscr P|\mathcal F}$}','The surviving tall left stem and broad angular right bowl resemble P. Two diagonal cancelling strokes and a lower hook obscure the exact original form; F remains possible.','low','misread symbol or index',change_c=True,crop=14,marked='yes',math=True)
diff('Words immediately after the cancelled capital','ses deux','un','ses deux','The first group has an initial angular s and two reduced humps; the next begins with a clear d loop and ends in a detached crossed x. Both words can be read in the crop. H’s following unread group is aligned separately with réalisations.','high','misread word',crop=14)
diff('Word preceding the parenthesis comme',r'\unsure{réalisations}',r'\ill{}',r'\unsure{réalisations}','The visible initial and final groups fit réalisations, with a tall l/t and several separated dots or short marks. The compressed medial letters do not permit removal of the doubt.','medium','readable ink left as \\ill{}',crop=15,marked='yes')
diff('Two low detached points beneath the middle of réalisations',r'\unsure{réalisations}',r'\ill{}',points_figure,'Two small dark detached points occur below the middle of the word, the second lower and to the right. Their function is not established; the local figure preserves their positions without converting them to a word-final colon or period.','medium','drawing or diagram',change_c=True,crop=15,marked='yes')
diff('comme partie(s) de',r'\unsure{partie|parties}','partie',r'\unsure{partie|parties}','The final letter group is thick and flat; it cannot establish a terminal plural s independently of the e exit.','medium',crop=16)
diff('First power-set letter before (M)',r'\unsure{\mathscr P|\mathcal P|\wp}',r'\mathfrak{P}',r'\unsure{\mathscr P|\mathcal P|\wp|P}','The capital has one tall upright and an angular bowl; unlike the second occurrence it lacks a distinct lower-left curl. A plain P is therefore also retained as an alphabet possibility. A Gothic form is not supported.','medium','misread symbol or index',change_c=True,crop=16)
diff('M inside first power-set parentheses',r'$M$',r'$\mathcal{M}$',r'$M$','The two peaked capital is plain M, despite its large left connecting entry stroke.',kind='misread symbol or index',crop=16,bbox=[1310,530,1410,630])
diff('Second power-set letter before (F)',r'\mathscr P',r'\mathfrak{P}',r'\mathscr P','This occurrence has a conspicuous lower-left curling return as well as the broad angular bowl. The clearly drawn curl supports the script P independently of the first occurrence.',kind='misread symbol or index',crop=17)
diff('Family letter inside second power-set parentheses',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','A broad upper arm, single cross arm and curved stem are present; there is no Gothic construction.',kind='misread symbol or index',crop=17,bbox=[435,645,520,735])
diff('Immediately after sigma membership Sigma before the display',r'$\sigma\in\Sigma$',r'$\sigma \in \Sigma$,',r'$\sigma\in\Sigma$','After the final capital Sigma there is clear paper; no comma is present on the manuscript line.',kind='text not on the page',source=b,bbox=[1245,615,1490,710])
diff('Display, first M with sigma subscript',r'M_\sigma',r'\mathcal{M}_\sigma',r'M_\sigma','Plain two-peaked M. The low oval-with-right-tail sigma differs visibly from the earlier round zero.',kind='misread symbol or index',source=b,bbox=[525,715,655,800])
diff('Display, ambient M after first inclusion',r'M',r'\mathcal{M}',r'M','A plain M after the right-opening inclusion sign.',kind='misread symbol or index',source=b,bbox=[705,710,800,795])
diff('Display, family F with sigma subscript',r'\mathcal F_\sigma',r'\mathfrak{F}_\sigma',r'\mathcal F_\sigma','A broad looped upper arm and curved single stem accompany the small low sigma; no Gothic construction.',kind='misread symbol or index',source=b,bbox=[875,700,985,795])
diff('Display, ambient family F after second inclusion',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The single stem and broad upper arm are the local family F form.',kind='misread symbol or index',source=b,bbox=[1030,685,1125,785])
diff('End of the displayed pair',r'\mathcal F',r'\mathfrak{F} .',r'\mathcal F','No detached period follows the final F; the nearby ink belongs to the letter and the preceding text line.',kind='text not on the page',source=b,bbox=[1020,685,1190,805])
diff('Bottom paragraph, revised compound beginning anti',r'anti\deleted{\unsure{isomorph|homéo}}\unsure{involution|bijection|dualité}',r'anti\ill{}',anti_figure,'The post-anti letters occupy one crowded overwritten area. A heavy middle stroke crosses an earlier layer; the surviving loops, descender and two final uprights do not recover a complete old word or settle the live word. The unreadable old layer is estimated as one word and is spatially superposed with the live alternatives, rather than presented as a second successive word.','low','deletion state (struck given live or live given struck)',change_c=True,crop=18,marked='yes',math=True)
diff('Bottom paragraph, M in the intersection description',r'$M$',r'$\mathcal{M}$',r'$M$','Two ordinary peaks form the plain M.',kind='misread symbol or index',source=b,bbox=[860,1085,955,1165])
diff('Bottom paragraph, family F in the intersection description',r'$\mathcal F$',r'$\mathfrak{F}$',r'$\mathcal F$','The broad bent cap and curved single stem match the family letter; no Gothic strokes.',kind='misread symbol or index',source=b,bbox=[1180,1070,1260,1155])
diff('Placement of the two cancelled drafting attempts after F0 de M',r'\deleted{On \unsure{définit}} \deleted{L\'application du cosupport de} On',r'\struck{\ill{}}\n\n\struck{L\'application de cosupport d}\n\nOn',r'\deleted{On \unsure{définit}} \deleted{L\'application \unsure{du|de} cosupport \unsure{d|de}} On','The first cancelled attempt is at the right end of the definition line; the second occupies the following line, with the live On immediately beneath. There is no new paragraph-sized blank interval between these pieces.','high','insertion or placement',source=b,bbox=[300,300,1665,565],marked='yes')
diff('H editorial note about the M following F0',r'$\mathcal F_0$ de $M$',r'\note{« $\mathfrak{F}_0$ de $\mathcal{M}$ » : lire « de $\mathfrak{F}$ » ; la lettre finale est surchargée}',r'$\mathcal F_0$ de $M$','The visible final letter is M with two clear upright peaks. The phrase lire de F and the assertion of an overwritten final letter are editorial assertions in H, not words written on this page; no F is substituted.','high','text not on the page',source=b,bbox=[905,295,1255,390])

c_doubts = []
def cd(row,location,c,r,status,evidence,crop=None,source=None,bbox=None,extra=None):
    spec=by_num.get(crop)
    if spec:
        source=source or spec['source']; bbox=bbox or spec['bbox']
    assert source and bbox
    item=dict(id=f'R2-C{row:02d}',context_row=row,location=location,c=c,reading=r,status=status,scan_shows=evidence,crop=spec['path'] if spec else None,bbox=bbox,bbox_image=source,source=source)
    if extra: item.update(extra)
    c_doubts.append(item)

cd(1,'All Sigma/sigma occurrences and both display subscripts',r'\Sigma,\sigma,M_\sigma,\mathcal F_\sigma',r'\Sigma,\sigma,M_\sigma,\mathcal F_\sigma','resolved','Capital Sigma has two long outer arms joined by an angular middle. The low sign after pour and both display subscripts has a loop plus rightward tail. Earlier zero subscripts are plain small ovals.',source=b,bbox=[525,615,1490,800],extra={'additional_bbox':[1045,100,1150,170]})
cd(2,'First and second power-set letters',r'\unsure{\mathscr P|\mathcal P|\wp}',r'\unsure{\mathscr P|\mathcal P|\wp|P}; \mathscr P','revised','The first tall angular P has no secure lower-left curl, so plain P remains possible. The second has a clear lower-left return and is retained as script P.',crop=16,extra={'additional_crop':by_num[17]['path']})
cd(3,'Bottom operators',r'\mathrm{Inf},\mathrm{Sup}',r'\mathrm{Inf},\mathrm{Sup}','resolved','The first operator begins with a barred capital I and ends in a long-descending f; the last line begins with capital S followed by two lowercase groups.',source=b,bbox=[340,1030,910,1240])
cd(4,'ens at upper l’ens, lower l’ens and d’ens. ordonnés',r'ens; ens; ens.',r'ens; ens; ens.','resolved','Neither of the two l’ens groups has a distinct final point. A separate point follows ens in d’ens. ordonnés.',source=a,bbox=[825,920,1020,1015],extra={'additional_evidence':[{'source':b,'bbox':[1200,95,1410,175]},{'source':b,'bbox':[350,965,820,1035]}]})
cd(5,'Operator after L’application',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','One p descender is present in this abbreviated operator; the adjacent full cosupport shows its two descenders separately.',crop=5)
cd(6,'Cancelled first line, last glyph',r'\unsure{``c|``C|``6}',r'\unsure{``c|``C|``6}','retained','A quote-like pair and inward curl survive; the cross stroke hides the upper part of the final glyph.',crop=1)
cd(7,'Upper adjective before the parenthesis',r'\unsure{minimale}',r'\unsure{minimale}','retained','The worked middle strokes remain inseparable, although the final -ale is readable.',crop=2)
cd(8,'Word after parmi',r'\unsure{celles|telles}',r'\unsure{telles|celles}','revised','The initial tall stem and short right tick favour t. An elongated c remains possible; the reading is not decided from grammar.',crop=3)
cd(9,'Cancelled short word after s’appelle',r'\unsure{du|de}',r'\unsure{du|de}','retained','The d loop is clear; u/e is crossed by the deletion line.',crop=4)
cd(10,'Bijection and raised e',r'\unsure{bij\inserted{e}ction}',r'\unsure{bij\inserted{e}ction}','retained','The raised e-like loop is distinct from the baseline. The reduced word remains uncertain as a whole.',crop=6)
cd(11,'Saturées after des parties',r'\unsure{saturées|saturée}',r'\unsure{saturées|saturée}','retained','The straight final sweep does not settle the terminal s.',crop=7)
cd(12,'Small word before elles',r'\unsure{sur}',r'\unsure{sur}','retained','Three very reduced separated traces allow sur but do not securely form all its letters.',crop=8)
cd(13,'Sign after elles',r'\unsure{=|mêmes}',r'$=$','resolved','Two parallel horizontal strokes are visible. They are transcribed literally, without expanding them to mêmes.',source=a,bbox=[730,1035,880,1120])
cd(14,'Cancelled de before F0',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de}}','retained','The d ascender is visible but the second letter remains under thick crossing ink.',crop=10)
cd(15,'Cancelled On définit',r'\deleted{On \unsure{définit}}',r'\deleted{On \unsure{définit}}','retained','On, a d loop, f descender and terminal upright survive; the interior is partly suppressed.',crop=11)
cd(16,'Live verb before second Sigma',r'\unsure{désidentifie|délibérément identifie|identifie}',r'\unsure{désidentifie|identifie}','revised','One word-sized group is present. Its internal small marks do not settle the expanded first reading, but there is no separate second word supporting délibérément identifie.',crop=13)
cd(17,'Cancelled capital after Sigma de',r'\deleted{$\unsure{\mathcal F}$}',r'\deleted{$\unsure{\mathscr P|\mathcal F}$}','revised','The tall stem and angular bowl look P-like; cancelling diagonals prevent excluding F.',crop=14)
cd(18,'Réalisations',r'\unsure{réalisations}',r'\unsure{réalisations}','retained','The beginning, tall stems and final group support the attempted word, but the medial strokes remain reduced. Two low detached points are separately reproduced.',crop=15)
cd(19,'Repeated context check on the two power-set letters',r'\unsure{\mathscr P|\mathcal P|\wp};\mathscr P',r'\unsure{\mathscr P|\mathcal P|\wp|P};\mathscr P','revised','Local evidence differs: the first is angular and plain-stemmed; the second has a clear lower-left curl. Uncertainty is not propagated to the clearer second occurrence.',crop=17,extra={'additional_crop':by_num[16]['path']})
cd(20,'Old layer in the revised anti compound',r'\deleted{\unsure{isomorph|homéo}}',r'\deleted{\illegible{1}}','revised','After trying the proposed old readings, I cannot isolate a complete old word from the overlapping live letters and crossing stroke. One word is an estimate of the cancelled layer, spatially superposed with the live reading.',crop=18)
cd(21,'Live layer in the revised anti compound',r'\unsure{involution|bijection|dualité}',r'\unsure{involution|bijection|dualité}','retained','Loops, a descender and final uprights are visible, but their allocation between the two layers does not settle the live word. The alternatives are kept within the same correction group.',crop=18)
cd(22,'Low mark before abbreviated cosupport operator',r'\unsure{.} $\unsure{\operatorname{cosup}|\operatorname{cosupp}}$',r'\unsure{.} $\operatorname{cosup}$','revised','The low dash/point is distinct but its punctuation status remains uncertain. The adjacent operator itself has one p.',crop=5)
cd(23,'Accent over ou before cancelled de',r'\unsure{où|ou}','où','resolved','A detached short downward-right stroke over the second vowel is visible and retained as the grave accent.',crop=10)
cd(24,'Partie(s) in the parenthesis',r'\unsure{partie|parties}',r'\unsure{partie|parties}','retained','The terminal dark flat group cannot reliably distinguish e from e plus s.',crop=16)
cd(25,'Inserted M0 de M and F0 de M',r'\inserted{$M_0$} de $M$, \unsure{où|ou} \deleted{\unsure{de}} $\mathcal F_0$ de $M$',r'\inserted{$M_0$} de $M$, où \deleted{\unsure{de}} $\mathcal F_0$ de $M$','resolved','Both M capitals have two clear peaks. The final M is retained despite H’s editorial suggestion to read F. The leader next to the inserted M0 is separately drawn.',source=b,bbox=[200,295,1255,430],extra={'additional_crop':by_num[9]['path']})
cd(26,'Repeated context check on elles =',r'elles \unsure{=|mêmes}',r'elles $=$','resolved','The low pair of approximately horizontal strokes is literal =, with no additional letter shapes for mêmes.',source=a,bbox=[540,1020,880,1125])

inventory=[]
def inv(element,kind,position,objects):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=objects,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('I01','text','Top centre, above the first cancelled line','67')
inv('I02','deletion','Top line across the page','On a une notion de unfinished quotation')
inv('I03','text','Upper body, whole first paragraph','Toute partie de F ... relation d’inclusion.')
inv('I04','deletion','Upper body after qui','s’appelle du/de')
inv('I05','insertion','Above the middle of bijection','Raised e-like letter')
inv('I06','text','Middle body, definition paragraph','On désigne par Sigma l’ens des supports virtuels; supports and virtuels have separate underlines')
inv('I07','insertion','Left of de M in the definition line','M_0')
inv('I08','drawing','Beside the inserted M0, extending down-left','Separate curved oblique insertion leader without arrowhead')
inv('I09','deletion','Between où and F0','de')
inv('I10','deletion','Right end of the definition line','On définit, uncertain inner letters')
inv('I11','deletion','Next physical line','L’application du/de cosupport d/de')
inv('I12','text','Immediately below the cancelled application line','On désidentifie ... ses deux réalisations (comme partie(s) de P(M), ou de P(F)) et on écrit, pour sigma in Sigma')
inv('I13','deletion','After second Sigma de, before ses deux','One P/F-like capital')
inv('I14','drawing','Below the middle of réalisations','Two detached low points, second lower and to the right')
inv('I15','display','Below identification paragraph','M_sigma subset M, F_sigma subset F')
inv('I16','text','Bottom paragraph to page boundary','Dans Sigma ... Inf quelconques ... Sup quelconques (c’est la partie saturée')
inv('I17','deletion','Bottom paragraph after first Dans Sigma,','pour')
inv('I18','deletion','Within the crowded compound after anti','Unreadable older layer, estimated one word; kept spatially superposed')
inv('I19','text','Same crowded correction group after anti','Uncertain surviving involution/bijection/dualité')

remaining=[
 dict(location='Cancelled first-line quotation',reading=r'\unsure{``c|``C|``6}',alternatives=['``c','``C','``6'],confidence='low',reason='Cancellation crosses the upper part of the last looped glyph.'),
 dict(location='Adjective before (parmi ...)',reading=r'\unsure{minimale}',alternatives=[],confidence='medium',reason='Inner min strokes coalesce and are worked over.'),
 dict(location='Word after parmi',reading=r'\unsure{telles|celles}',alternatives=['telles','celles'],confidence='medium',reason='Tall initial stem with right tick favours t but can be an extended c.'),
 dict(location='Cancelled word following s’appelle',reading=r'\unsure{du|de}',alternatives=['du','de'],confidence='medium',reason='Strike line masks the final vowel.'),
 dict(location='Small low mark before cosup',reading=r'\unsure{.}',alternatives=['period-like mark','incidental low ink touch'],confidence='medium',reason='The ink is clear but its punctuation function is not.'),
 dict(location='Bijection with raised letter',reading=r'\unsure{bij\inserted{e}ction}',alternatives=[],confidence='medium',reason='Raised e-like sign is visible; small baseline letters remain compressed.'),
 dict(location='Saturées after des parties',reading=r'\unsure{saturées|saturée}',alternatives=['saturées','saturée'],confidence='medium',reason='Final sweep does not isolate a plural s.'),
 dict(location='Before elles',reading=r'\unsure{sur}',alternatives=[],confidence='medium',reason='The three traces are reduced and partly disconnected.'),
 dict(location='Cancelled de before F0',reading=r'\deleted{\unsure{de}}',alternatives=[],confidence='medium',reason='Second letter remains under dark cancellation.'),
 dict(location='Cancelled On définit',reading=r'\deleted{On \unsure{définit}}',alternatives=[],confidence='medium',reason='The word interior is covered by several crossing lines.'),
 dict(location='Cancelled application line, first short word',reading=r'\unsure{du|de}',alternatives=['du','de'],confidence='medium',reason='Flattened u/e trace lies on the strike.'),
 dict(location='Cancelled application line, last group',reading=r'\unsure{d|de}',alternatives=['d','de'],confidence='low',reason='Only d is individually distinguishable; a second letter cannot be excluded under the strike.'),
 dict(location='Live verb before second Sigma',reading=r'\unsure{désidentifie|identifie}',alternatives=['désidentifie','identifie'],confidence='low',reason='One long group, with unresolved reduced medial letters; two-word expansion is not securely present.'),
 dict(location='Cancelled capital before ses deux',reading=r'\unsure{\mathscr P|\mathcal F}',alternatives=[r'\mathscr P',r'\mathcal F'],confidence='low',reason='Angular P-like bowl remains under diagonal cancellation.'),
 dict(location='Réalisations',reading=r'\unsure{réalisations}',alternatives=[],confidence='medium',reason='Compressed medial letters cannot all be individually identified.'),
 dict(location='Two points below réalisations',reading=points_figure,alternatives=['intentional detached ink marks','incidental pen dots'],confidence='medium',reason='Both points are visible; no textual or mathematical function is assigned.'),
 dict(location='Partie(s) in parenthesis',reading=r'\unsure{partie|parties}',alternatives=['partie','parties'],confidence='medium',reason='A dark level terminal group does not settle final s.'),
 dict(location='First power-set alphabet',reading=r'\unsure{\mathscr P|\mathcal P|\wp|P}',alternatives=[r'\mathscr P',r'\mathcal P',r'\wp','P'],confidence='medium',reason='Tall angular form lacks the clear lower curl of the second occurrence.'),
 dict(location='Anti compound, older layer',reading=r'\deleted{\illegible{1}}',alternatives=['isomorph (not recovered)','homéo (not recovered)'],confidence='low',reason='No complete old word can be isolated from the overwritten group after attempts at the C alternatives.'),
 dict(location='Anti compound, surviving layer',reading=r'\unsure{involution|bijection|dualité}',alternatives=['involution','bijection','dualité'],confidence='low',reason='Loops, descender and final uprights cannot be assigned conclusively between the layers.'),
]

notation=[
 dict(sign='Family F',latex=r'\mathcal F,\mathcal F_0,\mathcal F_\sigma',appearance='Single curved stem with broad bent or looped upper arm; never the Gothic construction proposed by H.',location='First sentence, definition, power-set parenthesis, display, bottom paragraph',alternatives=[]),
 dict(sign='Ambient M',latex=r'M,M_0,M_\sigma',appearance='Two peaked ordinary capital with a curved entry stroke. Zero is round; sigma has a right tail.',location='All occurrences on the page',alternatives=[]),
 dict(sign='Capital and lowercase sigma',latex=r'\Sigma,\sigma',appearance='Capital is angular with long outer bars; lower sigma is looped and runs right.',location='On désigne; On ...; pour sigma; display; two Dans Sigma occurrences',alternatives=[]),
 dict(sign='First power-set letter',latex=r'\unsure{\mathscr P|\mathcal P|\wp|P}',appearance='Tall straight stem and angular broad bowl, without a securely formed lower-left curl.',location='First P(M)',alternatives=[r'\mathscr P',r'\mathcal P',r'\wp','P']),
 dict(sign='Second power-set letter',latex=r'\mathscr P',appearance='Broad bowl with distinct lower-left curl.',location='P(F) on following line',alternatives=[]),
 dict(sign='Cancelled capital',latex=r'\deleted{\unsure{\mathscr P|\mathcal F}}',appearance='Tall stem and angular bowl crossed by diagonals; lower hook survives.',location='After Sigma de and before ses deux',alternatives=[r'\mathscr P',r'\mathcal F']),
 dict(sign='Literal pair of strokes after elles',latex=r'=',appearance='Two nearly parallel separate horizontal strokes.',location='End of first paragraph, after elles',alternatives=[]),
 dict(sign='Abbreviated operator',latex=r'\operatorname{cosup}',appearance='One final descending p stroke.',location='After L’application in first paragraph',alternatives=[]),
 dict(sign='Insertion leader',latex=m0_figure,appearance='Separate curved oblique stroke, down-left from beside raised M0; no arrowhead.',location='Definition of saturated parts',alternatives=[]),
 dict(sign='Detached low point pair',latex=points_figure,appearance='Two small dark points, second slightly lower and to the right.',location='Under the middle of réalisations',alternatives=['incidental pen dots']),
 dict(sign='Order operators',latex=r'\mathrm{Inf},\mathrm{Sup}',appearance='Initial capital I/S, lower following letters, long f descender in Inf.',location='Bottom paragraph',alternatives=[]),
]
abbreviations=[dict(form='resp',expansion='respectivement'),dict(form='ens',expansion='ensemble'),dict(form='ens.',expansion='ensemble'),dict(form='cosup',expansion='cosupport'),dict(form='Inf',expansion='infimum'),dict(form='Sup',expansion='supremum')]

finished=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
report=dict(
 reader='R2',cote='156-4',scan='068',brief_version='v04',started_utc='2026-11-20T10:19:01Z',finished_utc=finished,
 image_views=[whole,a,b],reading_file=str(OUT/'reading.tex'),differences=diffs,c_doubts=c_doubts,inventory=inventory,
 remaining_doubts=remaining,notation=notation,abbreviations=abbreviations,
 notes=dict(
   summary='Handwritten manuscript page 67. The page defines saturated parts/supports, names their set Sigma, introduces its two realizations and begins the paragraph on order operations. All cancelled drafts, the raised e and M0, separate underlines, the M0 leader and two low points under réalisations are included. The page ends inside an open parenthesis.',
   math_reading_decisions='No mathematical assertion was proved or repaired. The paired realizations and the display prompted attention to the unexpected phrase F0 de M; the two visible peaks of M decide its transcription. Local shape comparison distinguishes round zero from looped sigma, one-p cosup from the double-descender full cosupport, and the two P occurrences. The anti compound is kept uncertain because the ink does not settle the old and live layers.',
   author_checks='The author cancels the opening attempt, s’appelle du/de, de before F0, two drafting attempts, a P/F-like capital, pour, and an earlier layer inside the anti compound. The raised letter in bijection and M0 are additions. No explicit completed proof or independent author validation is identifiable on this page.',
   title_dates_pagination='Visible manuscript number 67, scan marker retained as 68. No title, date, page count, archive sheet number, separate marginal sentence or typescript is present. H’s editorial instruction to replace the last M by F is not adopted.'
 ),
 check_events=[],crops=manifest,
 workflow_feedback=['The brief’s requirement to preserve a crowded overwrite as one physical group is helpful, but the supplied inline deletion macro alone cannot express superposed layers. A local TikZ group is used for the anti correction, with an estimated unreadable old layer and uncertain live layer.','All crop bboxes refer explicitly to the named original half. The supplied halves are 1681 by 1260 pixels; the lower half begins at whole-page y=1100. Crops preserve adjacent physical-line context and are not second displays of a whole half.']
)
def exact_strings(value):
    if isinstance(value,str):
        return value.replace(r"\'", "'").replace(r'\n\n', '\n\n')
    if isinstance(value,list):
        return [exact_strings(x) for x in value]
    if isinstance(value,dict):
        return {k:exact_strings(v) for k,v in value.items()}
    return value
report=exact_strings(report)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

observations={
 1:'Unfinished quotation and final c/C/6 remain uncertain; words before it are readable under one long strike.',
 2:'Minimale remains uncertain internally; final -ale clearer.',
 3:'Tall initial with short tick favours telles, retaining celles.',
 4:'Cancelled d is clear; final u/e unresolved; H le rejected.',
 5:'Separate low point retained uncertain; one p establishes cosup.',
 6:'Raised e-like sign is visible; whole word remains uncertain.',
 7:'Final s of saturées not distinguishable from level sweep.',
 8:'Sur remains a best reading of three reduced traces.',
 9:'Plain raised M0 and distinct curved down-left leader; no arrowhead.',
 10:'Separate grave-like mark above ou retained as où; cancelled de stays doubtful; F0 visible.',
 11:'On and parts of définit remain under several strikes; best reading retained uncertain.',
 12:'Cancelled application line readable except du/de and terminal d/de.',
 13:'One word-sized identification verb; de after Sigma is readable.',
 14:'Cancelled P-like capital with F alternative; ses deux is readable.',
 15:'Réalisations still uncertain; two detached low dots observed below its middle.',
 16:'Partie/parties uncertain; first P angular and lacks lower curl; M and sigma membership visible.',
 17:'Second P has clear lower-left curl; parentheses and family F present.',
 18:'One crowded overwritten anti compound; no securely recoverable old word, live alternatives retained.',
}
log=[
 '# R2 inspection log — 156-4 scan 068',
 '',
 'Started image reading after the recorded 2026-11-20T10:19:01Z clock observation. Read only the assigned packet, brief v04 and notation snapshot. No other reader, previous scan, OCR, outside research, delegation or LaTeX compiler was used.',
 '',
 f'1. Viewed whole page once: {whole}. Layout: manuscript number; cancelled opening; first paragraph; saturated-part definition and corrections; one display; lower paragraph continuing at the bottom edge. No mathematical diagram or separate margin sentence.',
 f'2. Viewed upper supplied half once: {a}. Read every line against C and H. Open places listed for crops 01–08; literal = and several alphabet/punctuation differences settled on this half.',
 f'3. Viewed lower supplied half once: {b}. Read every line, display, insertion and cancellation against C and H. Open places listed for crops 09–18. Sigma/subscripts, capital Inf/Sup, plain M after F0, missing terminal commas/periods and local alphabet distinctions inspected.',
 '',
 'Own crops were created together by make_crops.py, each from its named original half. No target was recropped. Every crop was viewed once, in batches of at most three; all three images in each batch were displayed successfully. No displayed crop was truncated in the tool output. Zero rotation was used throughout.',
 ''
]
for n,spec in enumerate(manifest,1):
    log += [f'{n+3}. Viewed {spec["path"]}',f'   Source: {spec["source"]}; original bbox: {spec["bbox"]}; scale: {spec["scale"]:.9f}; rotation: 0 degrees.',f'   Transformations: {"; ".join(spec["transformations"])}.',f'   Evidence: {observations[n]}']
log += ['', 'Structural verification only: JSON parse, exact required metadata/array fields, original-image bbox bounds, existing crop paths, complete C-context dispositions, balanced TeX braces and math delimiters, preserved scan/page markers, and inventory inclusion checks. No compilation or mathematical proof was performed.',f'Finished: {finished}.']
(OUT/'inspection_log.md').write_text('\n'.join(log)+'\n')
print(json.dumps({'differences':len(diffs),'c_doubts':len(c_doubts),'inventory':len(inventory),'remaining_doubts':len(remaining),'crops':len(manifest),'finished_utc':finished},indent=2))
