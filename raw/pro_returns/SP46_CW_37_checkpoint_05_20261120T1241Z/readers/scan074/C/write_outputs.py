from pathlib import Path
import json
base=Path('/workspace/scratch/006c0e32b2af/out/readers/scan074/C')
curve=r'''\par\vspace*{0.43\textheight}
\noindent\hfill\parbox[c]{9mm}{\figure{\unsure{\handwritten{%
\begin{tikzpicture}[x=1mm,y=1mm]
\draw[line width=0.25pt] (0,5.35)
 .. controls (2.3,4.50) and (5.65,3.65) .. (7.20,2.20)
 .. controls (8.05,1.43) and (8.45,0.50) .. (8.00,0.15)
 .. controls (7.88,0.03) and (7.60,-0.06) .. (7.42,0.00);
\end{tikzpicture}%
}}}}\hspace*{0.025\linewidth}\par'''
reading=r'''\scanpage{74}

\begin{flushright}
Massy le 3.11.1970\\
\end{flushright}

\noindent Cher Ferrand,\\

J'aimerais savoir si je peux compter sur ton exposé SGA 6 XI dans un avenir assez rapproché (diso\unsure{n|r|u} d'ici fin décembre). Dans le cas contraire, je pense qu'il serait préfé\deleted{é}r\deleted{\unsure{r}}able que je publie SGA 6 sans l'exposé XI. Il serait quand même raisonnable, après le travail que tu t'es tapé, que tu en fasses au moins un article d'exposition, et j'aimerais savoir alors où tu penses le publier, pour que je puisse y référer dans l'introduction à SGA 6.

Bien cordialement\\

% Isolated curved mark in the lower-right blank area, far below the closing.
% Its visible shape is retained; pen mark versus incidental surface trace remains uncertain.
'''+curve+'\n% archive sheet number: 73\n'
(base/'reading.tex').write_text(reading)
c_curve=r'''\margin{\handwritten{\figure{\begin{tikzpicture}[x=0.5cm,y=0.5cm]
\draw[line width=0.25pt] (0,0.65) .. controls (0.4,0.46) and (1.12,0.24) .. (1.02,0.05) .. controls (1.00,0.01) and (0.96,0.00) .. (0.94,0.00);
\end{tikzpicture}}}}'''
report={
 'scan':74,'reader':'C',
 'image_views':[
 '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan074.jpg',
 '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan074_a.jpg',
 '/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan074_b.jpg'],
 'reading_path':str(base/'reading.tex'),
 'crops':json.loads((base/'crop_manifest.json').read_text()),
 'decisions':[
  {'id':'074C-01','place':'Body, second typed line, clipped right edge after diso',
   'c_reading':r'diso\unsure{l|n|u}',
   'h_reading':r'diso\supplied{ns}',
   'reading':r'diso\unsure{n|r|u}',
   'diff_c':True,'diff_h':True,'c_doubt':True,'unresolved':True,
   'alternatives':['Partial n','Partial r','Partial u'],
   'confidence':'low','kind':'misread word',
   'scan_shows':'After the complete d, dotted i, s and closed o, only a short upright with a top serif and basal foot survives at the clipping boundary. Its dark top is at the x-height of s/o, without a full ascender like the preceding d; this disfavors C’s preferred l. The right shoulder or bowl is missing, so n, r and u cannot be separated securely. No final s is visible. The new alternative r and changed preferred letter are substantive uncertainty changes, not macro changes.',
   'crop':str(base/'074C_01_clipped_disol.jpg'),'bbox':[1103,314,1194,346]},
  {'id':'074C-02','place':'Body, fourth typed line, underlying accented e at the live r position in préférable',
   'c_reading':r'préf é'.replace(' ', '')+r'\deleted{é}r',
   'h_reading':'préférable','reading':r'préf é'.replace(' ', '')+r'\deleted{é}r',
   'diff_c':False,'diff_h':True,'c_doubt':False,'unresolved':False,
   'alternatives':[],'confidence':'high','kind':'deletion state (struck given live or live given struck)',
   'scan_shows':'An oblique acute accent remains above this overprinted position. Below it a curved e bowl and cross-stroke remain on the right of a heavier stem and foot belonging to the live r. Both components are visible; H suppresses the underlying é.',
   'crop':str(base/'074C_02_preferable_overtypes.jpg'),'bbox':[515,392,535,419]},
  {'id':'074C-03','place':'Body, fourth typed line, uncertain underlying letter at the live a position in préférable',
   'c_reading':r'\deleted{\unsure{r}}a',
   'h_reading':'préférable','reading':r'\deleted{\unsure{r}}a',
   'diff_c':False,'diff_h':True,'c_doubt':True,'unresolved':True,
   'alternatives':['Underlying r; exact form partly obscured by the live a'],
   'confidence':'medium','kind':'deletion state (struck given live or live given struck)',
   'scan_shows':'At the left of the live a there is an extra squared top serif and stem/shoulder remnant. These favor an underlying r, but its right portion is merged into the live a. C’s explicit doubt is retained. H has only the final word and omits this overtyped component.',
   'crop':str(base/'074C_02_preferable_overtypes.jpg'),'bbox':[535,399,556,420]},
  {'id':'074C-04','place':'Body, fifth typed line, right-edge après',
   'c_reading':'après','h_reading':r'aprè\supplied{s}','reading':'après',
   'diff_c':False,'diff_h':True,'c_doubt':False,'unresolved':False,
   'alternatives':[],'confidence':'high','kind':'other',
   'scan_shows':'The final letter is clipped at the right edge, but dark upper and lower curved portions of an s remain immediately after the accented è. The surviving letter is legible in the top half. H labels the whole s as supplied; the reading records the recognizable visible s.',
   'crop':'','bbox':[1102,423,1194,455]},
  {'id':'074C-05','place':'Lower-right blank area, isolated curved mark far below the closing',
   'c_reading':c_curve,'h_reading':'','reading':curve,
   'diff_c':True,'diff_h':True,'c_doubt':False,'unresolved':True,
   'alternatives':['An unlabelled pen stroke','An incidental surface trace or adhering fibre'],
   'confidence':'medium','kind':'drawing or diagram',
   'scan_shows':'One thin dark trace slopes downward from left to right, steepens at the right, then turns inward to a short leftward hook. It has uneven dark patches and a pale bordering halo. Its shape is recoverable, but those features do not securely establish pen ink versus a surface trace. No letters or signature can be read. The unmarked graphic in C is given an explicit uncertainty here; C_context also raised the material doubt, although C.tex had no unsure macro. The graphic is placed in the lower-right blank area and H omits it.',
   'crop':str(base/'074C_03_bottom_curve.jpg'),'bbox':[1109,1505,1165,1544]}
 ],
 'inventory':[
  {'sheet_kind':'letter','hand':'typewriter','element':'Place and date','kind':'text','position':'Upper right, x690–1050 y138–170','first_words_or_objects':'Massy le 3.11.1970','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Salutation','kind':'text','position':'Upper left, x160–416 y213–243','first_words_or_objects':'Cher Ferrand,','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Body paragraph, nine typed lines','kind':'text','position':'Upper portion, x157–1194 y282–598','first_words_or_objects':"J'aimerais savoir si je peux compter sur ton",'transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Overtyped é at live r','kind':'deletion','position':'Body fourth line, x515–535 y392–419','first_words_or_objects':r'\deleted{é}r','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Uncertain overtyped r at live a','kind':'deletion','position':'Body fourth line, x535–556 y399–420','first_words_or_objects':r'\deleted{\unsure{r}}a','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Closing','kind':'text','position':'Below body, x240–579 y617–646','first_words_or_objects':'Bien cordialement','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'unnamed hand','element':'Unassigned curve; attribution to a pen remains uncertain','kind':'drawing','position':'Lower-right blank area, x1109–1165 y1505–1544','first_words_or_objects':'Descending curve with short inward terminal hook','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'unnamed hand','element':'Archive number, recorded only in a comment','kind':'text','position':'Lower left, x86–143 y1653–1702','first_words_or_objects':'73','transcribed':'yes'}
 ],
 'notes':"One typewritten letter page headed Massy le 3.11.1970 and addressed Cher Ferrand. The paragraph asks whether exposé SGA 6 XI can be expected by the end of December, considers publishing SGA 6 without it, and asks about a separate exposition article and a reference in the introduction. The physical right edge cuts the end after diso and part of the s in après. Two adjacent overprints occur in préférable. The closing is Bien cordialement; no signature or author’s own page number is readable. There is no title and no explicit author doubt mark. The lower-right curve has no decipherable text and remains materially uncertain. Archive sheet number 73 is recorded only as a comment. The pale long vertical feature below the closing and the sheet-edge creases are surface features, not identified as authored ink. H’s archival wrapper and descriptive note were not counted as manuscript omissions.",
 'math_reading_decisions':[
  'All three SGA 6 references and both XI references were inspected independently as ordinary typewritten capitals/numerals; no upper or lower rule or independent double-struck alphabet was seen.',
  'The page has no formula, mathematical display, or diagram. Reading the publication request did not involve a proof or computation.'
 ],
 'check_events':[],
 'notation':[
  {'sign':'Roman exposé number','latex':r'\mathrm{XI}','evidence':'One crossed X and one upright I in ordinary typewriter forms, without transverse overline or underline.','place':'After the first SGA 6 and after exposé in the publication-without-XI sentence'},
  {'sign':'Publication abbreviation','latex':'SGA 6','evidence':'Separate single typewriter outlines S, G and A followed by a 6; no independent doubling.','place':'Three occurrences in the paragraph'}
 ],
 'abbreviations':[{'form':'SGA','expansion':'Not expanded on this page.'}],
 'slips':['Two adjacent typewriter errors remain visible beneath the corrected r and a in préférable; the first underlying letter is é and the second is probably r. The transcription preserves both.'],
 'completion':'Complete independent reading of this one page. The whole image was viewed once for layout, then half a and half b once each in order. All typed words, punctuation, accents, reference numerals, the two overprints, closing, isolated curved mark and archive number were checked. Three tight crops, one for each remaining open locus, were created and each viewed once. All substantive differences from C/H, both explicit C.tex doubts, the C_context material-status target, and the new uncertainty choices are reported. No OCR, web research, other page, peer reading, or TeX compilation was used.'
}
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and report.json')
