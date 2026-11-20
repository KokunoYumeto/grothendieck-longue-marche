from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan086/A')
source_root=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans')
point=r'''\makebox[0pt][l]{\hspace{0.08em}\raisebox{-0.32ex}[0pt][0pt]{\parbox[c]{0.6mm}{\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm,baseline=0pt]
\fill[gray!75] (0,0) ellipse[x radius=0.16,y radius=0.21,rotate=-18];
\end{tikzpicture}%
}}}}}'''
pair=r'''\makebox[0pt][r]{\raisebox{1.15ex}[0pt][0pt]{\parbox[c]{1.6mm}{\figure{\unsure{%
\begin{tikzpicture}[x=1mm,y=1mm,baseline=0pt]
\fill (0,0) .. controls (-0.17,0.01) and (-0.19,0.17) .. (-0.10,0.28)
 .. controls (-0.01,0.40) and (0.11,0.33) .. (0.18,0.17)
 .. controls (0.24,0.06) and (0.15,-0.03) .. (0,0) -- cycle;
\fill (0.51,0.85) ellipse[x radius=0.17,y radius=0.24,rotate=-25];
\end{tikzpicture}%
}}}}\hspace{3.5em}}'''
reading=r'''\scanpage{86}
\mspage{- 541 -}

\noindent\qquad 3.8. Morphismes universellement ouverts , universellement fermés , universellement bicontinus\dotfill

\noindent\qquad 3.9. Morphismes générisants\dotfill

\noindent\qquad 3.10. Morphismes submersifs et universellement submersifs

\noindent\quad \S\ 4. Sous-schémas et morphismes d'immersion .'''+point+r''' Schémas réduits\dotfill

\noindent\qquad 4.1. Sous-schémas\dotfill

\noindent\qquad 4.2. Morphismes d'immersion\dotfill

\noindent\qquad 4.3. Image réciproque d'un sous-schéma\dotfill

\noindent\qquad 4.4. Immersions locales et isomorphismes locaux\dotfill

\noindent\qquad 4.5. Schémas réduits\dotfill

\noindent\qquad 4.6. Existence d'un sous-schéma d'espace sous-jacent donné\dotfill

\noindent\quad \S\ 5. Morphismes séparés . Critères valuatifs\dotfill

\noindent\qquad 5.1. Diagonale d'un $S$-schéma\dotfill

\noindent\qquad 5.2. Morphismes et schémas séparés\dotfill

\noindent\qquad 5.3. Critères \deleted{\unsure{a|e}}de séparation\dotfill

\noindent\qquad 5.4. Morphismes schématiquement dominants et sous-schémas schématiquement denses\dotfill

\noindent\qquad 5.5. Critères valuati\deleted{\unsure{s|b}}fs\dotfill

\noindent\quad \S\ 6. Conditions de finitude relatives\dotfill

\noindent\qquad 6.1. Morphismes quasi-compacts et morphismes quasi-séparés\dotfill

\noindent\qquad 6.2. Morphismes localement de type fini et morphismes localement de présentation finie\dotfill

\noindent\qquad 6.3. Morphismes de type fini et morphismes de présentation finie\dotfill'''+pair+r'''

\noindent\qquad 6.4. Schémas de \deleted{d}Jacobson et anneaux de \deleted{j}Jacobson\dotfill

\noindent\qquad 6.5. Schémas algébriques et localement algébriques\dotfill

\noindent\qquad 6.6. Détermi\deleted{j}nation locale d'un morphisme\dotfill

\noindent\qquad 6.7. Image directe d'un faisceau quasi-cohérent\dotfill

\noindent\qquad 6.8. Prolongement de sections de faisceaux quasi-cohérents

\noindent\qquad 6.9. Prolongement des faisceaux quasi-cohérents\dotfill

\noindent\qquad 6.10.Image schémat\deleted{\unsure{l|t|j}}ique d'un schéma\unsure{,|.} Adhérence schématique d'un sous-schéma\dotfill

\noindent\qquad 6.11.Morphismes quasi-finis\dotfill

% archive sheet number: 85
'''
(root/'reading.tex').write_text(reading)

