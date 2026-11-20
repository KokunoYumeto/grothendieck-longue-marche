from pathlib import Path
import json
import re

out=Path('/workspace/scratch/006c0e32b2af/out/readers/scan074/B')
packet=Path('/workspace/scratch/006c0e32b2af/packets/scan074')
meta=json.loads((packet/'meta.json').read_text())
c=(packet/'C.tex').read_text()
curve=r'''\margin{\figure{\unsure{\handwritten{\begin{tikzpicture}[x=0.5cm,y=0.5cm]
\draw[line width=0.25pt] (0,0.65) .. controls (0.4,0.46) and (1.12,0.24) .. (1.02,0.05) .. controls (1.00,0.01) and (0.96,0.00) .. (0.94,0.00);
\end{tikzpicture}}}}}'''
reading=r'''\scanpage{74}

\begin{flushright}
Massy le 3.11.1970\\
\end{flushright}

\noindent Cher Ferrand,\\

% The right edge cuts through the character after diso; no invisible ending is supplied.
J'aimerais savoir si je peux compter sur ton exposé SGA 6 XI dans un avenir assez rapproché (diso\unsure{n|u|r} d'ici fin décembre). Dans le cas contraire, je pense qu'il serait préfé\deleted{é}r\deleted{\unsure{r}}able que je publie SGA 6 sans l'exposé XI. Il serait quand même raisonnable, après le travail que tu t'es tapé, que tu en fasses au moins un article d'exposition, et j'aimerais savoir alors où tu penses le publier, pour que je puisse y référer dans l'introduction à SGA 6.

Bien cordialement\\

% Isolated curved trace in the lower-right blank area; pen versus surface trace is uncertain.
'''+curve+r'''
% archive sheet number: 73
'''
(out/'reading.tex').write_text(reading)
c_curve=c[c.index(r'\margin{'):c.index('% archive')].strip()
crops=json.loads((out/'crop_manifest.json').read_text())
report={
 'scan':74,
 'reader':'B',
 'image_views':meta['images'],
 'reading_path':str(out/'reading.tex'),
 'crops':crops,
 'decisions':[
  {
   'id':'B074-01',
   'place':'Body, second typed line: clipped character after diso at the right edge.',
   'c_reading':r'diso\unsure{l|n|u}',
   'h_reading':r'diso\supplied{ns}',
   'reading':r'diso\unsure{n|u|r}',
   'diff_c':True,'diff_h':True,'c_doubt':True,'unresolved':True,
   'alternatives':['n (partial)','u (partial)','r (partial)'],
   'confidence':'low','kind':'misread word',
   'scan_shows':'After the complete diso, the surviving character starts at the same low x-height as the neighboring lower-case forms: a short upper-left horizontal serif, a vertical stem, and a low left foot survive. The right side is removed by the cut edge. No tall ascender supports l, and no final s survives. The added r alternative and changed preference are substantive changes to C\'s recorded uncertainty. H supplies the unseen complete ending ns.',
   'crop':str(out/'B074_01_clipped_diso.jpg'),
   'bbox':[1102,315,1195,349]
  },
  {
   'id':'B074-02',
   'place':'Body, quatrième typed line: first overtyped position within préférable, the live r.',
   'c_reading':r'\deleted{é}r',
   'h_reading':'r',
   'reading':r'\deleted{é}r',
   'diff_c':False,'diff_h':True,'c_doubt':False,'unresolved':False,
   'alternatives':[],
   'confidence':'high','kind':'omission',
   'scan_shows':'A separate acute diagonal stands above this position. Beneath the live upright and hooked upper shoulder of r, an e-shaped loop and transverse middle stroke remain. This is an accented underlying é, not just a heavy r. H\'s préférable gives the live r alone and omits this readable underprint.',
   'crop':str(out/'B074_02_preferable.jpg'),
   'bbox':[518,389,540,422]
  },
  {
   'id':'B074-03',
   'place':'Same word, second overtyped position: possible underlying r beneath the live a.',
   'c_reading':r'\deleted{\unsure{r}}a',
   'h_reading':'a',
   'reading':r'\deleted{\unsure{r}}a',
   'diff_c':False,'diff_h':True,'c_doubt':True,'unresolved':True,
   'alternatives':['r beneath a; the obscured shoulder remains uncertain'],
   'confidence':'medium','kind':'omission',
   'scan_shows':'The live a has a lower bowl and right upright. A darker upper horizontal/shouldered trace and extra upright occupy its left portion, supporting an underlying r, but the superposed strokes do not isolate the full shoulder securely. C\'s explicit doubt is therefore retained unchanged; H gives only the live a.',
   'crop':str(out/'B074_02_preferable.jpg'),
   'bbox':[539,396,561,423]
  },
  {
   'id':'B074-04',
   'place':'Body, fifth typed line, après at the clipped right edge.',
   'c_reading':'après',
   'h_reading':r'aprè\supplied{s}',
   'reading':'après',
   'diff_c':False,'diff_h':True,'c_doubt':False,'unresolved':False,
   'alternatives':[],
   'confidence':'high','kind':'other',
   'scan_shows':'The grave accent over è is visible, followed by the left portions of the final s: an upper bend, narrow middle, and lower curved trace reach the cut edge. The s is clipped but is not wholly absent. H treats the entire s as supplied; the half image permits the surviving s to be read directly. This is a source-status difference, not a different spelling.',
   'crop':'',
   'bbox':[1101,422,1195,456]
  },
  {
   'id':'B074-05',
   'place':'Isolated curved mark in the lower-right blank area, far below the closing.',
   'c_reading':c_curve,
   'h_reading':'',
   'reading':curve,
   'diff_c':True,'diff_h':True,'c_doubt':False,'unresolved':True,
   'alternatives':['pen stroke by an unidentified hand','surface trace or fiber rather than authored ink'],
   'confidence':'medium','kind':'drawing or diagram',
   'scan_shows':'One dark, narrow, slightly irregular stroke runs down and right from a small raised starting nub, rounds downward at the right, then hooks back a short distance left at its foot. No letter or signature can be read. Its shape is secure; the image does not securely distinguish a pen mark from a dark surface trace. C reproduces the curve but assigns it to handwriting without an in-place doubt; H omits it. The final snippet preserves C\'s adequate geometry and adds uncertainty of material status.',
   'crop':str(out/'B074_03_lower_right_curve.jpg'),
   'bbox':[1110,1504,1167,1545]
  }
 ],
 'inventory':[
  {'sheet_kind':'letter','hand':'typewriter','element':'Place and date','kind':'text','position':'Upper right, approximately x690–1051 y138–166','first_words_or_objects':'Massy le 3.11.1970','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Salutation','kind':'text','position':'Upper left below date, approximately x160–414 y213–244','first_words_or_objects':'Cher Ferrand,','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Single body paragraph, nine typed lines; right edge clips diso… and final s of après','kind':'text','position':'Upper body, approximately x157–1195 y281–598','first_words_or_objects':"J'aimerais savoir si je peux compter sur ton",'transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Readable underlying é beneath r in préférable','kind':'deletion','position':'Body fourth line, x518–540 y389–422','first_words_or_objects':r'\deleted{é}r','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Uncertain underlying r beneath a in préférable','kind':'deletion','position':'Body fourth line, x539–561 y396–423','first_words_or_objects':r'\deleted{\unsure{r}}a','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'typewriter','element':'Closing; no signature text follows','kind':'text','position':'Below body, approximately x238–577 y618–646','first_words_or_objects':'Bien cordialement','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'unnamed hand','element':'Unlabelled dark curved trace; pen status uncertain','kind':'drawing','position':'Lower-right blank area, x1110–1167 y1504–1545','first_words_or_objects':'Down-right curved stroke with short leftward terminal hook','transcribed':'yes'},
  {'sheet_kind':'letter','hand':'unnamed hand','element':'Archive sheet number, recorded only as a comment','kind':'text','position':'Bottom left, approximately x85–147 y1655–1705','first_words_or_objects':'73','transcribed':'yes'}
 ],
 'notes':'An unsigned typewritten French letter asks Ferrand whether his SGA 6 exposé XI can be expected by the end of December; otherwise the writer proposes publishing SGA 6 without it and asks where an exposition article might appear so the introduction can refer to it. No title is present. Place/date: Massy le 3.11.1970. Salutation: Cher Ferrand,. Closing: Bien cordialement. This packet contains one letter page, with no original manuscript page number and archive sheet number 73 at bottom left. There are no explicit author doubt marks. The right edge is physically clipped. Two overtyped positions survive in préférable. The central long pale vertical feature below the closing follows the paper surface and is treated as a crease, not authored writing. The isolated dark lower-right curve is reproduced with material-status uncertainty. All three requested source images and all three crop images reached the visual context; each source and each crop was inspected once, with no repeat view.',
 'math_reading_decisions':[
  'The three SGA 6 references and the two XI references were read separately. They are ordinary typewritten capitals and numerals, without independent doubled outlines, underlines, or added mathematical marks.',
  'The date reads 3.11.1970 with typed periods; its numerals have the same machine impression character as the body. No mathematical display or proof is present.',
  'The unmarked C-context target for the first overprint is confirmed as an underlying é beneath live r. The second overprint remains explicitly uncertain, and both are reported above.'
 ],
 'check_events':[],
 'notation':[
  {'sign':'Ordinary typewritten work and exposé references','latex':'SGA 6 XI; SGA 6; XI','evidence':'S, G and A have single ordinary machine outlines, the 6 has one loop, and XI consists of crossed X and one upright I. There are no separate upper/lower rules.','place':'First, fourth/fifth, and final body lines'},
  {'sign':'Clipped lower-case terminal character','latex':r'diso\unsure{n|u|r}','evidence':'Only an x-height upper serif, upright, and lower foot remain before the physical cut; there is no surviving high ascender or final s.','place':'Right edge of the second body line'},
  {'sign':'Isolated curved trace with uncertain material status','latex':curve,'evidence':'Dark down-right stroke with a rounded lower-right bend and short leftward return; no alphabetic form is securely present.','place':'Lower-right blank area'}
 ],
 'abbreviations':[{'form':'SGA','expansion':'Not expanded on the page; retained as typed.'}],
 'slips':[
  'The word préférable contains a typed underlying é at the live r position and a further uncertain r-like underprint at the live a position. These are retained as correction states, not silently normalized.'
 ],
 'completion':'Complete independent reading of the whole-page layout and both full-resolution halves, checked line by line against C and H. All visible text, accents, punctuation, clipping, both overprints, the closing, the isolated lower-right trace, and the archive number are covered. The three remaining open loci received one tight enlarged crop each; no page or crop was reopened. Every substantive witness difference, both explicit C doubts, and the new material-status uncertainty are recorded with whole-page bounding boxes. No OCR, external text, web research, other pages, peer readings, or TeX compilation was used.'
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

# Structural checks only: no TeX engine is invoked.
src='\n'.join(line.split('%',1)[0] for line in reading.splitlines())
stack=[]
for i,ch in enumerate(src):
    if ch in '{}':
        backslashes=0
        k=i-1
        while k>=0 and src[k]=='\\':
            backslashes+=1
            k-=1
        if backslashes%2:
            continue
        if ch=='{': stack.append(i)
        elif not stack: raise AssertionError('Unmatched closing brace')
        else: stack.pop()
assert not stack,stack
estack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',src):
    if m.group(1)=='begin': estack.append(m.group(2))
    else:
        assert estack and estack.pop()==m.group(2)
assert not estack
assert json.loads((out/'report.json').read_text())['scan']==74
assert len(report['image_views'])==3 and len(report['crops'])==3
for d in report['decisions']:
    assert len(d['bbox'])==4
    assert 0<=d['bbox'][0]<d['bbox'][2]<=1249
    assert 0<=d['bbox'][1]<d['bbox'][3]<=1761
print('Saved reading.tex and report.json; brace/environment balance and JSON/bbox checks passed; no TeX compilation.')
print('Decision count:',len(report['decisions']))
print('Actual image inspections: 3 sources, 3 crops, each once.')
