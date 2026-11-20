from pathlib import Path
from datetime import datetime, timezone
import json, re
R=Path('/workspace/scratch/94548b74fbe0/out/readers/013/B')
manifest=json.loads((R/'crop_manifest.json').read_text())
for c in manifest: c['viewed']=True
(R/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
tex=[r'\scanpage{13}',r'% Complete independent reading B. All drawing coordinates follow the original full scan.',r'% Doubt alternatives are editorial; no mathematical reconstruction is supplied.',r'\figure{\resizebox{\linewidth}{!}{%',r'\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round,',r'  every node/.style={inner sep=0pt,font=\fontsize{12}{14}\selectfont}]',r'\useasboundingbox (20,65) rectangle (2354,1668);']
inv=[]
def inventory(element,kind,position,words,hand='his hand',**extra):
 d=dict(sheet_kind='cover',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes');d.update(extra);inv.append(d)
def write(s): tex.append(s)
def node(id,x,y,content,anchor='base',font=None,color=None):
 opts=['anchor='+anchor]
 if font:opts.append('font=\\fontsize{%s}{%s}\\selectfont'%(font,font+2))
 if color:opts.append('text='+color)
 write('%% %s\n\\node[%s] (%s) at (%s,%s) {%s};'%(id,','.join(opts),id,x,y,content))
def draw(id,path,style='line width=.45pt'):
 write('%% '+id+'\n\\draw['+style+'] '+path+';')
def faint_graph(id,x,y,w,h,commands,purpose,hand='undetermined hand'):
 commands=re.sub(r'(radius=)([0-9.]+)(?=[,\]])',lambda m:m[1]+format(float(m[2])*.01,'.5f')+'cm',commands)
 write('%% '+id+': '+purpose+'; shape preserved, role/hand/surface origin unresolved.')
 write('\\node[anchor=base west] at (%s,%s) {\\unsure{\\begin{tikzpicture}[baseline=(current bounding box.south),x=.01cm,y=-.01cm,line cap=round,line join=round]\n\\useasboundingbox (0,0) rectangle (%s,%s);\n%s\n\\end{tikzpicture}}};'%(x,y+h,w,h,commands))
 inventory(id,'drawing',f'full-scan box ({x},{y})–({x+w},{y+h})',purpose,hand=hand,components=commands)
# Table is reproduced as one connected ruled drawing, with its written cell text.
inventory('B013.table','drawing','entire page','six-column ruled table',hand='undetermined hand')
write('% G-grid: connected table rules. Pale intermediate rules are retained as pale paths.')
for x,xt in [(403,394),(792,790),(1186,1184),(1566,1571),(1967,1970)]:
 draw('G-grid-vertical-'+str(x),f'({x},207)--({xt},1667)','black!18,line width=.24pt')
rows=[(123,129,45),(209,212,45),(285,294,12),(555,562,40),(639,647,25),(752,761,35),(839,846,28),(930,930,13),(1089,1093,75),(1204,1208,45),(1299,1304,45),(1564,1572,42)]
for y,z,g in rows:
 draw('G-grid-horizontal-'+str(y),f'(23,{y})--(791,{y})--(1568,{round((y+z)/2)})--(2351,{z})',f'black!{g},line width=.27pt')
draw('G-grid-thickening-2227','(2227,1303)--(2237,1303)','line width=.7pt')
# Headings and numbering.
cols=[(215,'1','A','(1976/77)'),(593,'5','B','(1978/79)'),(986,'7','C','(1979/80)'),(1357,'15','D','(1980)'),(1746,'20','E','(1981)'),(2153,'23','E','(1981)')]
for j,(x,n,L,date) in enumerate(cols,1):
 node('heading'+str(j),x,126,'Notes',font=14)
 node('notes-number'+str(j),x,207,n,font=14)
 inventory(f'B013.heading{j}','text',f'column {j}, top','Notes '+n)
# First cancelled A/date: readable wording and observed oblique hatching.
node('cancelled-date',83,292,r'\resizebox{2.42cm}{!}{\rlap{A (1976/77)}\phantom{\deleted{A (1976/77)}}}',anchor='base west',font=13)
for k,(x1,y1,x2,y2) in enumerate([(88,285,101,248),(99,289,122,246),(112,290,136,245),(126,292,151,247),(140,292,167,245),(154,294,182,245),(168,293,196,244),(182,294,211,242),(195,295,226,241),(210,294,241,240),(225,295,255,243),(241,296,271,240),(257,296,285,244),(272,297,299,241),(287,295,314,255)],1):
 draw('cancelled-date-hatch-'+str(k),f'({x1},{y1})--({x2},{y2})','line width=.65pt')
inventory('B013.cancelled-date','deletion','column 1, between Notes 1 and live A','A (1976/77); oblique hatching',components='cancelled-date-hatch-1 through -15')
# Pale overwritten A and its surrounding surviving pale curves. Source doubt row 1.
node('old-A',205,579,r'\rlap{A}\phantom{\deleted{A}}',font=16,color='black!35')
faint_graph('G-old-A-curves',168,556,72,34,r'\draw[black!25,line width=.4pt] (5,4) .. controls (0,18) and (8,24) .. (15,30);\draw[black!20,line width=.4pt] (65,6) .. controls (69,15) and (66,22) .. (63,28);','pale outer curves beside the lower A')
for j,(x,n,L,date) in enumerate(cols,1):
 node('letter'+str(j),[205,568,977,1332,1732,2128][j-1],557,L,font=20)
 node('date'+str(j),[214,586,982,1335,1740,2133][j-1],641,date,font=13)
 inventory(f'B013.letter-date{j}','text',f'column {j}, letter and date',L+' '+date)
inventory('B013.old-A','deletion','column 1, immediately below and overlapped by dark A','pale A',reading_state='overwritten; glyph resolved, no chronology beyond the overlap asserted')
# Left margin, preserved in its actual relationship to the table.
write('% G-margin: barred upward arrow meeting the brace; duplicated/pale continuations remain explicit.')
draw('G-margin-top-bar','(32,414)--(64,414)','line width=.6pt')
draw('G-margin-up-shaft','(48,421)..controls (50,500) and (41,585)..(43,657)--(40,667)','black!55,line width=.48pt')
draw('G-margin-up-head','(35,436)--(48,421)--(62,436) (49,421)--(61,424)','line width=.6pt')
draw('G-margin-left-return','(47,493)..controls (41,545) and (39,607)..(38,655)--(42,671)--(46,677)','black!40,line width=.36pt')
draw('G-margin-inner-loop','(51,557)..controls (42,574) and (45,596)..(52,609)','line width=.35pt')
draw('G-margin-main-brace','(64,495)..controls (54,492) and (55,538)..(56,573)..controls (57,621) and (54,653)..(43,666)..controls (59,668) and (62,685)..(64,725)..controls (66,775) and (64,837)..(72,846)','line width=.58pt')
draw('G-margin-pale-brace','(48,673)..controls (55,690) and (54,714)..(54,748)..controls (54,794) and (50,838)..(55,845)','black!25,line width=.45pt')
node('upper-question',86,616,'?',font=17)
draw('G-margin-down','(119,556)..controls (120,566) and (119,574)..(119,579) (112,568)--(119,579)--(124,573)','black!70,line width=.4pt')
draw('G-margin-middle-curve','(120,580)..controls (121,588) and (116,596)..(111,596)..controls (117,598) and (119,605)..(118,611)','black!55,line width=.38pt')
draw('G-margin-up','(120,636)..controls (117,626) and (119,619)..(118,611) (109,622)--(118,611)--(127,621)','black!70,line width=.4pt')
inventory('B013.margin','margin note','left side, y414–846','barred up arrow, brace, ?, opposed arrows; connected and retraced strokes',components='G-margin-top-bar, up-shaft, up-head, left-return, inner-loop, main-brace, pale-brace, down, middle-curve, up')
faint_graph('G-margin-point',44,399,9,12,r'\fill[black!35] (4,6) ellipse [x radius=1.2,y radius=2.1];','detached small gray point above the arrow bar')
# Two bent arrows between first date and title; each visible additional component is retained.
draw('G-bent-upper','(254,667)--(320,668)--(319,643) (312,649)--(319,643)--(326,653)','line width=.5pt')
faint_graph('G-bent-upper-arch',257,653,27,17,r'\draw[black!35,line width=.35pt] (3,12)..controls (14,2) and (19,2)..(22,7);','pale arch immediately above the left part of the upper bent arrow')
faint_graph('G-bent-upper-dash',303,648,12,9,r'\draw[black!65,line width=.4pt] (3,3)--(7,5);','short detached oblique stroke left of upper arrowhead')
faint_graph('G-bent-upper-dot',301,670,9,10,r'\fill[black!45] (4,4) ellipse [x radius=1.2,y radius=1.6];','small point below the upper bent-arrow shaft')
draw('G-bent-lower','(255,701)..controls (277,710) and (301,704)..(326,712)--(327,735) (319,728)--(327,737)--(334,731)','line width=.55pt')
draw('G-bent-lower-retrace','(254,712)--(280,712)--(303,710)--(315,708)','black!65,line width=.38pt')
inventory('B013.bent-arrows','drawing','column 1, between date and Découverte','two bent arrows and the lower retraced horizontal stroke',components='G-bent-upper, G-bent-lower, G-bent-lower-retrace')
faint_graph('G-date-hook',401,616,17,25,r'\draw[black!55,line width=.35pt] (11,3)..controls (11,11) and (8,16)..(5,20);\draw[black!25,line width=.25pt] (5,21)--(4,24);','short hook meeting the first date-row rule near the column boundary')
# Main title cells.
node('title1a',218,752,'Découverte',font=14)
node('title1b',201,786,'de la',font=11)
node('title1c',236,838,'Méditation',font=14)
inventory('B013.title1','text','column 1, main title','Découverte / de la / Méditation')
# The broken diagonal is recorded graphically, without assigning a cancellation target.
node('title2a',586,753,'Réveil',font=14)
faint_graph('G-Reveil-diagonal',498,692,61,63,r'\fill[black] (3,4)..controls (7,0) and (11,6)..(13,11)--(8,10)--cycle;\draw[black!65,line width=.4pt] (15,15)--(20,21);\draw[black!45,line width=.3pt] (23,24)--(31,32);\draw[black!45,line width=.35pt] (45,49)--(55,59);','interrupted oblique stroke passing through the initial R; cancellation role unresolved')
node('title2b',576,790,'en',font=11)
node('old-C-Ca',525,837,r'\rlap{\unsure{C|Ca}}\phantom{\deleted{\unsure{C|Ca}}}',font=14,color='black!65')
node('title2c',615,839,'Cascades',font=14)
inventory('B013.title2','text','column 2, main title','Réveil / en / Cascades')
inventory('B013.old-C-Ca','deletion','column 2, beginning of Cascades','overlapping C or Ca',reading_state='overwritten reading retained with C|Ca doubt')
for ident,x,y,s,font in [('title3a',966,752,'Die Eltern',14),('title3b',970,839,'(Les parents)',13),('title4a',1348,752,'Das Kind',14),('title4b',1350,839,"(L'enfant)",13),('title5a',1754,754,'Der Baumeister',14),('title5b',1757,840,'(Le Bâtisseur)',13),('title6a',2153,759,'Le Bâtisseur',14)]:node(ident,x,y,s,font=font)
for j,s in [(3,'Die Eltern (Les parents)'),(4,"Das Kind (L'enfant)"),(5,'Der Baumeister (Le Bâtisseur)'),(6,'Le Bâtisseur')]:inventory(f'B013.title{j}','text',f'column {j}, main title',s)
# Small discrete marks in the title area, with no supplied alphabetic or punctuational role.
faint_graph('G-Baumeister-upper-gray',1789,697,10,12,r'\fill[black!40] (5,5) circle [radius=1.5];','gray point above Baumeister')
faint_graph('G-Baumeister-upper-black',1850,695,14,14,r'\fill[black] (4,9)--(6,4)--(10,4)--(9,9)--(6,11)--cycle;\draw[black!25,line width=.25pt] (10,4)--(12,3);','dark point with a pale short continuation above the final part of Baumeister')
faint_graph('G-Baumeister-left-gray',1689,730,9,10,r'\fill[black!35] (4,4) ellipse [x radius=1.0,y radius=1.8];','small gray point between Der and the B')
faint_graph('G-Baumeister-right-gray',1897,736,12,13,r'\draw[black!25,line width=.3pt] (5,4)--(5,8);','faint short upright after Baumeister')
# Hatched-out subdivision row. The original candidate is carried in invisible deletion boxing;
# actual cancellation strokes are drawn, rather than a new generic horizontal strike.
cancel_specs=[('A',205,r'(\unsure{\mathrm i})',[(185,923,200,895),(189,932,208,904),(197,931,217,905),(205,930,223,911)]),('B',587,r'(\unsure{\mathrm{ii}|\mathrm i})',[(557,930,582,898),(561,931,595,898),(568,930,606,907),(583,934,615,918)]),('C',975,r'(\unsure{\mathrm i|\mathrm{ii}})',[(949,922,975,897),(955,929,983,904),(971,931,994,913),(973,932,997,926)]),('D',1344,r'(\unsure{\mathrm i})',[(1318,919,1336,903),(1322,921,1345,907),(1325,924,1356,912)]),('E20',1743,r'(\unsure{\mathrm i|\mathrm{ii}})',[(1718,920,1735,903),(1721,923,1742,905),(1725,925,1757,908)]),('E23',2161,r'(\unsure{\mathrm{iii}|\mathrm{iv}})',[(2128,918,2144,903),(2130,920,2157,904),(2146,923,2172,909),(2148,924,2185,913)])]
for label,x,candidate,strokes in cancel_specs:
 node('cancel-'+label,x,932,r'\rlap{$'+candidate+r'$}\phantom{\deleted{$'+candidate+r'$}}',font=11)
 for k,(x1,y1,x2,y2) in enumerate(strokes,1):draw('hatch-'+label+'-'+str(k),f'({x1},{y1})--({x2},{y2})','line width=.6pt')
 inventory('B013.cancel-'+label,'deletion','crossed subdivision in column '+label,candidate+'; actual oblique hatching',components=[f'hatch-{label}-{i+1}' for i in range(len(strokes))])
draw('cancel-C-terminal-hook','(993,926)..controls (998,925) and (1000,930)..(1000,934)','line width=.45pt')
draw('cancel-E23-terminal-hook','(2190,925)..controls (2196,923) and (2197,930)..(2201,934)','line width=.5pt')
for label in ['C','E23']:inventory('B013.cancel-'+label+'-hook','drawing','right end of crossed subdivision '+label,'low curved terminal hook',components='cancel-'+label+'-terminal-hook')
faint_graph('G-cancel-C-gray-point',938,892,12,12,r'\fill[black!35] (3,3)--(7,2)--(8,6)--(4,7)--cycle;','small gray patch above-left of the crossed C subdivision')
# Lower question and faint arrow: ? is resolved; shaft has a curled upper end.
node('lower-question',132,975,'?',font=15,color='black!40')
draw('G-lower-A-arrow','(172,922)..controls (162,914) and (157,919)..(158,934)--(158,996) (150,991)--(158,1001)--(167,992)','black!25,line width=.45pt')
inventory('B013.lower-question-arrow','margin note','column 1, under crossed subdivision','? and faint downward arrow with curved upper end',components='lower-question and G-lower-A-arrow')
draw('G-lower-B-arrow','(527,1029)..controls (528,1040) and (532,1046)..(535,1049)--(540,1054) (528,1045)..controls (532,1051) and (536,1051)..(538,1045)','black!40,line width=.35pt')
inventory('B013.lower-B-arrow','drawing','column 2, above-left of live (ii)','curved descending arrow, with shaft continuing a short distance down-right',components='G-lower-B-arrow')
# Live subdivision row and pale local forms.
node('old-sub-A',186,1124,r'\unsure{(i)|\deleted{(i)}}',font=10,color='black!25')
node('live-sub1',187,1090,'(i)',font=12)
node('live-sub2',582,1090,'(ii)',font=12)
node('old-sub-C-left',943,1083,r'\unsure{(|\deleted{(}}',font=11,color='black!35')
faint_graph('G-live-C-gray-dot',961,1047,11,13,r'\draw[black!40,line width=.35pt] (5,3)--(6,8);','pale raised short stroke over the C subdivision i')
faint_graph('G-live-C-right-curve',978,1056,15,32,r'\draw[black!30,line width=.4pt] (5,3)..controls (14,12) and (11,21)..(2,27);','pale curve adjoining the right parenthesis of the live C subdivision')
node('live-sub3',964,1090,'(i)',font=12)
node('old-sub-D',1344,1068,r'\rlap{(i)}\phantom{\deleted{(i)}}',font=11,color='black!45')
node('live-sub4',1346,1090,'(i)',font=12)
node('live-sub5',1746,1090,'(i)',font=12)
node('live-sub6',2144,1090,'(iv)',font=12)
for j,(x,s) in enumerate([(187,'(i)'),(582,'(ii)'),(964,'(i)'),(1346,'(i)'),(1746,'(i)'),(2144,'(iv)')],1):
 inventory(f'B013.live-sub{j}','text',f'column {j}, lower subdivision row',s)
inventory('B013.old-sub-A','deletion','below the live first (i)','pale (i), live/deleted state unresolved',reading_state='live primary; deleted alternative; glyph resolved')
inventory('B013.old-sub-C-left','deletion','left of live third opening parenthesis','pale (, retraced/live versus deleted state unresolved',reading_state='live primary; deleted alternative; glyph resolved')
inventory('B013.old-sub-D','deletion','upper overlapping form at the fourth live subdivision','pale (i) overlaid by lower dark (i)',reading_state='overwritten; glyph resolved')
# Second titles: preserve their physical title and translation lines.
for ident,x,y,s,font in [('lower-title1',185,1204,'Envol',14),('lower-title2',593,1204,'Vers un plus long Voyage',12),('lower-title3',1001,1203,'Bild und Wahrheit',14),('lower-trans3',971,1299,'(Image et Réalité)',13),('lower-title4',1344,1204,'Der Wolf',15),('lower-trans4',1351,1300,'(Le Loup)',13),('lower-title5',1769,1206,'Spiel- und Sucht',14),('lower-trans5',1763,1301,'(Jeu - et Fringale)',13),('lower-title6',2152,1207,"Le ``Maître''",15)]:node(ident,x,y,s,font=font)
for j,s in [(1,'Envol'),(2,'Vers un plus long Voyage'),(3,'Bild und Wahrheit (Image et Réalité)'),(4,'Der Wolf (Le Loup)'),(5,'Spiel- und Sucht (Jeu - et Fringale)'),(6,"Le ``Maître''")]:inventory(f'B013.lower-title{j}','text',f'column {j}, second title',s)
faint_graph('G-long-dot',588,1235,13,11,r'\draw[black,line width=.45pt] (3,6)--(7,4);','small detached dark dash below the tail of long')
faint_graph('G-Jeu-overmark',1612,1255,12,12,r'\fill[black!70] (3,5)--(7,4)--(4,7)--cycle;','small triangular overmark above the J of Jeu')
faint_graph('G-Spiel-lower-spot',1695,1223,12,13,r'\fill[black!25] (5,6) ellipse [x radius=1.8,y radius=1.5];','small gray spot below the end of Spiel')
# Other discrete graphical traces; no letters, numerals, punctuation or mathematical function are assigned.
faint_graph('G-A-blank-trace',224,1404,17,39,r'\fill[black!80] (11,4)--(9,8)--(11,11)--(8,14)--(5,13)--(6,8)--cycle;\fill[black!85] (8,17) ellipse [x radius=2,y radius=1.5];\fill[black!30] (8,25) ellipse [x radius=1.8,y radius=1.5];\fill[black!30] (4,32) ellipse [x radius=1.6,y radius=1.4];\fill[black!30] (5,36) ellipse [x radius=1.6,y radius=1.2];','short upper dark trace followed by separated dark and pale spots below Envol')
faint_graph('G-A-foot-trace',329,1578,17,37,r'\fill[black!25] (12,5) ellipse [x radius=2,y radius=2];\fill[black!45] (11,11) circle [radius=1.5];\fill[black!60] (8,16) ellipse [x radius=1.5,y radius=2];\fill[black!35] (6,22) circle [radius=1.5];\fill[black!45] (7,26) ellipse [x radius=1,y radius=1.5];\fill[black!50] (4,30) ellipse [x radius=2,y radius=1.3];\fill[black!20] (4,34) ellipse [x radius=2,y radius=1.3];','descending oblique cluster of small spots below the first foot cell')
faint_graph('G-E23-dash',2248,1338,25,13,r'\draw[black!65,line width=.4pt] (4,6)--(20,6);','short horizontal dash below the last second-title cell')
faint_graph('G-E20-blot',1926,1353,15,19,r'\fill[black!25] (6,3)--(9,4)--(11,8)--(9,12)--(6,14)--(3,13)--(5,11)--(4,7)--cycle;','small gray irregular blot below the Fringale cell')
faint_graph('G-D-point',1490,1517,10,11,r'\fill[black!70] (4,5) circle [radius=1.4];','tiny isolated point to the right of the Sch I cell')
faint_graph('G-A-edge-slant',368,1013,24,31,r'\fill[black!20] (4,5) ellipse [x radius=2.5,y radius=3];\fill[black!35] (7,11) ellipse [x radius=2,y radius=2.5];\fill[black!35] (10,16) ellipse [x radius=2.5,y radius=2];\fill[black!30] (14,21) ellipse [x radius=1.5,y radius=1.8];\fill[black!30] (18,25) ellipse [x radius=2,y radius=1.7];\fill[black!25] (12,7) circle [radius=1.7];','pale broken oblique cluster near the first column right boundary below the cancelled row')
# Foot cells, with the exact baseline star and numeral bars.
for j,(x,s) in enumerate([(203,r'M $1976\mathord{*}$'),(573,'M 1979'),(946,r'HS $\mathrm I$'),(1312,r'Sch $\mathrm I$'),(1746,r'Sch $\overline{\underline{\mathrm{VI}}}$'),(2147,r'Sch $\overline{\underline{\mathrm{IX}}}$')],1):
 node('foot'+str(j),x,1564 if j<6 else 1573,s,font=15)
 inventory(f'B013.foot{j}','text',f'column {j}, foot',s)
# Ten surviving groups at the cut right edge: each corresponds to one original C path.
edge=[('01',[(2342,117),(2351,128),(2343,127)]),('02',[(2344,202),(2351,208),(2341,206)]),('03',[(2337,364),(2351,376),(2339,372)]),('04',[(2337,419),(2351,425),(2338,428)]),('05',[(2330,551),(2343,562),(2334,560)]),('06',[(2334,640),(2348,648),(2335,649)]),('07',[(2335,965),(2345,977),(2335,974)]),('08',[(2332,1081),(2344,1092)]),('09',[(2335,1198),(2341,1205)]),('10',[(2335,1566),(2338,1577)])]
for ident,points in edge:
 draw('G-edge-'+ident,'--'.join('(%s,%s)'%p for p in points),'black!80,line width=.45pt')
 inventory('B013.edge'+ident,'drawing','cut right edge, full y'+str(points[0][1]),'surviving short stroke group '+ident,hand='undetermined hand',components='G-edge-'+ident,C_path_index=int(ident))
write(r'\end{tikzpicture}}}')
write('% archive sheet number: 12')
inventory('B013.archive','text','lower-right corner, written sideways','12 (archive sheet number; comment only)',hand='another unnamed hand')
(R/'reading.tex').write_text('\n'.join(tex)+'\n')
(R/'inventory_work.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
print('Wrote complete reading.tex with',len(inv),'inventory entries.')