# Every decision is tied to the whole-image coordinate system, even if settled in a half.
def dec(id,place,c,read,diff,doubt,unresolved,alts,conf,kind,shows,bbox,crop=''):
    return dict(id=id,place=place,c_reading=c,h_reading=None,reading=read,diff_c=diff,diff_h=False,c_doubt=doubt,unresolved=unresolved,alternatives=alts,confidence=conf,kind=kind,scan_shows=shows,crop=str(root/crop) if crop else '',bbox=bbox)
decisions=[
 dec('A086-01','Top-centre typed pagination',r'\mspage{541}',r'\mspage{- 541 -}',True,False,False,[], 'high','omission','One short horizontal dash precedes the separate digits 5, 4, 1, and a second horizontal dash follows them. The numeral is unchanged; the flanking punctuation is retained.',[803,53,956,90]),
 dec('A086-02','§4 heading: detached lower mark immediately right of the full stop',r'\unsure{\textsubscript{.}}',point,True,True,True,['small displaced impression','incidental ink point','surface speck'], 'low','drawing or diagram','A compact dark oblique oval lies below and to the right of the larger ring-shaped typed period. It is smaller than the period and has no matching typed baseline. The reading preserves its observed oval shape and lower-right placement without assigning it punctuation status; this is a shape/placement change from the generic subscript period.',[1195,339,1225,365],'A086_01_section4_point.jpg'),
 dec('A086-03','Between the leader rows of §4 and 4.1',None,'',False,False,False,['paper crease or scratch'], 'high','other','A narrow white central streak separates two pale gray edges and cuts through a typed leader point; the uneven gray flanks continue above and below that point. This is surface disruption rather than an independent ink stroke, so no textual or graphic element is added.',[803,405,824,484],'A086_07_vertical_trace.jpg'),
 dec('A086-04','5.3: overwritten letter before live de',r'\deleted{\unsure{a|e}}de',r'\deleted{\unsure{a|e}}de',False,True,True,['a','e'], 'low','misread word','Live d has a tall right ascender and its own lower bowl. Additional rounded lower and middle traces occupy the same character position, but the right side of the older body is covered. They still permit a or e. No separate old accent is established.',[618,974,660,1012],'A086_02_de_underprint.jpg'),
 dec('A086-05','5.5: older character under f in valuatifs',r'valuati\deleted{\unsure{s|b}}fs',r'valuati\deleted{\unsure{s|b}}fs',False,True,True,['s','b'], 'low','misread word','The live f has a tall hooked top, stem and crossbar. A rounded older lower loop remains to its right, while the upper distinguishing contour merges with the live f. Both s and b remain possible.',[756,1128,803,1164],'A086_03_valuatifs_underprint.jpg'),
 dec('A086-06','Right blank area above the 6.3 leader row',None,pair,True,False,True,['unassigned ink points','incidental surface marks','punctuation-like pair of unknown function'], 'medium','drawing or diagram','Two separate small dark forms lie on an ascending left-to-right diagonal above the leaders: a lower compact slightly angular point and an upper narrower oblique oval. Neither joins the text or the leaders. Their shape is preserved, while authorship and function remain undetermined.',[1398,1505,1419,1527],'A086_06_detached_pair.jpg'),
 dec('A086-07','6.10: older character under i in schématique',r'schémat\deleted{\unsure{l|t}}ique',r'schémat\deleted{\unsure{l|t|j}}ique',True,True,True,['l','t','j'], 'low','misread word','The live i occupies an overprinted position with merged upper head/point traces and a broad lower serif. A separate short dark foot survives below the ordinary baseline, near the level of the following q descender. The older upright still permits l or t with displacement; the low foot and upper point also allow j. Adding j changes the recorded alternatives while retaining the first candidate and the uncertainty.',[693,1865,722,1909],'A086_04_schematique_underprint.jpg'),
 dec('A086-08','6.10: punctuation after schéma',r'\unsure{,|.}',r'\unsure{,|.}',False,True,True,[',','.'], 'low','misread symbol or index','The small mark has an angular upper body and a short low leftward/downward extension. Its lower contour is not a complete ring, favouring a comma, but the broken impression does not rule out a degraded period. The following capital is not used to resolve the ink.',[1028,1882,1048,1903],'A086_05_schema_punctuation.jpg')
]

inventory=[]
def item(element,kind,position,first,hand='typewriter'):
    inventory.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
