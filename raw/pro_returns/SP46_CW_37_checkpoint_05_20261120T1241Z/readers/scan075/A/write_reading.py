from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/A')
packet=Path('/workspace/scratch/006c0e32b2af/packets/scan075')
meta=json.loads((packet/'meta.json').read_text())
graphic=r'''\margin{\vspace{1.5\baselineskip}\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm]
\fill (0,0) .. controls (-0.30,0.07) and (-0.28,0.37) .. (-0.08,0.47)
 .. controls (0.02,0.76) and (0.24,0.57) .. (0.28,0.44)
 .. controls (0.58,0.39) and (0.54,0.13) .. (0.27,0.10)
 .. controls (0.20,-0.12) and (0.04,-0.18) .. (0,0) -- cycle;
\fill (0.62,1.11) -- (0.60,1.46)
 .. controls (0.60,1.65) and (0.83,1.65) .. (0.85,1.82)
 .. controls (1.03,1.98) and (1.14,1.72) .. (1.26,1.65)
 .. controls (1.48,1.56) and (1.23,1.41) .. (1.07,1.43)
 -- (1.07,1.13) -- cycle;
\fill[gray!65] (0.47,-0.14) .. controls (0.50,-0.04) and (0.61,-0.19) .. (0.65,-0.36)
 .. controls (0.61,-0.54) and (0.44,-0.40) .. (0.47,-0.14) -- cycle;
\fill[gray!50] (0.92,-0.57) ellipse[x radius=0.09,y radius=0.12];
\end{tikzpicture}%
}}}'''
reading=(packet/'C.tex').read_text()
reading=reading.replace(r'\margin{\unsure{:}}','')
reading=reading.replace(r'\diagram{\footnotesize',graphic+'\n\n'+r'\diagram{\footnotesize',1)
(root/'reading.tex').write_text(reading)

def decision(id,place,c,reading,bbox,**kw):
 d=dict(id=id,place=place,c_reading=c,h_reading=None,reading=reading,diff_c=False,diff_h=False,c_doubt=False,unresolved=False,alternatives=[],confidence='high',kind='other',scan_shows='',crop='',bbox=bbox)
 d.update(kw)
 return d

decisions=[
 decision('A-075-01','Upper-left slanted pencil note, first word',r'\unsure{joindre}',r'\unsure{joindre}',[47,67,141,140],c_doubt=True,unresolved=True,confidence='low',kind='misread word',scan_shows='Long initial descending, loop-ended stroke; a rounded join follows, then a short crowded run, an ascender and terminal r/e-like joined strokes. The middle joins do not independently settle every letter. The crop was rotated 22 degrees clockwise. The preferred word remains joindre; no different complete word is securely supported.',crop='A01_pencil_verb.jpg'),
 decision('A-075-02','Soit enfin: introductory cotangent-complex letter',r'\unsure{K|\mathbb{K}}',r'\unsure{K|\mathbb{K}}',[1157,976,1182,1009],c_doubt=True,unresolved=True,alternatives=['K',r'\mathbb{K}'],confidence='medium',kind='misread symbol or index',scan_shows='The two diagonal arms determine K. The upper part of its thick left stem has adjacent dark traces that merge lower down; they do not determine retracing versus an independent double stroke. The plain K forms in the later parentheses are not used to erase this local uncertainty.',crop='A02_intro_K.jpg'),
 decision('A-075-03','After the underlined description of K',"il s'obtient","il s'obtient",[1094,1051,1258,1098],confidence='high',scan_shows='A distinct dot stands above the short first upright, and the following l has a tall closed loop. This resolves the temporary il/Il question in favour of C\'s lowercase il.',crop='A03_il_initial.jpg'),
 decision('A-075-04','Before lisse in the local embedding sentence',r'\unsure{schéma}',r'\unsure{schéma}',[949,1131,1059,1171],c_doubt=True,unresolved=True,confidence='medium',kind='misread word',scan_shows='s, c, tall looped h, accented e and the humps of m are readable. The terminal dark cluster has several superposed rounded strokes and a small rightward loop. It favours a reworked a but does not isolate a distinct readable underletter or settle the final form completely. No invented deleted undertext is supplied.',crop='A04_schema.jpg'),
 decision('A-075-05','Far right of the upper row of diagram (2)',r'\margin{\unsure{:}}',graphic,[1542,1362,1554,1377],diff_c=True,c_doubt=True,unresolved=True,alternatives=['A colon-like mark','Stray pen points or another nontextual mark'],confidence='medium',kind='drawing or diagram',scan_shows='Two separate dark lobed marks lie on a rising left-to-right diagonal, with the upper point to the right of the lower; the upper contour is roughly squarish and the lower is rounded/lobed. Fainter bluish traces continue below-right of the lower mark. A vertically aligned typographic colon suppresses this geometry. The shapes are reproduced with a doubt mark; punctuation and material status remain unassigned.',crop='A05_margin_points.jpg')
]

