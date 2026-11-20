from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/C')
packet=Path('/workspace/scratch/006c0e32b2af/packets/scan075')
page=(packet/'C.tex').read_text()
point_graphic=r'''\margin{\vspace*{1.4em}\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\fill (-0.22,-0.07)
 .. controls (-0.27,0.06) and (-0.16,0.16) .. (-0.08,0.17)
 .. controls (-0.04,0.30) and (0.06,0.25) .. (0.11,0.14)
 .. controls (0.25,0.10) and (0.27,-0.03) .. (0.15,-0.11)
 .. controls (0.04,-0.15) and (-0.15,-0.16) .. (-0.22,-0.07) -- cycle;
\fill (0.37,0.72)
 .. controls (0.34,0.85) and (0.44,0.95) .. (0.50,0.98)
 .. controls (0.54,1.10) and (0.65,1.11) .. (0.71,1.00)
 .. controls (0.83,0.94) and (0.77,0.85) .. (0.68,0.81)
 .. controls (0.73,0.69) and (0.64,0.62) .. (0.53,0.65)
 .. controls (0.44,0.63) and (0.38,0.65) .. (0.37,0.72) -- cycle;
\end{tikzpicture}%
}}}'''
assert page.count(r'\margin{\unsure{:}}')==1
page=page.replace(r'\margin{\unsure{:}}','')
page=page.replace('Soit le diagramme :\n\n', 'Soit le diagramme :\n\n% Detached pair beside the upper diagram row; punctuation value unresolved.\n'+point_graphic+'\n\n')
page=page.replace(r'\unsure{schéma} lisse',r'\unsure{schéma} lisse')
(root/'reading.tex').write_text(page)
meta=json.loads((packet/'meta.json').read_text())
crops=json.loads((root/'crop_log.json').read_text())
for crop in crops:
 crop['requested_deliveries']=1
 crop['actual_views']=1
crop_by_id={x['id']:x['file'] for x in crops}

def decision(id,place,c_reading,reading,diff_c,c_doubt,unresolved,alternatives,confidence,kind,scan_shows,bbox,crop=''):
 return dict(id=id,place=place,c_reading=c_reading,h_reading=None,reading=reading,diff_c=diff_c,diff_h=False,c_doubt=c_doubt,unresolved=unresolved,alternatives=alternatives,confidence=confidence,kind=kind,scan_shows=scan_shows,crop=crop,bbox=bbox)

