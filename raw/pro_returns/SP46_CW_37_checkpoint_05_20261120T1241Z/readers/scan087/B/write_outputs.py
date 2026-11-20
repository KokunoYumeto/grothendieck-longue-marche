from pathlib import Path
import json

out=Path('/workspace/scratch/006c0e32b2af/out/readers/scan087/B')
trace=r'''\makebox[0pt][l]{\hspace{-0.08em}\raisebox{2.15ex}[0pt][0pt]{\parbox[c]{1.4mm}{\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm,baseline=0pt]
\draw[gray!75,line width=0.28pt] (0,0) .. controls (0.20,-0.03) and (0.31,0.03) .. (0.39,0.20)
 .. controls (0.47,0.38) and (0.43,0.64) .. (0.55,0.77);
\end{tikzpicture}%
}}}}}'''
pair=r'''\margin{\vspace*{0.35em}\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\fill (-0.18,-0.06) .. controls (-0.22,0.03) and (-0.16,0.22) .. (-0.04,0.24)
 .. controls (0.07,0.25) and (0.20,0.04) .. (0.16,-0.08)
 .. controls (0.05,-0.17) and (-0.12,-0.16) .. (-0.18,-0.06) -- cycle;
\fill (0.52,0.79) ellipse[x radius=0.13,y radius=0.22,rotate=-31];
\end{tikzpicture}%
}}}'''
reading=r'''\scanpage{87}
\mspage{- 539 -}

\noindent\qquad 3.8. Quasi-homéomorphismes et images réciproques de faisceaux\dotfill

\noindent\qquad 3.9. Faisceaux d'espaces pseudo-discrets\dotfill

\noindent\quad \S\ 4. Espaces annelés\dotfill

\noindent\qquad 4.1. Espaces annelés , $A$-Modules , $A$-Algèbres\dotfill

\noindent\qquad 4.2. Image directe d'un $A$-Module\dotfill

\noindent\qquad 4.3. Image réciproque d'un $B$-Module\dotfill

\noindent\qquad 4.4. Relations entre images directes et images réciproques\dotfill

\noindent\qquad 4.5.Immersions ouvertes et morphismes représentables par des immersions ouvertes \dotfill

\noindent\quad \S\ 5. Faisceaux quasi-cohérents et faisceaux cohérents\dotfill

\noindent\qquad 5.1. Faisceaux quasi-cohérents\dotfill

\noindent\qquad 5.2. Faisceaux de type fini\dotfill

\noindent\qquad 5.3. Faisceaux cohérents\dotfill

\noindent\qquad 5.4. Faisceaux localement libres\dotfill

\noindent\qquad 5.5. Modules localement libres sur un espace localement annelé\dotfill

\noindent\qquad 5.6. Groupe de Picard\dotfill

\noindent\qquad 5.7. Morphismes plats d'espaces an'''+trace+r'''nelés\dotfill

\noindent\quad \S\ 6. Compléments d'algèbre commutative .

\noindent\qquad 6.1. Limites inductives d'anneaux\dotfill

\noindent\qquad 6.2. Identification du module $M_f$ à une limite \deleted{\unsure{project|projecti}} inductive\dotfill

\noindent\qquad 6.3. Propriétés de finitude\unsure{,|.}\dotfill

\noindent\qquad 6.4. Critères pour qu'un anneau soit noethérien\dotfill

\noindent\qquad 6.5. Anneaux normaux et ferm\deleted{t}e\deleted{e}ture intégrale\dotfill
'''+pair+r'''

\noindent\qquad 6.6. Compléments sur la platitude\dotfill

\noindent\qquad 6.7. Compléments sur\deleted{\unsure{l|1}} les modules projectifs\dotfill

\noindent\qquad 6.8. Existence d'extensions plates d'anneaux locaux\dotfill

\noindent\quad \deleted{\S\ 7\unsure{.|{}}}

\noindent\quad \S\ 7. Compléments d'algèbre topologique\dotfill

\noindent\qquad 7.1. Anneaux admissibles\dotfill

\noindent\qquad 7.2. Anneaux adiques et limites projectives\dotfill

\noindent\qquad 7.3. Anneaux préadiques noethériens\dotfill

\noindent\qquad 7.4. Modules quasi-finis sur les anneaux locaux\dotfill

\noindent\qquad \deleted{7\unsure{.|3|{}}} 7.5. Anneaux de séries formelles restreintes\dotfill

\noindent\qquad 7.6. Anneaux complets de fractions\dotfill

% archive sheet number: 86
'''
(out/'reading.tex').write_text(reading)
crops=json.loads((out/'crop_manifest.json').read_text())

