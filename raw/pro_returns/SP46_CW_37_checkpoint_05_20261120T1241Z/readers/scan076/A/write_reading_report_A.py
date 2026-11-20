from pathlib import Path
import json
base=Path('/workspace/scratch/006c0e32b2af/out/readers/scan076/A')
sourcebase=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans')
insertion=r'''\raisebox{0.2ex}{\parbox[b]{2.8em}{\figure{%
\begin{tikzpicture}[x=1mm,y=1mm,baseline=0pt]
\node[inner sep=0pt,anchor=south] at (3.2,3.6) {$\inserted{U'_i}$};
\draw[line width=0.35pt] (0,3.3)
 .. controls (-0.1,1.5) and (1.4,1.4) .. (2.2,1.1)
 .. controls (2.8,0.9) and (3.0,0.3) .. (3.4,0)
 .. controls (3.9,1.4) and (4.9,2.6) .. (6.1,2.8);
\end{tikzpicture}%
}}}'''
marks=r'''\margin{\vspace*{4.5em}\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\fill (0,0) ellipse[x radius=0.23,y radius=0.21];
\fill (0.62,0.92) ellipse[x radius=0.22,y radius=0.31,rotate=-36];
\end{tikzpicture}%
}}}'''
reading=r'''\scanpage{76}
\noindent Soit donc \(U_i\) un recouvrement affine de \(X_0\), et
\[
 e\in H^{0^{(\mathrm{alg})}}(X_0,\mathscr{E}xt^1(K,\mathscr{N}))
\]
représenté par des classes d'isomorphies (algébriques) d'extensions INSERTION de \(U_i\) par \(\mathscr{N}\mid U_i\), classes d'isomorphies qui se recollent :

\[
 \text{soit }\unsure{\eta|n|\gamma}_{ij}\text{ un isomorphisme}\qquad
 U'_j\mid U_i\cap U_j
 \xrightarrow{\sim}
 U'_{\unsure{i|j}}\mid U_i\cap U_j\ .
\]

L'obstruction à construire des \(\eta_{ij}\) \deleted{d}tels que \(\eta_{ij}\eta_{jk}=\eta_{ik}\) est donné par \(d_2\eta\) où \(d_2\) est une certaine flèche
\[
 d_2:H^0(X_0,\mathscr{E}xt^1(K,\mathscr{N}))\longrightarrow
 H^2(X_0,\mathscr{H}om(K,\mathscr{N}))
\]

La même construction marche dans le cas analytique, et on conclut par une nouvelle application de GAGA.

\uline{Rmq} 1 : itou pour les espaces algébriques, espaces rigides analytiques ; schémas formels

\deleted{\uline{\unsure{Rmq 2|Rmqs}}} :

\noindent\hfill Bien à toi\\
\null\hfill P. Deligne
MARKS
% archive sheet number: 75
'''.replace('INSERTION',insertion).replace('MARKS',marks)
(base/'reading.tex').write_text(reading)
manifest=json.loads((base/'crop_manifest_A076.json').read_text())
for x in manifest:
 x['requested_deliveries']=1
 x['actual_visual_views']=1