decisions=[
 decision('C075-01','Upper-left slanted pencil note, first word',r'\unsure{joindre}',r'\unsure{joindre}',False,True,True,['joindre'],'low','other','A long descending initial with a low loop is followed by a rounded arch, short joined strokes, one tall d-like stroke, and a terminal small loop and rightward tail. The interior letters remain compressed even after rotation; the doubtful word is retained without supplying missing strokes.',[45,65,148,145],crop_by_id['note']),
 decision('C075-02','Introduction of the cotangent complex after Soit enfin',r'\unsure{K|\mathbb{K}}',r'\unsure{K|\mathbb{K}}',False,True,True,[r'K',r'\mathbb{K}'],'medium','misread symbol or index','The capital has two very close dark vertical traces at the top of its left stem, joined in a dense blue mass below, and two clear oblique arms to the right. The image does not decide a deliberate second stem against retracing. Later parenthesized examples have a single stem.',[1154,975,1186,1012],crop_by_id['introduced_K']),
 decision('C075-03','Word before lisse',r'\unsure{schéma}',r'\unsure{schéma}',False,True,True,['schéma'],'medium','other','The sequence schém is legible, including a separate acute stroke. The terminal area contains several dense overlapping blue loops and a small loop at the right. The intended final a remains the best reading, but the overlapping strokes do not permit a separate readable undertext or secure removal of the doubt.',[946,1126,1064,1170],crop_by_id['schema']),
 decision('C075-04','Detached marks far right of the upper row of diagram (2)',r'\margin{\unsure{:}}',point_graphic,True,True,True,['two unassigned detached marks',':','incidental marks'],'high','drawing or diagram','Two compact dark forms lie on a rising diagonal: the lower-left form has a broad rounded base and a short upper point; the upper-right form is taller, with a lobed upper-right contour and a rounded lower-left part. Their centres are offset horizontally by roughly 5 pixels and vertically by roughly 7 pixels. Neither is a vertical shaft or attached formula punctuation. Their shape and placement are reproduced without assigning a colon.',[1539,1359,1558,1379],crop_by_id['marginal_points']),
 decision('C075-05','Sentence after the full stop following catégorie dérivée',"il s'obtient", "il s'obtient",False,False,False,[],'high','other','The first letter has a short upright and a separate dot; the adjacent l has a tall closed loop. The first letter is lower-case i, despite beginning a sentence after a full stop.',[1090,1048,1250,1096],crop_by_id['sentence_il']),
 decision('C075-06','Group-definition paragraph, first word of the second line',"d'extensions", "d'extensions",False,False,False,[],'high','other','After the closed o and the two-stroke n, the word ends in a separate hooked s contour curving down at the right. The plural ending in C is retained.',[297,970,465,1014],crop_by_id['extensions_ending']),
 decision('C075-07','Pale fleck below the end of Ext in display (1)','', '',False,False,False,[],'medium','other','The crop shows a very small grey triangular fleck below the formula, without a blue pen outline, shaft, or attachment to a character. Its appearance is comparable to the other grey surface specks in the crop. It is not read as an independent authored mathematical or punctuation sign, and no token is inserted.',[1028,1248,1041,1261],crop_by_id['ext_detached_trace']),
 decision('C075-08','Label of the first display','(1)','(1)',False,False,False,[],'high','other','The central numeral is a short single upright between two curved parentheses. The isolated small speck higher and to the left is beside the opening parenthesis, not over the central upright; it does not establish a dotted i. The label remains (1).',[201,1206,246,1255],crop_by_id['formula_label'])
]
body_hand='named other hand: P. Deligne (attribution in supplied H description; this sheet is unsigned)'
pencil_hand='his hand (pencil-note attribution in supplied H description)'
def inv(element,kind,position,first,hand=body_hand):
 return dict(sheet_kind='letter',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes')
inventory=[
 inv('Slanted pencil note','margin note','upper left, x45–232 y64–242',r'\unsure{joindre}; SGA 7; ruled VI; ?; App.; ruled II',pencil_hand),
 inv('Date and location line','text','upper right, x782–1358 y74–116','Bures sur Yvette, le 21 octobre 1968'),
 inv('Salutation','text','upper centre-left, x524–803 y213–268','Cher Grothendieck,'),
 inv('Opening paragraph','text','x294–1398 y342–466',"En fait, il n'est pas nécessaire"),
 inv('Underlined proposition','text','x293–1480 y503–635','proposition : Soit X un espace analytique complexe compact.'),
 inv('Reduction paragraph','text','x301–1535 y659–785','On se ramène à supposer montrer que si X_0'),
 inv('Cancelled word in the reduction paragraph','deletion','x687–794 y674–703','supposer'),
 inv('Square-zero implication','display','x365–1141 y810–856',r'(X_0\text{ est un schéma})\Longrightarrow(X\text{ est un schéma})'),
 inv('Definitions of extension groups and cotangent complex','text','x299–1535 y886–1180',r'Soit E^{\mathrm{an}}(X_0,\mathscr{N}) et E^{\mathrm{alg}}(X_0,\mathscr{N})'),
 inv('Dense terminal correction or retracing within schéma','text','x1028–1064 y1147–1168',r'\unsure{schéma}; no independently readable prior letter'),
 inv('Display labelled (1)','display','x203–1287 y1205–1254',r'\mathscr{H}om(K,\mathscr{N}) et \mathscr{E}xt^1(K,\mathscr{N}) .'),
 inv('Diagram introduction','text','x424–732 y1286–1331','Soit le diagramme :'),
 inv('Two-row comparison diagram labelled (2)','diagram','x195–1318 y1351–1535','0; H^{1^{alg}}; E^{alg}; H^0; 0; H^{1^{an}}; E^{an}; H^{0^{an}}; six rightward arrows; three downward arrows; alpha and beta labels'),
 inv('Detached diagonal pair','drawing','right margin by upper diagram row, x1539–1558 y1359–1379','Two separate compact dark shapes, uncertain punctuation value','unnamed hand'),
 inv('Closing argument paragraph','text','x297–1480 y1564–1765','Vu les significations (locales) de (1), les lignes sont exactes ;'),
 inv('Cancelled earlier formulation in the final line','deletion','x296–774 y1718–1763',r'comparer les images de \alpha et \beta'),
 inv('Archive sheet number, recorded only as a comment','text','bottom left, x56–113 y1923–1971','74','unnamed hand')
]
report={
 'scan':75,'reader':'C','image_views':meta['images'],'reading_path':str(root/'reading.tex'),'crops':crops,'decisions':decisions,'inventory':inventory,
 'notes':"Handwritten French letter on squared paper, dated Bures sur Yvette, le 21 octobre 1968, addressed Cher Grothendieck. The supplied H description attributes the blue-ink letter to P. Deligne and the pencil note to Grothendieck; there is no signature on this sheet. The page states a criterion for a compact complex analytic space to be a scheme, reduces it to a square-zero extension, and writes a comparison diagram for algebraic and analytic extension groups. These are the author's claims; no proof verification was undertaken. The underlined word proposition is a local heading, not a separate document title. No manuscript page number, written sheet count, closing, or signature occurs. Archive number 74 is recorded only as a comment. The pencil note contains an authorial question mark after the ruled VI reference. Three original lexical/alphabet doubts (joindre, K versus blackboard K, and schéma) are retained. The uncertain marginal colon is represented by its observed diagonal pair of shapes. Pale isolated surface flecks inspected below Ext and beside the first label were not treated as authored mathematical signs. H has description only: all h_reading values are null and all diff_h values false.",
 'math_reading_decisions':[
  r'The criterion has X_{\mathrm{red}}: joined lowered red, without an added acute accent. The other point suffixes are small lowered ovals read as 0 in X_0.',
  r'The ideal is represented by \mathscr{N}: a rising left loop and a narrow tall stroke ending in a small loop recur in the prose and all formula arguments.',
  r'The extension-group E is an ordinary capital with a single upright and short horizontal arms. Its qualifiers an and alg are raised words, not subscripts.',
  r'The Hom and Ext initials have looped cursive forms, retained as \mathscr{H}om and \mathscr{E}xt; their following letters remain on the ordinary formula baseline. The Ext degrees are short raised single strokes, read as 1.',
  r'The first introduced K retains the explicit K versus \mathbb{K} doubt. The later K letters in parentheses show single stems and remain ordinary K.',
  r'The diagram retains H^{1^{\mathrm{alg}}} and H^{1^{\mathrm{an}}}, with the qualifiers on a second rise beside the degree. Its upper-right H has only the degree 0; the lower-right term is H^{0^{\mathrm{an}}}. No alg has been supplied to the upper-right term.',
  r'The diagram contains six rightward arrows and three downward arrows. The final horizontal arrow of the upper row is labelled \alpha; that of the lower row is labelled \beta. No terminal arrow after the rightmost object is present.',
  r'The earlier implication has two parallel shafts and a right-pointing head, retained as \Longrightarrow. The final inclusion is an open curved sign without an extra lower bar, retained as \subset.',
  r'The pencil numerals are VI and II, each with a separate upper and lower transverse rule. The two groups are retained with \overline{\underline{\mathrm{VI}}} and \overline{\underline{\mathrm{II}}}.',
  r'The first formula label is (1), and the diagram label is (2). The argument later refers to (1). These ink readings were retained; no numerical or mathematical reconstruction was used to add symbols.'
 ],
 'check_events':[],
 'notation':[
  {'sign':'Ruled Roman references','latex':r'\overline{\underline{\mathrm{VI}}}; \overline{\underline{\mathrm{II}}}','evidence':'A rounded V followed by one upright, and a pair of uprights, each between separate transverse rules.','place':'Slanted upper-left pencil note'},
  {'sign':'Reduced-space suffix','latex':r'X_{\mathrm{red}}','evidence':'Small joined r-e-d below the X baseline; no distinct acute stroke.','place':'Underlined proposition'},
  {'sign':'Lowered zero suffix','latex':r'X_0','evidence':'Small closed low oval following ordinary crossed X.','place':'Reduction paragraph, displays and diagram'},
  {'sign':'Ideal letter','latex':r'\mathscr{N}','evidence':'Left rising loop, oblique transition and narrow tall right stroke with a small loop.','place':'Square-zero paragraph and repeated formula arguments'},
  {'sign':'Introduced cotangent-complex capital','latex':r'\unsure{K|\mathbb{K}}','evidence':'Two close dark stem traces merge in dense blue ink; independent second stroke versus retracing unresolved.','place':'After Soit enfin'},
  {'sign':'Sheaf functors','latex':r'\mathscr{H}om; \mathscr{E}xt^1','evidence':'Crossing loops in the H initial; rounded upper and lower curves in the E initial; raised short stroke for degree 1.','place':'Display (1) and diagram (2)'},
  {'sign':'Nested raised qualifiers','latex':r'H^{1^{\mathrm{alg}}}; H^{1^{\mathrm{an}}}; H^{0^{\mathrm{an}}}','evidence':'Small qualifier words are written above and right of the raised degree.','place':'Diagram (2)'},
  {'sign':'Arrow labels and final inclusion','latex':r'\alpha; \beta; \operatorname{Im}(\beta)\subset\operatorname{Im}(\alpha)','evidence':'Alpha has a small loop and right arm; beta has an upright and two curved parts; inclusion is an open curved stroke without a lower rule.','place':'Last arrows in diagram rows and final line'},
  {'sign':'Detached marginal pair','latex':point_graphic,'evidence':'Lower broad pointed form and upper-right taller lobed form; diagonal offset is preserved; punctuation status unresolved.','place':'Far right of upper row of diagram (2)'}
 ],
 'abbreviations':[
  {'form':'App.','expansion':'appendice'}, {'form':'SGA','expansion':'Séminaire de géométrie algébrique'}, {'form':'red','expansion':'réduit'}, {'form':'an','expansion':'analytique'}, {'form':'alg','expansion':'algébrique'}, {'form':'GAGA','expansion':'géométrie algébrique et géométrie analytique'}, {'form':'Im','expansion':'image'}, {'form':'Hom','expansion':'homomorphismes'}, {'form':'Ext','expansion':'extensions'}
 ],
 'slips':["The author writes singular Soit before two coordinated extension-group names; the text is not changed to Soient.","The author begins il s'obtient with lower-case i after a full stop; this is retained."],
 'completion':'Complete independent reading of scan 075: the whole-page image was viewed once for layout, half a once and then half b once line by line. Eight unique tight crops were each viewed once; no delivery was truncated. All text blocks, the slanted note, underlining, two cancellations, two displays, every diagram object, all nine diagram arrows and both labels, the detached marginal pair, and the archive number are covered. No OCR, external research, other-page or peer reading, delegation, or TeX compilation was used. Only structural source checks were run after writing.'
}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and report.json')
print('Decision rows:',len(decisions))
print('Differences from C:',sum(d['diff_c'] for d in decisions))
print('C doubts:',sum(d['c_doubt'] for d in decisions))
print('Unresolved decisions:',sum(d['unresolved'] for d in decisions))