def decision(id,place,c_reading,reading,diff_c,c_doubt,unresolved,alternatives,confidence,kind,shows,crop,bbox):
 return dict(id=id,place=place,c_reading=c_reading,h_reading=None,reading=reading,diff_c=diff_c,diff_h=False,c_doubt=c_doubt,unresolved=unresolved,alternatives=alternatives,confidence=confidence,kind=kind,scan_shows=shows,crop=str(out/'crops'/crop) if crop else '',bbox=bbox)

decisions=[
 decision('087-B-01','Top page number',r'\mspage{539}',r'\mspage{- 539 -}',True,False,False,[],'high','omission','The three numerals 5, 3 and 9 are flanked by separate thick horizontal hyphens, one on each side. The numeral spacing and repeated mechanical outlines support typewriting. The flanking marks are retained inside the page-number macro.','B087_01_page_number.jpg',[807,57,958,94]),
 decision('087-B-02','5.7, above the junction of the first and second n in annelés','',trace,True,False,True,['unassigned added ink trace','incidental dark surface trace'],'medium','drawing or diagram','A detached short gray stroke has an upright/slanted upper segment and a small lower-left hook or foot. It lies above the n area, separate from the actual acute accent over é. No paper-coloured interruption or scratch channel establishes surface damage. Shape is retained without assigning punctuation or authorship.','B087_02_anneles_trace.jpg',[1002,1107,1017,1121]),
 decision('087-B-03','6.2, cancelled word after limite',r'\deleted{\unsure{project|projecti}}',r'\deleted{\unsure{project|projecti}}',False,True,True,['project','projecti'],'low','other','Repeated typed X forms cross a p with a descender, r shoulder, rounded o, descending j, e loop and later c/t-like contours. The final X-covered position does not securely distinguish the shorter abandoned string project from projecti. No unprinted completion is supplied.','B087_03_project_cancelled.jpg',[1249,1303,1420,1341]),
 decision('087-B-04','6.3, mark immediately after finitude',r'finitude\dotfill',r'finitude\unsure{,|.}\dotfill',True,False,True,[',','.'],'medium','misread symbol or index','The first low mark after the e is solid and angular, with a downward member; the following leader points have rounder, partly hollow impressions. The downward member favours a comma, but an irregular period remains possible. This is a new explicit punctuation uncertainty, not a silent change to the leader convention.','B087_04_finitude_punctuation.jpg',[868,1413,890,1435]),
 decision('087-B-05','Right margin, just below the leaders of 6.5','',pair,True,False,True,['unassigned added ink points','incidental dark surface marks'],'high','drawing or diagram','Two small solid dark points lie on a rising left-to-right diagonal: a compact triangular/lobed lower-left point and an oblique oval upper-right point. They are separated from the larger round leader dots and do not form a paper-coloured channel. Their visible shape is secure; function and material origin remain uncertain.','B087_06_margin_points.jpg',[1547,1530,1568,1552]),
 decision('087-B-06','6.7, cancelled glyph attached to sur',r'\deleted{\unsure{l|1}}',r'\deleted{\unsure{l|1}}',False,True,True,['l','1'],'medium','other','The underlying glyph has a leftward top serif, long upright and broad foot, closely resembling the following l of les; an oblique slash crosses it. The surviving typewriter outline by itself does not decisively distinguish l from 1.','B087_07_sur_cancelled.jpg',[722,1598,752,1638]),
 decision('087-B-07','Cancelled section start above the live section 7 heading',r'\deleted{\S\ \unsure{7.}}',r'\deleted{\S\ 7\unsure{.|{}}}',True,True,True,['7.','7 without a separately recoverable point'],'medium','other','Beneath the row of typed Xs, the opposed section-sign curls remain at the left. A capped descending 7-shaped stroke survives farther right, including its low descending end. The low thickening at the final X foot may be a period or cancellation ink. The numeral doubt is removed; the point doubt is retained with an explicit no-point alternative.','B087_08_section_stub.jpg',[274,1672,361,1707]),
 decision('087-B-08','Cancelled stub before the live 7.5',r'\deleted{7\unsure{.}}',r'\deleted{7\unsure{.|3|{}}}',True,True,True,['.','3','no separately recoverable following character'],'low','other','A 7 is visible at the left under cancellation. At the following X, a low trace could be a period; a small curved upper shoulder and crowded lower contour also permit an obscured 3, while attribution to the X impressions alone remains possible. The added 3 and empty alternatives are differences in recorded reading, not macro-only changes.','B087_09_entry_stub.jpg',[314,1975,361,2007]),
]

inventory=[]
def inv(element,kind,position,words,hand='typewriter'):
 inventory.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inv('Page number','text','Top centre','- 539 -')