(base/'crop_manifest_A076.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

def decision(id,place,c,reading,diff,doubt,unresolved,alternatives,confidence,kind,shows,bbox,crop=''):
 return {'id':id,'place':place,'c_reading':c,'h_reading':None,'reading':reading,'diff_c':diff,'diff_h':False,'c_doubt':doubt,'unresolved':unresolved,'alternatives':alternatives,'confidence':confidence,'kind':kind,'scan_shows':shows,'crop':str(base/crop) if crop else '', 'bbox':bbox}
D=[]
D.append(decision('A076-01','Interlinear insertion after d’extensions',r'\(\inserted{U\'_i}\)'.replace("\\'","'"),insertion,True,False,False,[],'high','drawing or diagram','The raised U has one detached prime at upper right and a small i below it. A separate curved connector begins below-left of the label, bows downward to a low central point and rises to the right into the gap before de. C represents the inserted expression but not this connector.',[1284,177,1348,249]))
D.append(decision('A076-02','First transition symbol after soit',r'\unsure{\eta|n|\gamma}_{ij}',r'\unsure{\eta|n|\gamma}_{ij}',False,True,True,[r'\eta',r'n',r'\gamma'],'medium','misread symbol or index','A curved left entry rises into a small arch, comes down obliquely, then joins a second upward turn and longer right downstroke. Eta is preferred. The compressed joining strokes still allow cursive n or gamma; the crop does not securely remove either. The separate lowered i has a short foot and j has a long looped descender.',[596,377,642,435],'A076_01_transition.jpg'))
D.append(decision('A076-03','Source of the displayed isomorphism: U-prime subscript',r"U'_{\unsure{j|i}}",r"U'_j",True,True,False,[],'high','misread symbol or index','Below the U and detached prime, the suffix has a long downward stroke with a low loop and left-returning tail. It extends well below the neighboring short i. These visible strokes settle j. Heavy retracing does not isolate a separate earlier character.',[941,375,986,438],'A076_02_source_index.jpg'))
D.append(decision('A076-04','Target of the displayed isomorphism: U-prime subscript',r"U'_{\unsure{i|j}}",r"U'_{\unsure{i|j}}",False,True,True,['i','j'],'medium','misread symbol or index','The suffix has a short dark upright and a wide rightward foot, favoring i, but overlapping lower curves form a crowded closed patch. A j-shaped undercurve or retracing cannot be separated with confidence. No distinct earlier character is transcribed as deleted.',[1212,372,1257,430],'A076_03_target_index.jpg'))
D.append(decision('A076-05','Initial of tels in obstruction paragraph',r'\deleted{\unsure{d}}tels',r'\deleted{d}tels',True,True,False,[],'high','deletion state (struck given live or live given struck)','The live tall vertical initial carries a separate horizontal t bar. Beneath its lower part, a closed oval extends to the left of the stem and returns into it, preserving the bowl of an overwritten d. The later e, l and s are separately legible.',[946,460,990,500],'A076_04_tels.jpg'))
D.append(decision('A076-06','Est donné par',r'\unsure{donné|donnée}','donné',True,True,False,[],'high','misread word','After the tall d and rounded o, two low n arches lead to one terminal e loop. A separate rising acute accent lies above that final e; the final stroke merely exits upward and does not form a second e.',[1385,461,1476,500],'A076_05_donne.jpg'))
D.append(decision('A076-07','Number following underlined Rmq',r'\uline{Rmq} \unsure{1|s}',r'\uline{Rmq} 1',True,True,False,[],'high','misread symbol or index','After q there is one detached near-vertical short stroke, tapering at the bottom, without the two curves of an s. The underline ends before that stroke. Two separate points to its right form the colon.',[313,968,409,1020],'A076_06_remark_heading.jpg'))
D.append(decision('A076-08','First word of first remark',r'\unsure{itou}','itou',True,True,False,[],'high','misread word','A short i has its detached dot; the following tall t has a separated transverse bar. A small closed o loop joins a low two-stroke u with an upturned final exit.',[429,967,496,1008],'A076_07_itou.jpg'))
D.append(decision('A076-09','Full cancelled second remark heading',r'\deleted{\uline{\unsure{Rmq 2|Rmqs}}}',r'\deleted{\uline{\unsure{Rmq 2|Rmqs}}}',False,True,True,['Rmq 2','Rmqs'],'low','misread word','Several rising diagonal cancellation strokes cross the complete underlined heading. R retains its bowl and leg; the low humps and descending q remain traceable. The terminal curved stroke has an upper bend and lower rightward foot compatible with 2, but cancellation intersects its middle and still allows s. The colon to the right is outside the cancellation.',[311,1048,407,1094],'A076_08_cancelled_heading.jpg'))
D.append(decision('A076-10','Far-right blank area below signature',r'\margin{\unsure{:}}',marks,True,True,True,['Detached punctuation-like pair','Marks unrelated to the letter'],'low','drawing or diagram','Two small dark marks lie on an upward-right diagonal: a compact almost round lower-left point and an oblique upper-right oval. They are neither vertically aligned nor attached to the signature. Their shapes and relative positions are preserved; their textual function and origin remain unresolved.',[1401,1374,1418,1393],'A076_09_detached_marks.jpg'))

def inv(element,kind,position,first,hand='named other hand (P. Deligne)'):
 return {'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'}
I=[
inv('Opening sentence','text','Top, y65–111','Soit donc U_i un recouvrement affine de X_0, et'),
inv('First cohomology display','display','Upper centre, y114–189',r'e\in H^{0^{(\mathrm{alg})}}(X_0,\mathscr{E}xt^1(K,\mathscr{N}))'),
inv('Extensions and gluing paragraph','text','Two lines, y224–342',"représenté par des classes d'isomorphies"),
inv('Raised local-extension expression','insertion','Above d’extensions/de, x1290–1344, y180–219',r"U'_i"),
inv('Insertion connector','drawing','Below raised U-prime, x1287–1345, y216–247','Curved downward-pointing connector'),
inv('Displayed transition isomorphism','display','Across y373–437',r"soit \eta_{ij} un isomorphisme; U'_j|U_i\cap U_j\xrightarrow{\sim}U'_i|U_i\cap U_j"),
inv('Obstruction paragraph','text','Two lines, y460–582',"L'obstruction à construire des"),
inv('Overwritten d at start of tels','deletion','x949–971, y471–496','d beneath t'),
inv('Obstruction map','display','Centre, y651–709',r'd_2:H^0(X_0,\mathscr{E}xt^1(K,\mathscr{N}))\longrightarrow H^2(X_0,\mathscr{H}om(K,\mathscr{N}))'),
inv('Analytic case and conclusion','text','Two lines, y771–892','La même construction marche dans le cas analytique'),
inv('First remark','text','Across y968–1019','Rmq 1 : itou pour les espaces algébriques'),
inv('Cancelled second remark heading','deletion','Left, y1047–1095','Rmq 2 / Rmqs'),
inv('Uncancelled colon after deleted heading','text','x399–407, y1065–1087',':'),
inv('Closing','text','Centre, y1124–1161','Bien à toi'),
inv('Signature','text','Centre, y1213–1279','P. Deligne'),
inv('Unassigned diagonal dark pair','drawing','Far right below signature, x1401–1418, y1374–1393','Two separate small marks','unnamed hand / material origin unresolved'),
inv('Archive sheet number','text','Lower-left, x61–120, y1906–1973','75 (comment only)','unnamed other hand')
]
report={
'scan':76,'reader':'A',
'image_views':[str(sourcebase/x) for x in ['H37-01_37_scan076.jpg','H37-01_37_scan076_a.jpg','H37-01_37_scan076_b.jpg']],
'reading_path':str(base/'reading.tex'),
'crops':manifest,
'decisions':D,
'inventory':I,
'notes':'One wholly handwritten continuation and ending of a letter signed P. Deligne. It gives local extension classes and gluing isomorphisms, states an obstruction via d_2, then applies the same construction in the analytic setting and invokes GAGA. One live remark lists algebraic spaces, rigid analytic spaces and formal schemes; a second remark heading alone is crossed out. No title, date, salutation or author page number appears on this sheet; the lower-left 75 is recorded only as an archive number. No explicit author question or expression of doubt is visible. All uncertainty marks in reading.tex are editorial. H is description only and is unavailable for textual collation: every h_reading is null and every diff_h false. The source images were viewed once each, whole then half a then half b. Each of nine distinct remaining loci was cropped once, and each retained crop was visually delivered once. The graphic connector at the raised insertion was settled on half a without an additional crop.',
'math_reading_decisions':[
'The cover uses U_i with a short lowered i; X_0 has a rounded lowered zero. Raised U-prime in the insertion has one prime and lowered i. Restriction signs are tall single vertical bars.',
'The first plain cohomology H has an elevated 0, and the parenthesized alg stands at a further raised level. The same display has a script E in Ext, a raised 1, plain K and script N; all parentheses are retained.',
'The source transition suffix is j, decided from the long looped descender. The target favors i but remains i/j. The arrow points right and has one wavy stroke above its shaft. Intersection signs open downward and both restriction expressions read U_i cap U_j.',
'The transition symbol remains eta/n/gamma at its first occurrence; subsequent copies are written eta under the recurring-glyph convention. All visible cocycle suffixes were read separately as ij, jk and ik: j has a descending loop, k an oblique branch.',
'The page writes d_2 eta in the obstruction sentence. The ink is not replaced by d_2 e, despite the earlier class being called e. The d has a lowered 2 in all three occurrences.',
'The last display has plain H^0 on the left and H^2 on the right, script E in Ext^1, script H in Hom, and script N in both arguments. All arrows, capitals, exponents, subscripts and closing parentheses were independently checked from half a.'
],
'check_events':[
{'statement_id':'A076-cocycle','type':'local type/composition check','outcome':'Conditional on the preferred target i, eta_ij maps the j extension to the i extension and eta_jk maps the k extension to the j extension; their indicated composite has the same source and target as eta_ik. This is only a diagnostic consistency check, not a proof of the asserted obstruction formula; the crowded target index remains marked.'}
],
'notation':[
{'sign':'Recurring transition symbol','latex':r'\unsure{\eta|n|\gamma} at first occurrence; \eta thereafter','evidence':'Arched left entry and joined longer right downstroke; competing cursive constructions remain possible.','place':'First isomorphism, cocycle equation and d_2 eta'},
{'sign':'Primed local extensions and restrictions','latex':r"U'_j\mid U_i\cap U_j; U'_{\unsure{i|j}}\mid U_i\cap U_j",'evidence':'Detached upper primes; source suffix has long looped descender; target suffix has crowded retracing; tall vertical restriction bars.','place':'Displayed isomorphism'},
{'sign':'Raised algebraic qualifier','latex':r'H^{0^{(\mathrm{alg})}}','evidence':'Small oval zero above H and parenthesized alg on a higher line.','place':'First display'},
{'sign':'Sheaf-functor and coefficient alphabets','latex':r'\mathscr{E}xt^1; \mathscr{H}om; \mathscr{N}','evidence':'Rounded double-curve E; looped H; N has curved entry and returning terminal stroke. Cohomology H and K are plain.','place':'First and last displays'},
{'sign':'Obstruction differential','latex':r'd_2','evidence':'Looped upright d with detached low 2.','place':'Obstruction paragraph and final display'},
{'sign':'Detached diagonal pair','latex':marks,'evidence':'Almost round lower-left point and slanted upper-right oval, with no textual attachment.','place':'Below and to the right of the signature'}
],
'abbreviations':[{'form':'Rmq','expansion':'remarque'},{'form':'alg','expansion':'algébrique'},{'form':'P.','expansion':'Initial before Deligne; forename not supplied on the page'}],
'slips':['The live text reads est donné with only one final e, despite the preceding feminine noun L’obstruction; this is preserved.','The obstruction sentence uses d_2 eta although the earlier cohomology class is called e. This discrepancy is retained, without deciding that it is an error.'],
'completion':'Complete independent page coverage: all visible prose, three displays, the raised insertion and its connector, the overwritten initial, the entire readable crossed-out heading, closing, signature, detached mark pair and archive-number comment are represented. Nine explicit C doubts each have a decision record, resolved or retained. No external source, OCR, other reader, other-page image or TeX compilation was used.'
}
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Saved reading.tex and report.json; decisions:',len(D),'inventory:',len(I))