def inv(element,kind,position,words,hand='unnamed hand (blue ink)'):
 return dict(sheet_kind='letter',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes')

inventory=[
 inv('Slanted pencil annotation','margin note','upper-left, x47–231 y65–244',r'\unsure{joindre}; SGA 7; ruled VI; ?; App.; ruled II','unnamed other hand (pencil)'),
 inv('Place and date','text','upper-right, x783–1357 y73–120','Bures sur Yvette, le 21 octobre 1968'),
 inv('Salutation','text','x526–804 y214–272','Cher Grothendieck,'),
 inv('Opening paragraph','text','x297–1396 y338–475',"En fait, il n'est pas nécessaire"),
 inv('Underlined proposition','text','x295–1480 y499–635','proposition : Soit X un espace analytique complexe compact.'),
 inv('Square-zero reduction paragraph','text','x299–1538 y658–785','On se ramène à ... montrer que si X_0'),
 inv('Cancelled verb','deletion','within reduction paragraph, x684–793 y671–707',r'\deleted{supposer}'),
 inv('Implication','display','x369–1131 y808–861',r'(X_0\text{ est un schéma})\Longrightarrow(X\text{ est un schéma})'),
 inv('Extension groups and local cotangent complex','text','x299–1536 y878–1183',r'Soit E^{\mathrm{an}}(X_0,\mathscr{N}) et E^{\mathrm{alg}}(X_0,\mathscr{N})'),
 inv('Sheaf functors, labelled (1)','display','x204–1284 y1201–1256',r'(1)\quad\mathscr{H}om(K,\mathscr{N})\quad et\quad\mathscr{E}xt^{1}(K,\mathscr{N}) .'),
 inv('Diagram introduction','text','x424–730 y1284–1334','Soit le diagramme :'),
 inv('Algebraic/analytic comparison, labelled (2)','diagram','x194–1318 y1345–1535',r'(2); 0; H^{1^{\mathrm{alg}}}; E^{\mathrm{alg}}; H^0; 0; H^{1^{\mathrm{an}}}; E^{\mathrm{an}}; H^{0^{\mathrm{an}}}; six right arrows; three down arrows; labels \alpha and \beta'),
 inv('Detached marginal mark cluster','drawing','right of upper diagram row, x1542–1554 y1362–1377','two dark points with faint lower-right traces','unnamed hand or unidentified material'),
 inv('Final explanatory paragraph','text','x298–1479 y1558–1773',r'Vu les significations (locales) de (1), les lignes sont exactes ;'),
 inv('Cancelled comparison phrase','deletion','last line, x297–773 y1722–1770',r'\deleted{comparer les images de \alpha et \beta}'),
 inv('Archive sheet number','text','bottom-left, x56–112 y1920–1973','74 (comment only)','unnamed archival hand (pencil)')
]

report=dict(
 scan=75,
 reader='A',
 image_views=meta['images'],
 reading_path=str(root/'reading.tex'),
 crops=json.loads((root/'crop_manifest.json').read_text()),
 decisions=decisions,
 inventory=inventory,
 notes="One fully handwritten letter page on squared paper. The main letter is in blue ink; a different slanted pencil annotation stands at upper left. The supplied descriptive H attributes the letter to P. Deligne, but no signature occurs on this page and the inventory does not infer authorship from the handwriting. The date is Bures sur Yvette, le 21 octobre 1968; the salutation is Cher Grothendieck,. The only heading is underlined lowercase proposition. No manuscript page number or page count is written; archive sheet number 74 is retained only as a comment. The pencil note has a question mark after the ruled VI. Two textual cancellations are present: supposer and comparer les images de α et β. There are no witnessed insertion carets. H contains descriptive notes rather than a transcription, so every h_reading is null and every diff_h is false. The author claims the scheme criterion, exactness of both diagram rows, and GAGA isomorphisms, and then states the remaining image inclusion. Those claims were read, not independently proved. Whole-page image was viewed once for layout; half a and then half b were viewed once line by line; half b begins at whole-image y=920. Each of the five open loci received exactly one saved enlarged crop and exactly one actual visual view, delivered in batches of three and two; no requested image delivery was truncated.",
 math_reading_decisions=[
  r'The pencil groups read \overline{\underline{\mathrm{VI}}} and \overline{\underline{\mathrm{II}}}; both the upper and lower transverse rules are visible. The question mark is on the SGA 7 VI line.',
  r'The criterion has X_{\mathrm{red}}, with a small joined red suffix and no distinguishable acute accent. The reduction and later formulas have lowered round 0 suffixes: X_0.',
  r'The ideal letter is \mathscr{N}: its left rising loop and terminal loop differ from the crossed Xs. The same letter was checked separately in the prose, displayed functors and diagram arguments.',
  r'The extension-group initials are ordinary E, with an upright and horizontal arms. an and alg are raised abbreviations without abbreviation points. Singular Soit is what is written.',
  r'K is locally uncertain only at its introduction; the K letters in the parentheses have single stems and diagonal arms. The introductory uncertainty is retained explicitly.',
  r'The initials of \mathscr{H}om and \mathscr{E}xt are looped/script forms, whereas the cohomology initials H and extension-group initials E are ordinary capitals. The raised 1 on Ext is preserved at every occurrence.',
  r'Diagram (2) has top H^{1^{\mathrm{alg}}}, E^{\mathrm{alg}}, H^0 and bottom H^{1^{\mathrm{an}}}, E^{\mathrm{an}}, H^{0^{\mathrm{an}}}. The an/alg qualifiers beside the H degrees sit on a second rise. No alg qualifier is visible on upper-right H^0, and none is supplied.',
  r'The displayed reduction uses two shafts and a right head, hence \Longrightarrow. Diagram (2) has three right arrows in each row and exactly three downward arrows; the final right arrows are labelled \alpha above and \beta below. There is no extra terminal zero or arrow.',
  r'The final formula reads \operatorname{Im}(\beta)\subset\operatorname{Im}(\alpha): the open curved inclusion has no lower bar. The preceding comparison phrase is struck through as a whole, including both Greek letters.',
  'The repeated mathematical objects were used to detect possible missing qualifiers, but every retained letter, degree, label and direction was decided from the page. No proof or computation was performed.'
 ],
 check_events=[],
 notation=[
  dict(sign='Ruled pencil Roman numerals',latex=r'\overline{\underline{\mathrm{VI}}}; \overline{\underline{\mathrm{II}}}',evidence='V followed by I, and two Is; separate upper and lower transverse rules around each group.',place='Upper-left pencil note'),
  dict(sign='Reduced-space suffix and zero suffix',latex=r'X_{\mathrm{red}}; X_0',evidence='Joined small r-e-d without a distinct acute; other suffixes are small closed low ovals.',place='Proposition and subsequent text/displays'),
  dict(sign='Script ideal letter',latex=r'\mathscr{N}',evidence='Left rising curl and looped right stroke, distinct from the two crossing diagonals of X.',place='Square-zero paragraph and every formula'),
  dict(sign='Cotangent complex, introductory uncertainty',latex=r'\unsure{K|\mathbb{K}}',evidence='Two close dark upper stem traces merge downward; diagonal arms determine K but retracing/doubling is unresolved.',place='Soit enfin K'),
  dict(sign='Script sheaf-functor initials',latex=r'\mathscr{H}om; \mathscr{E}xt^1',evidence='Crossing looped H and rounded upper/lower E arcs; small ordinary letters follow.',place='Formula (1) and diagram (2)'),
  dict(sign='Cohomology degrees and qualifiers',latex=r'H^{1^{\mathrm{alg}}}; H^{1^{\mathrm{an}}}; H^0; H^{0^{\mathrm{an}}}',evidence='Upright 1 or round 0 on the first raised level; abbreviated qualifiers on a further rise, absent in upper-right H.',place='Diagram (2)'),
  dict(sign='Arrow labels and inclusion',latex=r'\alpha; \beta; \operatorname{Im}(\beta)\subset\operatorname{Im}(\alpha)',evidence='Small crossed/looped alpha and two-part beta; final open curved sign has no underline.',place='Diagram (2) and final line'),
  dict(sign='Detached marginal cluster',latex=graphic,evidence='Two dark irregular points on an upper-right/lower-left diagonal with small faint lower-right traces; punctuation status unresolved.',place='Right of upper diagram row')
 ],
 abbreviations=[
  dict(form='SGA',expansion='Séminaire de géométrie algébrique'),
  dict(form='App.',expansion='appendice'),
  dict(form='red',expansion='réduit'),
  dict(form='an',expansion='analytique'),
  dict(form='alg',expansion='algébrique'),
  dict(form='GAGA',expansion='géométrie algébrique et géométrie analytique'),
  dict(form='Im',expansion='image'),
  dict(form='Hom',expansion='homomorphismes'),
  dict(form='Ext',expansion='extensions')
 ],
 slips=[
  'The page uses singular Soit before the two extension groups; preserved without grammatical correction.',
  'The sentence after the period following dérivée begins with the dotted lowercase il; preserved.',
  'Idéal begins with a capital I in the middle of the reduction sentence; preserved.'
 ],
 completion='Full coverage of all text, accents, punctuation, underlines, labels, mathematical letters and suffixes, displayed expressions, diagram objects/arrows/labels, both cancellations, slanted pencil note, detached marginal marks and archive-number comment. No OCR, other-page image, external research, peer reading, delegation or TeX compilation was used. Residual ambiguities remain explicitly marked in the reading and report.'
)
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and report.json')
print('Decisions:',len(decisions),'C doubts:',sum(d['c_doubt'] for d in decisions),'C differences:',sum(d['diff_c'] for d in decisions),'H differences:',sum(d['diff_h'] for d in decisions))