entries_a=[
 ('3.8','upper body, first entry','Quasi-homéomorphismes et images réciproques de faisceaux'),
 ('3.9','below 3.8','Faisceaux d\'espaces pseudo-discrets'),
 ('Section 4 heading','upper body','§ 4. Espaces annelés'),
 ('4.1','below section 4 heading','Espaces annelés , A-Modules , A-Algèbres'),
 ('4.2','below 4.1','Image directe d\'un A-Module'),
 ('4.3','below 4.2','Image réciproque d\'un B-Module'),
 ('4.4','below 4.3, two source lines','Relations entre images directes et images réciproques'),
 ('4.5','below 4.4, two source lines','Immersions ouvertes et morphismes représentables par des immersions ouvertes'),
 ('Section 5 heading','upper-middle body','§ 5. Faisceaux quasi-cohérents et faisceaux cohérents'),
 ('5.1','below section 5 heading','Faisceaux quasi-cohérents'),
 ('5.2','below 5.1','Faisceaux de type fini'),
 ('5.3','below 5.2','Faisceaux cohérents'),
 ('5.4','below 5.3','Faisceaux localement libres'),
 ('5.5','below 5.4, two source lines','Modules localement libres sur un espace localement annelé'),
 ('5.6','near horizontal fold','Groupe de Picard'),
 ('5.7','below 5.6','Morphismes plats d\'espaces annelés'),
]
for e,p,w in entries_a:inv(e,'text',p,w)
inv('Detached short hook','drawing','Above annelés in 5.7','Short slanted upright and lower-left foot','unnamed hand')
inv('Section 6 heading','text','Middle body','§ 6. Compléments d\'algèbre commutative .')
inv('6.1','text','Below section 6 heading','Limites inductives d\'anneaux')
inv('6.2','text','Below 6.1, two source lines','Identification du module M_f à une limite … inductive')
inv('Cancelled word in 6.2','deletion','End of first source line of 6.2','project / projecti, overtyped with Xs')
inv('6.3','text','Below 6.2','Propriétés de finitude, / .')
inv('6.4','text','Below 6.3','Critères pour qu\'un anneau soit noethérien')
inv('6.5','text','Below 6.4','Anneaux normaux et fermeture intégrale')
inv('First overtyped letter in fermeture','deletion','6.5, after ferm','t under live e')
inv('Second overtyped letter in fermeture','deletion','6.5, after corrected e','e under live t')
inv('Detached point pair','drawing','Right blank margin, just below 6.5 leaders','Lower-left triangular point and upper-right slanted oval','unnamed hand')
inv('6.6','text','Below 6.5','Compléments sur la platitude')
inv('6.7','text','Below 6.6','Compléments sur … les modules projectifs')
inv('Cancelled extra glyph in 6.7','deletion','Between sur and les','l / 1 crossed by an oblique slash')
inv('6.8','text','Below 6.7','Existence d\'extensions plates d\'anneaux locaux')
inv('Cancelled section start','deletion','Between 6.8 and live section 7 heading','§ 7 with uncertain final point, overtyped with Xs')
inv('Section 7 heading','text','Lower body','§ 7. Compléments d\'algèbre topologique')
inv('7.1','text','Below section 7 heading','Anneaux admissibles')
inv('7.2','text','Below 7.1','Anneaux adiques et limites projectives')
inv('7.3','text','Below 7.2','Anneaux préadiques noethériens')
inv('7.4','text','Below 7.3','Modules quasi-finis sur les anneaux locaux')
inv('Cancelled entry start','deletion','Immediately left of the live 7.5','7 with uncertain following period / 3 / no recoverable character')
inv('7.5','text','Below 7.4','Anneaux de séries formelles restreintes')
inv('7.6','text','Last body entry','Anneaux complets de fractions')
inv('Archive number','text','Lower-left corner, recorded only in a TeX comment','86','unnamed hand')