item('Typed pagination','text','Top centre, y54–87','- 541 -')
entries=[
('3.8','y104–189','Morphismes universellement ouverts , universellement fermés , universellement bicontinus'),
('3.9','y205–241','Morphismes générisants'),
('3.10','y253–291','Morphismes submersifs et universellement submersifs'),
('§4','y319–405',"Sous-schémas et morphismes d'immersion . Schémas réduits"),
('4.1','y438–474','Sous-schémas'),
('4.2','y488–525',"Morphismes d'immersion"),
('4.3','y537–576',"Image réciproque d'un sous-schéma"),
('4.4','y588–626','Immersions locales et isomorphismes locaux'),
('4.5','y638–676','Schémas réduits'),
('4.6','y689–776',"Existence d'un sous-schéma d'espace sous-jacent donné"),
('§5','y810–848','Morphismes séparés . Critères valuatifs'),
('5.1','y876–913',"Diagonale d'un S-schéma"),
('5.2','y927–964','Morphismes et schémas séparés'),
('5.3','y976–1013','Critères de séparation'),
('5.4','y1027–1112','Morphismes schématiquement dominants et sous-schémas schématiquement denses'),
('5.5','y1127–1165','Critères valuatifs'),
('§6','y1194–1233','Conditions de finitude relatives'),
('6.1','y1262–1348','Morphismes quasi-compacts et morphismes quasi-séparés'),
('6.2','y1362–1447','Morphismes localement de type fini et morphismes localement de présentation finie'),
('6.3','y1463–1548','Morphismes de type fini et morphismes de présentation finie'),
('6.4','y1562–1604','Schémas de Jacobson et anneaux de Jacobson'),
('6.5','y1614–1653','Schémas algébriques et localement algébriques'),
('6.6','y1665–1704',"Détermination locale d'un morphisme"),
('6.7','y1715–1754',"Image directe d'un faisceau quasi-cohérent"),
('6.8','y1765–1804','Prolongement de sections de faisceaux quasi-cohérents'),
('6.9','y1816–1854','Prolongement des faisceaux quasi-cohérents'),
('6.10','y1865–1951',"Image schématique d'un schéma, Adhérence schématique d'un sous-schéma"),
('6.11','y1967–2005','Morphismes quasi-finis')]
for label,pos,first in entries:
    item(('Section heading ' if label.startswith('§') else 'Contents entry ')+label,'text',pos,first)
    if label=='§4':
        item('Detached lower point','drawing','Right of the period in §4, x1216 y356','Small oblique oval; function and material origin uncertain','unnamed hand')
    if label=='5.3':
        item('Overtyped letter in de','deletion','5.3, x618–646 y974–1012','a/e under d')
    if label=='5.5':
        item('Overtyped letter in valuatifs','deletion','5.5, x763–789 y1128–1164','s/b under f')
    if label=='6.3':
        item('Detached diagonal point pair','drawing','Above the right-hand 6.3 leaders, x1398–1419 y1505–1527','Lower compact point and upper oblique oval','unnamed hand')
    if label=='6.4':
        item('First corrected Jacobson initial','deletion','6.4, x657–687 y1562–1599','d under J')
        item('Second corrected Jacobson initial','deletion','6.4, x1125–1155 y1558–1606','j under J')
    if label=='6.6':
        item('Corrected letter in Détermination','deletion','6.6, x578–602 y1665–1704','j under n')
    if label=='6.10':
        item('Corrected letter in schématique','deletion','6.10, x693–722 y1865–1909','l/t/j under i')
item('Archive sheet number','text','Lower-left corner, x43–98 y2060–2118','85, recorded only in a comment','unnamed hand')

