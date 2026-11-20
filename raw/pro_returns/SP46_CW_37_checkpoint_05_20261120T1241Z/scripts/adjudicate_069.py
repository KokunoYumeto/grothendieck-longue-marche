from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan069/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC'];ds=copy.deepcopy(A)
bm=[0,1,3,5,4,7,8,11,12,13,14,15,16,17,19]
cm=[0,1,4,6,5,9,10,11,None,12,13,14,15,16,18]
for i,d in enumerate(ds):
 d['readers']={'A':A[i]['reading'],'B':B[bm[i]]['reading'],'C':C[cm[i]]['reading'] if cm[i] is not None else "``implique''"}
 d['crop']='';d['marked_in_H']='no'
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
cp=lambda f:'readers/scan069/C/'+f
for i,f in [(3,'C069_quote_before_X.jpg'),(7,'C069_overtyped_de.jpg'),(10,'C069_detached_dot.jpg'),(11,'C069_Q_coefficient.jpg'),(12,'C069_Q_coefficient.jpg'),(14,'C069_final_de.jpg')]:ds[i]['crop']=cp(f)
ds[0].update(crop='crops/scan069/pagination.jpg',scan_shows='The handwritten 4 is flanked by two separate short horizontal strokes. Both strokes are visible in the main crop and were independently reported by all three readers; retain - 4 -.')
ds[3]['scan_shows']='Two short handwritten strokes are joined low into a shallow cup above the implication-arrow tip. Their orientation does not securely distinguish an opening pair from a closing pair. Preserve the original opening-pair preference and closing-pair alternative without adding balancing marks.'
ds[7]['scan_shows']='The live e has a dark horizontal middle and open lower-right form. A broader upper curve, right upright and projecting foot survive beneath it, identifying the underlying a. All three readers and the main crop resolve d\\deleted{a}e.'
ds[8].update(crop='readers/scan069/A/A_06_p9_implique_quote.jpg',scan_shows='Three near-vertical dark strokes can be separated before the i, with the two left ones crowded and joined at the top. The image permits three quotation strokes, or a doubled impression within a pair. Retain A’s triple-stroke preference with the ordinary pair as alternative; B and C read the pair without a doubt. No deletion chronology is assigned.')
spot_tikz=r'''\begin{tikzpicture}[x=1mm,y=1mm,baseline=0pt]
\fill (0,0) .. controls (-0.12,0.12) and (-0.09,0.42) .. (0.02,0.52)
 .. controls (0.15,0.63) and (0.30,0.43) .. (0.28,0.24)
 .. controls (0.28,0.06) and (0.14,-0.03) .. (0,0) -- cycle;
\end{tikzpicture}'''
pair_tikz=r'''\begin{tikzpicture}[x=1mm,y=1mm,baseline=0pt]
\fill (0,0) .. controls (-0.12,0.10) and (-0.17,0.35) .. (0.01,0.42)
 .. controls (0.16,0.48) and (0.36,0.30) .. (0.25,0.14)
 .. controls (0.17,0.03) and (0.07,-0.05) .. (0,0) -- cycle;
\fill (0.60,1.13) ellipse[x radius=0.34,y radius=0.17,rotate=45];
\end{tikzpicture}'''
# The supplied figure macro is a paragraph-level centered block. Small parboxes
# preserve that required macro while anchoring these tiny shapes inline.
spot=r'\hspace{0.4em}\raisebox{0.35ex}[0pt][0pt]{\parbox[c]{2mm}{\figure{\unsure{'+spot_tikz+r'}}}}'
pair=r'\makebox[0pt][l]{\hspace{0.70em}\raisebox{-1.45ex}[0pt][0pt]{\parbox[c]{2mm}{\figure{\unsure{'+pair_tikz+r'}}}}}'
ds[10].update(reading=spot,scan_shows='A small detached dark patch stands above the baseline to the right of the question mark. Its blurred outline is roughly upright and rounded, rather than a typographic full stop. C’s uncertainty about punctuation versus surface speck remains; the main graphic follows the crop’s shape and position.')
ds[11]['scan_shows']='The faint lowered Q has one oval outline, an inner lower curl continuous with its outward tail, and a separate dark horizontal underline. There is no independent parallel stroke supporting a double-struck alphabet. Resolve the underlined Q with all three readers.'
ds[12].update(reading=pair,scan_shows='Below the r of the second Gr are two detached dark marks: an upper-right oblique oval and a lower-left small angular point. All three readers found this omitted pair in their existing coefficient crop. Preserve the pair graphically, with its authored status and function left uncertain.')
ds[14]['scan_shows']='A faint tall ascender with a leftward top serif and right basal foot survives behind the dark e. Those parts match the adjacent live d and extend both above and below the e; they cannot be accounted for by an accent alone. Read d\\deleted{d}e, retaining the underprint and the live unaccented vowel.'
s=(O/'readers/scan069/A/reading.tex').read_text()
start=s.index('% A small detached, raised quadrilateral');end=s.index('p.10, li.11',start)
s=s[:start]+'''% Detached marks retain uncertain authorship; small inline boxes preserve their relative placement.
p.9 : références pour $\\mathrm{Gr}^{\\bullet}_{\\mathrm{top}}$ et l'assertion de compatibilité aux filtrations ?'''+spot+'''\n\nDonner aussi le diagramme analogue à (7.10.1 bis) avec '''+pair+r'''$\mathrm{Gr}^{\bullet}(\ )_{\underline{Q}}$ pour $g$ projectif, d'intersection complète, et de dimension relative virtuelle donnée.

'''+s[end:]
if not s.rstrip().endswith(r'\clearpage'):s=s.rstrip()+'\n\\clearpage\n'
(O/'pages/B37-04_37_scan069.tex').write_text(s)
notes=R['C']['notes']+' The crowding before implique permits three visible quotation strokes or a doubled impression within a pair; that new reader uncertainty remains explicit. The final de is unaccented live text over an underlying d, not a spelling modernization. The tiny graphic groups use the prescribed figure macro inside inline boxes to preserve their placement.'
notation=copy.deepcopy(R['C']['notation']);notation.append(dict(sign='Crowded typed quotation strokes',latex=r'\unsure{```|``}',evidence='Three upright traces, the left two crowded; ordinary pair with a doubled impression remains possible.',place='Before implique, p.9 li.6.'))
out=dict(scan=69,decisions=ds,inventory=R['C']['inventory'],notes=notes,math_reading_decisions=R['C']['math_reading_decisions'],notation=notation,abbreviations=R['C']['abbreviations'],slips=R['C']['slips']+['The three-or-doubled quotation strokes before implique remain uncertain; no typing chronology is inferred.'],check_events=[],main_crops=json.loads((O/'crops/scan069/manifest.json').read_text()))
(O/'decisions/scan069.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Wrote scan 069: 15 records, five explicit C doubts reviewed, seven C differences.')