report=dict(
 scan=87,reader='B',
 image_views=[f'/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan087{s}.jpg' for s in ['', '_a', '_b']],
 reading_path=str(out/'reading.tex'),crops=crops,decisions=decisions,inventory=inventory,
 notes='One typescript contents page, numbered - 539 - at top; archive sheet number 86 is recorded only as a comment. No date or separate title occurs. The page contains the end of section 3 (3.8–3.9), section 4 Espaces annelés (4.1–4.5), section 5 Faisceaux quasi-cohérents et faisceaux cohérents (5.1–5.7), section 6 Compléments d’algèbre commutative (6.1–6.8), and section 7 Compléments d’algèbre topologique (7.1–7.6): 28 live numbered entries and four live section headings. The author/typist cancels an incomplete word, an extra glyph, a section start and an entry start, and corrects two transposed letters in fermeture. There are no explicit authorial question marks or verbal doubts. Reader uncertainties are marked in place. H provides a description only, so all h_reading values are null and diff_h values are false; its absence of a transcription is not collated as omissions. The two detached graphic traces have uncertain material origin and are preserved by shape; they are not silently assigned punctuation. The broad pale horizontal fold and low paper texture are not added ink. Source images and all nine retained crops were each actually viewed once, in the prescribed order; processing and line-by-line coverage are documented in processing.md.',
 math_reading_decisions=[
  'Entry 6.2: M is an ordinary typewritten capital with the same mechanical outline family as other typed M forms; f is visibly lowered. Read $M_f$, without changing its alphabet or turning the lowered f into a prime.',
  'Entries 4.1, 4.2 and 4.3: each A and B was inspected separately in the half. A has a single pair of diagonal stems and crossbar; B has its single upright and two bowls. No independent doubled alphabet is visible. Retain ordinary A-Modules, A-Algèbres, A-Module and B-Module.',
  'Unmarked C-context target 6.5: the retained single crop confirms a high t stem/crossbar underneath the round live e in the first corrected position, followed by a residual e bowl under the live tall t. Retain ferm\\deleted{t}e\\deleted{e}ture. This is a palaeographic confirmation, not a mathematical proof check.',
  'Section signs 4, 5, 6 and 7 each show opposed curls. All live decimal entry numbers and their low points were read separately; 4.5.Immersions has no intervening space after the number. Section 6 heading has a terminal period and no leaders; the other live headings and all live entries have leaders.'
 ],
 check_events=[],
 notation=[
  dict(sign='Ordinary mathematical capitals',latex='A; B; M',evidence='Single typewriter outlines, with no distinct independent doubled stem; each occurrence inspected.',place='4.1–4.3 and 6.2'),
  dict(sign='Lowered module index',latex='M_f',evidence='Small f with upper hook and crossbar sits below the M baseline.',place='6.2'),
  dict(sign='Section and decimal numbering',latex=r'\S\ 4.; \S\ 5.; \S\ 6.; \S\ 7.; 3.8.; 7.6.',evidence='Opposed section-sign curves, individually read numerals, and low separating/terminal points.',place='Headings and numbered entries'),
  dict(sign='Contents leaders',latex=r'\dotfill',evidence='Repeated low rounded mechanical point impressions, mostly with lighter centres.',place='All live entries and headings except the section 6 heading'),
  dict(sign='Detached short hooked trace',latex=trace,evidence='Short gray upper slant or upright with lower-left foot, separate from text and actual é accent.',place='Above annelés in 5.7'),
  dict(sign='Uncertain punctuation',latex=r'\unsure{,|.}',evidence='Solid angular low impression with a downward member, followed by rounder hollow leader points.',place='After finitude in 6.3'),
  dict(sign='Detached point pair',latex=pair,evidence='Small solid lower-left triangular point and upper-right oblique oval.',place='Right blank margin beside 6.5'),
  dict(sign='Cancelled extra glyph',latex=r'\deleted{\unsure{l|1}}',evidence='Top serif, tall upright and broad foot crossed by an oblique stroke.',place='6.7 after sur'),
  dict(sign='Cancelled section-start punctuation',latex=r'\deleted{\S\ 7\unsure{.|{}}}',evidence='Section-sign loops and descending 7 survive the Xs; a final low thickening remains ambiguous.',place='Above live section 7 heading'),
  dict(sign='Cancelled entry-start suffix',latex=r'\deleted{7\unsure{.|3|{}}}',evidence='7 survives; following low trace and curved upper residual are obscured by an X.',place='Before live 7.5')
 ],
 abbreviations=[],
 slips=[
  '6.2 contains a cancelled abandoned project/projecti before live inductive; no longer adjective is completed from context.',
  '6.5 exchanges e and t by overtyping: the original t then e remain recorded immediately before the live e then t.',
  '6.7 has an extra cancelled l/1 attached to sur.',
  'A cancelled section start precedes the live section 7 heading, and a cancelled entry start precedes live 7.5; both remain in order.',
  'The possibly comma-shaped first mark after finitude is retained as a punctuation uncertainty rather than regularized into the leaders.'
 ],
 completion='Complete independent reading of scan 087: every live entry, heading, pagination mark, visible correction/cancellation, leader series and detached graphic has been covered. All four explicit C doubts have separate decisions; every substantive difference from C and every new uncertainty has a whole-image bbox. H is description-only. No OCR, external research, other reader/page consultation, delegation or TeX compilation occurred. Only source/LaTeX balance and JSON/schema checks are performed after writing.'
)
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and report.json:',len(decisions),'decisions,',len(inventory),'inventory rows,',len(crops),'crops.')