manifest=json.loads((root/'crop_manifest.json').read_text())
for r in manifest:
    r['visual_views']=1
    r['delivery_requests']=1
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
report=dict(
 scan=86,reader='A',
 image_views=[str(source_root/f'B37-04_37_scan086{suffix}.jpg') for suffix in ('','_a','_b')],
 reading_path=str(root/'reading.tex'),
 crops=[{k:r[k] for k in ('file','bbox','rotation','reason')} for r in manifest],
 decisions=decisions,
 inventory=inventory,
 notes='One typescript table-of-contents continuation, with typed page line “- 541 -” and pencilled archive number 85. It contains entries 3.8–3.10, the §4 heading and six entries, the §5 heading and five entries, and the §6 heading and eleven entries: 28 text blocks besides pagination and archival numbering. No date or overall document title appears, and no explicit authorial doubt or question mark is present. The visible headings concern immersions and reduced schemes, separated morphisms and valuative criteria, and relative finiteness conditions. Six overtyped character positions are preserved as deletions followed by their live replacements. H supplies only description, so it is unavailable for textual collation throughout. Editorial uncertainty remains at all five explicit C-doubt loci; the older character in schématique gains j as an additional possibility. Two tiny unassigned graphic loci are reproduced without claiming a material origin. The vertical interruption among the upper leaders is identified as a crease/scratch and is not transcribed. Source-image and crop processing/view documentation is retained in processing.md, crop_manifest.json and make_crops.py. No OCR, external research, other page/reader inspection or TeX compilation was used.',
 math_reading_decisions=[
  'C-context 5.3: the live de is independently confirmed; d has a high ascender and low bowl, while the overprinted a/e remains uncertain and is separately reported.',
  'C-context 5.5: live valuatifs is independently confirmed; f has its hooked upper head, tall stem and transverse stroke, while the older s/b remains uncertain and is separately reported.',
  'C-context 6.4: the first ordinary typed J has a top cap and low left hook over a smaller d bowl/right ascender; the second ordinary typed J covers a dotted lower-case j with a surviving low descender. Both C underprints d and j are confirmed in half b without reopening the loci.',
  'C-context 6.6: the live n has two uprights joined by an arch; the older dot and downward hook identify j beneath it in Détermination. C is confirmed from half b.',
  'C-context 6.10: the live word schématique and replacement i are confirmed; the older l/t remains unresolved and the low surviving foot also permits j. The alternatives are recorded in decision A086-07.',
  'The capital S in 5.1 has one ordinary curved typed outline, with no independent doubled stroke; $S$ is retained. There are no formulas, mathematical displays, arrows or indices on this contents page.',
  'Every section sign has the opposed curved loops, and the numbered labels and decimal points were checked independently. The leader series are present except after 3.10 and 6.8; those two entries end in text without leaders.',
  'Typed pagination reads 541 with a dash on either side, and the separate handwritten archive numeral reads 85.'
 ],
 check_events=[],
 notation=[
  dict(sign='Section signs',latex=r'\S\ 4.; \S\ 5.; \S\ 6.',evidence='Two opposed loops form each section sign; the following digits and separate low points are legible.',place='Section headings'),
  dict(sign='Ordinary typed S',latex='S',evidence='Single curved typewriter contour, without a second independent alphabetic outline.',place='5.1, S-schéma'),
  dict(sign='Decimal entry labels',latex='3.8.; 3.9.; 3.10.; 4.1.–4.6.; 5.1.–5.5.; 6.1.–6.11.',evidence='The typewritten digits and low separating/terminal points were read separately; the last two labels have no visible word-space after the terminal point.',place='Entry labels'),
  dict(sign='Leader points',latex=r'\dotfill',evidence='Repeated low ring-shaped typewriter impressions extend to the right margin; absent for 3.10 and 6.8.',place='Contents entries and section headings'),
  dict(sign='Detached lower point',latex=point,evidence='Small oblique oval lower and to the right of the heading period; textual status not established.',place='§4 heading'),
  dict(sign='Detached point pair',latex=pair,evidence='Lower compact angular point and upper narrower oblique oval on a short rising diagonal.',place='Above the right end of 6.3 leaders'),
  dict(sign='Overprinted underletter',latex=r'\deleted{\unsure{l|t|j}}i',evidence='Merged upper head/point traces and a low surviving foot; old character remains uncertain.',place='6.10, schématique')
 ],
 abbreviations=[],slips=[],
 completion='Full assigned-page coverage completed: whole image once, half a once and half b once in that order, followed by one retained enlargement for each of seven remaining open loci, viewed once each. Every word, accent, number, punctuation sign, leader series, overtyped character and potentially textual graphic was checked. All five explicit C doubts and all substantive C changes are reported, all confirmed unmarked C-context targets are recorded, and H is unavailable throughout. Reading and report were saved; only source balance and JSON/schema checks were performed after writing, without TeX compilation.'
)
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote reading.tex ({len(reading)} characters) and report.json with {len(decisions)} decisions, {len(inventory)} inventory rows, {len(manifest)} crops.')
