from pathlib import Path
import csv
import json
import re

ROOT=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
PACKET=ROOT/'packets/145_scan019'
OUT=ROOT/'edition'
manifest=json.loads((OUT/'reader_reports/145_scan019_crop_boxes.json').read_text())
boxes={x['name']:x['box'] for x in manifest}
def crop(name): return 'crops/145_scan019_'+name+'.png'

tex=(PACKET/'C.tex').read_text()
for old,new,n in [
    (r'\varepsilon_0&=l_0^{\deleted{\unsure{-1}}}\sigma_0l_1^{\deleted{\unsure{-1}}}',
     r'\varepsilon_0&=l_0^{\deleted{\unsure{-1}}}\sigma_0l_{\unsure{1}}^{\deleted{\unsure{-1}}}',1),
    (r'\varepsilon_1&=l_1^{\deleted{\unsure{-1}}}\sigma_1l_\infty^{\deleted{\unsure{-1}}}',
     r'\varepsilon_1&=l_{\unsure{1}}^{\deleted{\unsure{-1}}}\sigma_1l_\infty^{\deleted{\unsure{-1}}}',1),
    (r'\varepsilon_\infty&=l_\infty\sigma_\infty l_0^{\deleted{\unsure{-1}}}',
     r'\varepsilon_\infty&=l_\infty\sigma_\infty l_{\unsure{0}}^{\deleted{\unsure{-1}}}',1),
    (r'\varepsilon_{\rho i}',r'\varepsilon_{\dot\rho i}',1),
    (' i.e.',' i.e',1),
    (r'\text{OK}',r'\text{ok}',1),
    (r'\rho\deleted{\unsure{l_\infty}}(\ldots),\quad\varepsilon_1\varepsilon_\infty=\ldots,\quad\varepsilon_\infty\varepsilon_0=\ldots',
     r'\rho\deleted{\unsure{l_\infty}}(\unsure{..|\ldots}),\quad\varepsilon_1\varepsilon_\infty=\mathinner{..},\quad\varepsilon_\infty\varepsilon_0=\mathinner{.\!-}',1),
    (r'\rho\unsure{l_0}',r'\rho l_0',2),
    (r'\rho\unsure{l_1}',r'\rho l_1',1),
    (r'\rho\unsure{l_\infty}',r'\rho l_\infty ',1),
    ('Eliminant les','Éliminant les',1),
]:
    assert tex.count(old)==n,(old,tex.count(old),n)
    tex=tex.replace(old,new)
assert tex.count(r'\deleted{\unsure{l_\infty}}')==1
assert r'\rhol' not in tex and r'\inftyl' not in tex

eight=tex[tex.index(r'\['):tex.index(r'\]')+2]
margin_start=tex.index(r'\margin{')
margin_end=tex.index('\nOn a bien')
margin=tex[margin_start:margin_end]
square_start=tex.index(r'\[',tex.index('On a bien'))
square_end=tex.index(r'\]',square_start)+2
square=tex[square_start:square_end]
nb_start=tex.index(r'(\uline{NB}')
nb_end=tex.index('\n\nIci')
nb=tex[nb_start:nb_end]
system_start=tex.index('Ici on voit')
system_end=tex.index('\n\\[',system_start)
system=tex[system_start:system_end]
relations_start=system_end+1
relations_end=tex.index(r'\]',relations_start)+2
relations=tex[relations_start:relations_end]
completion_start=tex.index('où il faut compléter')
completion_end=tex.index('\n\\deleted',completion_start)
completion=tex[completion_start:completion_end]
cancelled_start=completion_end+1
cancelled_end=tex.index('\n\\[',cancelled_start)
cancelled=tex[cancelled_start:cancelled_end]
product_start=cancelled_end+1
product_end=tex.index(r'\]',product_start)+2
product=tex[product_start:product_end]
nine_start=tex.index(r'\[',tex.index('donc finalement'))
nine_end=tex.index(r'\]',nine_start)+2
nine=tex[nine_start:nine_end]
final_prose=tex[tex.index('Éliminant les'):tex.index(r'\mspage{18}')].strip()
(OUT/'reader_reports/145_scan019.tex').write_text(tex)

changes=[]
def change(n,place,C,H,final,ink,confidence,kind,cc,hc,marked,name,cats,math=''):
    changes.append({
        'id':f's019-{n:02d}','place':place,'C':C,'H':H,'final':final,
        'ink':ink,'confidence':confidence,'kind':kind,'c_changed':cc,'h_changed':hc,
        'marked_in_H':marked,'crop':crop(name),'box':boxes[name],
        'error_category':cats,'math_consequence':math,
    })

change(1,'display (8), the five small cancelled superscripts',
       r'l_0^{\deleted{\unsure{-1}}}\sigma_0l_1^{\deleted{\unsure{-1}}};\quad l_1^{\deleted{\unsure{-1}}}\sigma_1l_\infty^{\deleted{\unsure{-1}}};\quad l_\infty\sigma_\infty l_0^{\deleted{\unsure{-1}}}',
       r'l_0^{\ill{}}\,\sigma_0\,l_1^{\ill{}};\quad l_1^{\ill{}}\,\sigma_1\,l_\infty^{\ill{}};\quad l_\infty\,\sigma_\infty\,l_0^{\ill{}}',
       r'l_0^{\deleted{\unsure{-1}}}\sigma_0l_{\unsure{1}}^{\deleted{\unsure{-1}}};\quad l_{\unsure{1}}^{\deleted{\unsure{-1}}}\sigma_1l_\infty^{\deleted{\unsure{-1}}};\quad l_\infty\sigma_\infty l_{\unsure{0}}^{\deleted{\unsure{-1}}}',
       'There are exactly five small superscript clusters: both l factors in the first two rows and only the final l factor in the third row. Each contains short horizontal/upright traces crossed by extra oblique strokes. Minus-one is compatible with the remains, but none is resolved through its cancellation. They are cancelled superscripts, not live illegible exponents. Three newly doubtful overwritten subscripts are recorded in doubts only.',
       'medium','deletion state',False,True,'yes','formula_eight',[5,7],
       'Preserves the cancellation of the tentative inverse exponents in the written definitions.')
change(2,'right-margin NB label',
       r'\uline{NB}',r'\text{NB}',r'\uline{NB}',
       'Below the two large letters there is a separate dark underline, extending across their width and rising slightly at the right. It is not part of either letter.',
       'high','other',False,True,'no','margin_covariance',[10])
change(3,'right-margin covariance formula, right-hand epsilon subscript',
       r'\varepsilon_{\rho i}',r'\varepsilon_{\rho(i)}',r'\varepsilon_{\dot\rho i}',
       'The rho in the small right-hand subscript has a distinct detached dark dot above its loop. A second separate dot belongs to the following i. No parentheses surround i. The other rho factors in this margin note are undotted.',
       'high','misread symbol or index',True,True,'no','margin_covariance',[1,3,9],
       'Restores the locally written dotted rho in the action on the index, without adding function-argument parentheses.')
change(4,'abbreviation after the general covariance formula',
       'i.e.','i.e.','i.e',
       'The point between i and e is visible. The e ends in its normal stroke and is followed by blank paper; there is no separate terminal point. Both drafts supply that final punctuation.',
       'high','other',True,True,'no','margin_covariance',[10])
change(5,'square verification, formula attached to the underbrace',
       r'\underbrace{\sigma_0l_1l_0\sigma_0}_{\substack{\sigma_0(l_1l_0)=\sigma_0(l_1)\sigma_0(l_0)\\=l_\infty(l_1l_\infty)^{-1}=l_1^{-1}}}',
       r'\underbrace{\sigma_0\,l_1\,l_0\,\sigma_0}'+'\n'+r'\[\sigma_0(l_1 l_0)=\sigma_0(l_1)\,\sigma_0(l_0)=l_\infty\,(l_1l_\infty)^{-1}=l_1^{-1}\]',
       r'\underbrace{\sigma_0l_1l_0\sigma_0}_{\substack{\sigma_0(l_1l_0)=\sigma_0(l_1)\sigma_0(l_0)\\=l_\infty(l_1l_\infty)^{-1}=l_1^{-1}}}',
       'The brace spans precisely sigma0 l1 l0 sigma0. Its central cusp points to the two calculation rows immediately beneath this factor; the second row begins with an equals sign. H places the calculation in a detached display instead of preserving this specific brace attachment.',
       'high','insertion or placement',False,True,'no','square_verification',[6],
       'Preserves which factor the author is evaluating.')
change(6,'right end of the square verification',
       r'\text{OK}',r'\text{ok}',r'\text{ok}',
       'The first letter is a small oval at lowercase height. The following k has a taller stem and two lower arms. These are lowercase o and k, not two capitals.',
       'high','misread word',True,False,'no','square_verification',[2])
change(7,'opening of the parenthetic NB paragraph',
       r'(\uline{NB}',r'\textbf{NB}',r'(\uline{NB}',
       'A separate opening parenthesis curves down the left of NB. A horizontal stroke under the two letters is an underline. The matching closing parenthesis is visible at the end of the next line.',
       'high','omission',False,True,'no','nb_left_cancelled_ici',[3,10])
change(8,'NB paragraph, cancelled wording and raised replacement after tantôt',
       r"\deleted{\unsure{il faudrait}} \inserted{qu'il faudra}",
       r"\struck{qu'il faudrait \ill{} noter $\varepsilon'_i$ …}",
       r"\deleted{\unsure{il faudrait}} \inserted{qu'il faudra}",
       'The raised replacement has q with a long descending stem, u, apostrophe, dotted i and l, then the tall looped f, low au, upright d and final ra. There is no final t after faudra. The baseline phrase is crossed horizontally; fragments support il faudrait but are not sufficiently separate to resolve it. The live raised q descender crosses the lower strike and must not be assigned to a struck qu’il.',
       'medium','deletion state',False,True,'yes','nb_faudrait_revision',[2,5,6,7])
change(9,'NB paragraph, lower line from the cancelled ici through noter',
       r"\deleted{\unsure{ici}} donc noter $\varepsilon'_i\ldots$)",
       r"\struck{qu'il faudrait \ill{} noter $\varepsilon'_i$ …})",
       r"\deleted{\unsure{ici}} donc noter $\varepsilon'_i\ldots$)",
       'A short crossed word at the far left has a tall opening trace, small dotted/curved bodies and is compatible with ici, still doubtful. Its strike stops before donc. The d loop and connected onc of donc, the n/o, tall t and er of noter, and the primed epsilon with i and three separate following marks remain live. H omits donc and extends the deletion across the surviving ending.',
       'medium','deletion state',False,True,'yes','nb_left_cancelled_ici',[3,5,7])
change(10,'two-line introduction of the generators and relations',
       r"Ici on voit donc qu'on a un syst. de gén. et relations \inserted{de $\mathcal E^+$}",
       r'Ceci dit, \uncertain{on a une} présentation de $\mathcal{E}^{+}$ par générateurs et relations,',
       r"Ici on voit donc qu'on a un syst. de gén. et relations \inserted{de $\mathcal E^+$}",
       'The opening reads Ici, then on voit: the tall v/t contour of voit and its i dot are present. donc has its d loop; qu’on has the long q descender and apostrophe. un syst. has the short un body, y descender, tall final t and a stop. gén. is visibly abbreviated with a stop. relations continues on the next baseline. The small de E+ insertion has a curved guide into the gap after relations, before the generator list. H’s Ceci dit, présentation and par générateurs are not the written words.',
       'high','misread word',False,True,'yes','generators_prose',[2,6,8,9])
change(11,'uncompleted relation, cancelled factor immediately after rho',
       r'\rho\deleted{\unsure{l_\infty}}',r'\rho',r'\rho\deleted{\unsure{l_\infty}}',
       'A small looped/upright factor and low looped index occur between the rho and the placeholder parenthesis. They are crossed and merge with the parenthesis boundary. l-infinity is plausible but not resolved. The cancelled factor is present; H omits it.',
       'low','omission',False,True,'no','relation_block',[3,7])
change(12,'the three uncompleted product placeholders in the relations block',
       r'\rho\deleted{\unsure{l_\infty}}(\ldots),\quad\varepsilon_1\varepsilon_\infty=\ldots,\quad\varepsilon_\infty\varepsilon_0=\ldots',
       r'\rho(\ldots),\quad\varepsilon_1\varepsilon_\infty=\ldots,\quad\varepsilon_\infty\varepsilon_0=\ldots',
       r'\rho\deleted{\unsure{l_\infty}}(\unsure{..|\ldots}),\quad\varepsilon_1\varepsilon_\infty=\mathinner{..},\quad\varepsilon_\infty\varepsilon_0=\mathinner{.\!-}',
       'After the second product equality there are exactly two separated dark points. After the third there is one point and one short horizontal dash-like mark. Neither has three dots. Inside the first parentheses two marks are visible, but cancellation at the left could conceal another; that count remains uncertain. The dot-dash pair is reproduced as a placeholder, not interpreted as subtraction.',
       'medium','other',True,True,'no','relation_block',[1,10],
       'Preserves the author’s unfinished placeholders rather than regularizing their visible marks to three-dot ellipses.')
change(13,'comme and produits in the instruction to complete the products',
       r'\inserted{comme} produits','comme produit',r'\inserted{comme} produits',
       'The darker compact comme has c/o followed by two shallow m bodies and a final e, inserted before the next word. produits has the p descender, connected r/o/d/u/i sequence, tall crossed t and a small hooked continuation after that t supporting final s. The plural is retained from the ink.',
       'high','misread word',False,True,'no','comme_produits',[2,6])
change(14,'cancelled short product between prose lines',
       r'\deleted{$\varepsilon_0\varepsilon_1=l_0\sigma_1l_1$}',
       r'\struck{$\varepsilon_0\varepsilon_1=l_0\sigma l_1$}',
       r'\deleted{$\varepsilon_0\varepsilon_1=l_0\sigma_1l_1$}',
       'A distinct short black vertical 1 stands at the lower right of the sigma and before the last looped l. The long cancellation crosses the whole formula, leaving this subscript visible below it. All factors of the short formula, including this 1, are readable.',
       'high','misread symbol or index',False,True,'no','cancelled_product',[1,3])
change(15,'display (9), extra crossed glyph in the first left member',
       r'\varepsilon_0\varepsilon_1\deleted{\unsure{\varepsilon}}',
       r'\varepsilon_0\varepsilon_1',
       r'\varepsilon_0\varepsilon_1\deleted{\unsure{\varepsilon}}',
       'After the two surviving epsilon factors there is a separate small glyph, crossed and retraced, before the equals sign. Its curved upper and lower bodies support epsilon, but intersecting strokes prevent a certain reading. The additional cancelled glyph cannot be omitted.',
       'low','omission',False,True,'no','formula_nine',[3,7])
change(16,'first word of the final prose',
       'Eliminant','Éliminant','Éliminant',
       'A compact dark oblique mark is centered above the capital E, separate from its top stroke and from the following tall l. It is an accent mark; the accented French letter is retained.',
       'high','misread word',True,False,'no','eliminant_accent',[2])
change(17,'final line, wording before the doubtful last word',
       r'avec relations de \unsure{définition}','une relation de définition',
       r'avec relations de \unsure{définition}',
       'The first word has a small a body followed by low v/e/c strokes, not the un/e contour of une. relations has its r/e, tall looped l, crossed t and a hooked plural ending. The following de is separate. The compressed last word remains doubtful, especially its termination.',
       'high','misread word',False,True,'no','definition_ending',[2])
change(18,'lower-left handwritten pagination',
       r'\mspage{18}','',r'\mspage{18}',
       'The first digit has an ascending entry and a long upright. The second has two closed connected loops, the upper narrower than the lower: 18. It is an actual handwritten page number and distinct from the editorial scan identifier.',
       'high','omission',False,True,'no','manuscript_number_eighteen',[3])

decisions=[]
def dec(id,name,reading,ink,confidence,result):
    decisions.append({'id':id,'decision':result,'reading':reading,'ink':ink,
                      'crop':crop(name),'box':boxes[name],'confidence':confidence})
dec('M0833','square_verification',r'\unsure{1}',
    'The l following the first underbrace has a darkened index combining upright and looping traces. A 1 is plausible but the lower overwriting does not separate it securely. The complete square verification and its two annotation rows were read.',
    'low','undecided')
dec('M0834','product_derivation',r'l_0',
    'After the rho, the live looped l has its own downstroke and rightward foot; its separate low rounded 0 is visible before the last l-infinity. Earlier overlapping traces do not erase these current letter and index strokes.',
    'high','first')
dec('M0835','formula_nine',r'l_0',
    'In row 1 after rho, the current tall looped l and its separate small closed 0 can be followed despite residual vertical strokes. The following l-infinity is a separate factor.',
    'high','first')
dec('M0836','formula_nine',r'l_1',
    'In row 2 after rho, the current l body is clear and the index has a tall straight 1 with a firm lower foot. Old curved traces under and beside it do not obscure the live 1.',
    'high','first')
dec('M0837','formula_nine',r'l_\infty',
    'In row 3 after rho, the current l has a visible upper loop and foot and the low index consists of two joined loops. The following l1 is separate. Lower overwritten traces are recorded as a material-state uncertainty, not as a different live factor.',
    'high','first')
dec('M0838','definition_ending',r'\unsure{définition}',
    'The opening dé/f region and dotted i are supported, but the letters following the tall f are compressed and the final tion sequence cannot be independently separated at the right edge. The full word is left tentative.',
    'medium','undecided')

unlisted_decisions=[]
def unlisted(id,name,reading,ink,confidence='low'):
    unlisted_decisions.append({'id':id,'decision':'undecided','reading':reading,'ink':ink,
                              'crop':crop(name),'box':boxes[name],'confidence':confidence})
for j,place in enumerate([
    'row 1, first l0','row 1, final l1','row 2, first l1',
    'row 2, final l-infinity','row 3, final l0'
],1):
    unlisted(f'U019-{j:02d}','formula_eight',r'\deleted{\unsure{-1}}',
             'At '+place+', short horizontal and upright traces remain inside a small obliquely crossed superscript cluster. Minus-one is plausible, but cancellation prevents resolving both characters.')
unlisted('U019-06','nb_faudrait_revision',r'\deleted{\unsure{il faudrait}}',
         'The crossed baseline fragments support il faudrait. The raised q descender overlaps them, and the original letters cannot all be isolated.')
unlisted('U019-07','nb_left_cancelled_ici',r'\deleted{\unsure{ici}}',
         'The short struck word has narrow upright and curved fragments compatible with ici, but not all letters are separable from the strike.')
unlisted('U019-08','relation_block',r'\deleted{\unsure{l_\infty}}',
         'The small cancelled factor next to rho has an l-like loop and low looped traces, entangled with the left parenthesis; the index remains uncertain.')
unlisted('U019-09','formula_nine',r'\deleted{\unsure{\varepsilon}}',
         'A separate crossed curved glyph follows the two live epsilon factors in row 1; epsilon is supported but not fully clear.')

doubts=[]
def doubt(place,reading,alternatives,reason,confidence='low'):
    doubts.append({'place':place,'reading':reading,'alternatives':alternatives,
                   'confidence':confidence,'reason':reason})
for place in ['(8), row 1 first l0 exponent','(8), row 1 final l exponent',
              '(8), row 2 first l exponent','(8), row 2 final l-infinity exponent',
              '(8), row 3 final l exponent']:
    doubt(place,r'\deleted{\unsure{-1}}',['-1'],
          'Small crossed superscript; neither the sign nor digit can be fully isolated through the cancellation.')
doubt('(8), row 1 final l subscript',r'\unsure{1}',['1'],
      'New doubt: the subscript combines a dark upright with looped overwritten remains; the current numeral cannot be confidently separated.')
doubt('(8), row 2 first l subscript',r'\unsure{1}',['1'],
      'New doubt: a heavy vertical/foot-like trace overlaps low loops, so agreement of the drafts does not securely establish the index.')
doubt('(8), row 3 final l subscript',r'\unsure{0}',['0'],
      'New doubt: a dark enclosing oval is visible but has doubled internal openings and overlapping strokes; current 0 is favored, not resolved.')
doubt('square verification, l immediately after underbrace',r'\unsure{1}',['1'],
      'The small index is heavily blackened and retains overlapping upright and looping strokes.')
doubt('NB paragraph, cancelled baseline phrase',r'\deleted{\unsure{il faudrait}}',['il faudrait'],
      'Crossing line and raised q descender obscure the original phrase; not every letter is plain.')
doubt('NB paragraph, cancelled lower-line word',r'\deleted{\unsure{ici}}',['ici'],
      'Short crossed upright and curved traces remain compatible with ici without securing all three letters.')
doubt('relations block, cancelled factor after rho',r'\deleted{\unsure{l_\infty}}',[r'l_\infty'],
      'The factor is crowded against the opening parenthesis and heavily crossed.')
doubt('relations block, first parenthesized placeholder',r'\unsure{..|\ldots}',['two visible marks','three marks with one obscured'],
      'Two marks can be seen to the right of the cancellation; an additional left mark might be hidden. The later placeholders are independently visible and do not determine this count.','medium')
doubt('(9), row 1 extra cancelled glyph',r'\deleted{\unsure{\varepsilon}}',[r'\varepsilon'],
      'The separate curved glyph is crossed and retraced; its epsilon-like outline is not completely plain.')
doubt('final word',r'\unsure{définition}',['définition'],
      'The last part is too compressed to recover each terminal letter; no expansion or grammatical normalization is made.','medium')
doubt('earlier overwritten layers around rho and the live l factors in the derivation and (9)',
      r'l_0;\quad l_0,l_1,l_\infty',
      ['earlier underlying inscription cannot be independently recovered'],
      'Material-state uncertainty only: the live factors are readable and their C marks are resolved. Extra lower loops, vertical remnants and small slashes, particularly below the final infinity of (9), do not identify a separate earlier factor or index securely enough to assign letters. They are documented without inventing an additional cancelled factor.','low')

inventory=[]
def inv(kind,position,reading,box):
    inventory.append({'element':f'I{len(inventory)+1:02d}','kind':kind,
                      'position':position,'first_words_or_objects':reading,'box':box,
                      'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('display','upper-left numbered definition block (8)',eight,boxes['formula_eight'])
inv('margin note','upper-right underlined NB, general formula and three-row brace',margin,boxes['margin_covariance'])
inv('text','line introducing the square calculation','On a bien',[210,345,510,410])
inv('display','square verification, underbrace, two-row annotation and ok',square,boxes['square_verification'])
inv('text','parenthetic NB paragraph on two baselines, with raised replacement',nb,[215,620,1655,835])
inv('text','introduction of generators, two lines with moved de E+ phrase',system,boxes['generators_prose'])
inv('display','three-row relations brace',relations,boxes['relation_block'])
inv('text','instruction to complete the products, three prose baselines',completion,[210,1300,1630,1565])
inv('deletion','short crossed product at left between the last prose lines',cancelled,boxes['cancelled_product'])
inv('display','long product calculation and its two underbrace labels',product,boxes['product_derivation'])
inv('text','line before the numbered cyclic products','donc finalement',[215,1710,625,1785])
inv('display','numbered three-row block (9)',nine,boxes['formula_nine'])
inv('text','final two prose lines',final_prose,[215,1970,1660,2170])
inv('text','lower-left handwritten page number',r'\mspage{18}',boxes['manuscript_number_eighteen'])
for place,box in [
    ('(8), row 1 first l0 superscript',[620,30,675,80]),
    ('(8), row 1 final l superscript',[755,35,810,85]),
    ('(8), row 2 first l superscript',[630,105,685,160]),
    ('(8), row 2 final l-infinity superscript',[765,110,820,165]),
    ('(8), row 3 final l superscript',[770,190,825,245]),
]:
    inv('deletion',place,r'\deleted{\unsure{-1}}',box)
inv('deletion','NB, baseline phrase after tantôt !',r'\deleted{\unsure{il faudrait}}',boxes['nb_faudrait_revision'])
inv('insertion','NB, raised replacement over the cancelled phrase',r"\inserted{qu'il faudra}",boxes['nb_faudrait_revision'])
inv('deletion','NB, beginning of its second baseline',r'\deleted{\unsure{ici}}',boxes['nb_left_cancelled_ici'])
inv('insertion','small phrase above the gap after relations',r'\inserted{de $\mathcal E^+$}',[340,900,525,1010])
inv('deletion','same phrase cancelled after the final generator rho',r'\deleted{de $\mathcal E^+$}',[1035,925,1300,1015])
inv('deletion','small factor next to rho in first unfinished product',r'\deleted{\unsure{l_\infty}}',[515,1180,610,1280])
inv('insertion','comme before produits, above the cancelled short product',r'\inserted{comme}',boxes['comme_produits'])
inv('deletion','extra glyph after epsilon0 epsilon1 in first row of (9)',r'\deleted{\unsure{\varepsilon}}',[575,1775,650,1850])

second_boxes=[]
def second(kind,coords,reading):
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,
                         'coords':coords,'reading':reading})
second('complete numbered doubtful display (8), all five deletions, all live indices and every numeral',
       boxes['formula_eight'],eight)
second('complete margin note, underline, dotted index correction, abbreviation and all three numerical cases',
       boxes['margin_covariance'],margin)
second('complete square verification, doubtful l index, all powers, underbrace calculation and lowercase ok',
       boxes['square_verification'],square)
second('complete parenthetic NB, both cancellations, replacement, inverse exponent, prime and ellipsis',
       [215,620,1655,835],nb)
second('all lexical disagreements in the generators prose, complete numerical generator list, inserted and deleted de E+',
       boxes['generators_prose'],system)
second('complete relations brace, every index/power, cancelled factor and all unfinished placeholders',
       boxes['relation_block'],relations)
second('complete completion instruction with epsilon0 epsilon1, inserted comme, plural produits and crossed short product between its lines',
       [210,1300,1630,1565],completion+'\n'+cancelled)
second('complete derivation, resolved live l0, every index/power and both underbrace labels',
       boxes['product_derivation'],product)
second('complete numbered block (9), cancelled epsilon, resolved live factors and all overwritten numeric indices',
       boxes['formula_nine'],nine)
second('accent correction and complete first final-prose line, including epsilon_i squared',
       [220,1970,1655,2085],r'Éliminant les $l_i$ comme $\varepsilon_i^2$, on trouve')
second('complete final generator list, with every numeric index, lexical disagreement and doubtful definition ending',
       [220,2050,1660,2170],
       r'des gén. $\varepsilon_0,\varepsilon_1,\varepsilon_\infty,\rho$, avec relations de \unsure{définition}')
second('actual handwritten page number omitted by H',
       boxes['manuscript_number_eighteen'],r'\mspage{18}')

raw=list(csv.DictReader((PACKET/'differences.tsv').open(),delimiter='\t'))
coverage={}
def cov(row,status,explanation,change_id=None):
    d={'row':row,'status':status,'explanation':explanation,
       'C_tokens':raw[row-1]['witness C'],'H_tokens':raw[row-1]['witness H']}
    if change_id: d['change_id']=change_id
    coverage[row]=d
cov(1,'macro/editorial','19 is C’s editorial scan marker, not an extra source inscription.')
for row in [2,16,17,35,39,56,70]:
    cov(row,'macro/editorial','Aligned/gathered versus cases and the invisible right-delimiter syntax encode the same visible left brace and row arrangement.')
for row in [3,5,6,8,11]:
    cov(row,'substantive','This token segment concerns one of the five cancelled superscripts in (8). H’s live illegibility markup loses the cancellation; all five tentative -1 readings remain doubtful. Any adjacent environment or spacing tokens are editorial.','s019-01')
for row in [4,7,9,10,12,13,22,23,24,25,36,37,45,46,47,48,49,50,51,52,53,54,55,58,59,60,61,62,63,64,65,66,67,68,69]:
    cov(row,'macro/editorial','The extra comma token is H’s TeX thin-space command, or the difference merely separates adjacent l factors in tokenization. It is not an additional handwritten comma or a changed factor.')
for row in [14,15]:
    cov(row,'substantive','H supplies parentheses around the index i; none is written. The same inspected subscript also has a detached dot over rho that both drafts omit.','s019-03')
cov(18,'macro/editorial','H’s note about heavy retracing is editorial and not transcribed. The actual five cancelled superscripts are s019-01; the three newly doubtful live subscripts are in doubts only.')
for row in [19,20,21]:
    cov(row,'substantive','Long token realignment comes from C attaching the two-row evaluation beneath the specific underbrace while H makes it a detached display. The factors are present in both; no factor omission is inferred from the alignment.','s019-05')
cov(26,'macro/editorial','The bracket closes H’s detached annotation display and the following words are an editorial note about retracing. They are not source text. The attachment itself is s019-05.')
cov(27,'substantive','The main equality chain exists in both witnesses and is displaced in the token alignment. The actual wording difference here is uppercase OK versus written lowercase ok (s019-06); C’s opening parenthesis before the NB is also genuine and separately logged in s019-07. H’s retracing note is editorial.','s019-06')
cov(28,'substantive','H assigns the raised q to the crossed baseline phrase. The insertion is live qu’il faudra, without final t; the cancelled il faudrait remains doubtful.','s019-08')
cov(29,'substantive','The raised qu’il faudra is retained (s019-08). The cancelled ici and live donc/noter ending are separately distinguished in s019-09 rather than struck as a single clause.','s019-09')
cov(30,'macro/editorial','C’s ldots and H’s Unicode ellipsis represent the three visible terminal marks after the primed epsilon. The deletion-scope error affecting this text is s019-09.')
for row in [31,32,33,34]:
    cov(row,'substantive','These are parts of H’s rewritten generators prose. The ink reads Ici on voit donc qu’on a un syst. de gén. et relations, with de E+ inserted after relations. The explicit abbreviations are preserved.','s019-10')
cov(38,'substantive','The cancelled l-infinity-like factor next to rho is actual, still doubtful ink; H omits it. The neighboring placeholder-count corrections are s019-12.','s019-11')
cov(40,'substantive','The word has a small hooked continuation after its tall t, supporting produits; comme is also an insertion.','s019-13')
for row in [41,42,43,44]:
    cov(row,'substantive','The cancelled short formula and the live long derivation both exist in both witnesses. Their token alignments interleave: the genuine difference is the visible subscript 1 on sigma in the cancelled short formula. The live long formula begins with sigma0 and is not altered by this token shift.','s019-14')
cov(57,'substantive','A separate crossed epsilon-like glyph remains after the two live factors in row 1 of (9); H omits it.','s019-15')
cov(71,'substantive','H’s preceding note is editorial and excluded. The actual word has a visible accent over capital E, so Éliminant is retained against C’s unaccented spelling.','s019-16')
cov(72,'substantive','The ink reads avec relations, plural, rather than H’s une relation. The last word remains doubtful as in C.','s019-17')
cov(73,'substantive','18 is an actual handwritten footer number, unlike the editorial scan marker in row 1. H omits it.','s019-18')
assert sorted(coverage)==list(range(1,len(raw)+1))

report={
    'scan':19,'reader':'reader_c','lines_read':34,
    'layout':'Upright handwritten sheet. Numbered three-row definition (8) sits at upper left and an underlined NB with covariance formulas forms a separate right-margin block. A square verification has two annotation lines under a brace. Two revised prose paragraphs lead to a three-row relations block, a crossed short product, a long derivation with two underbrace labels, and numbered three-row product formulas (9). Two final prose lines end above handwritten 18 at lower left. There is no independent diagram or drawing.',
    'changes':changes,'decisions':decisions,'unlisted_decisions':unlisted_decisions,
    'doubts':doubts,'inventory':inventory,'second_boxes':second_boxes,
    'notation':[
        'The page uses epsilon0, epsilon1 and epsilon-infinity with l0, l1 and l-infinity. Infinity subscripts may be drawn as two low joined loops, sometimes open like a small omega; their local form is checked rather than replaced by omega.',
        'Five inverse-looking superscripts in (8) are explicitly cancelled. The first l-infinity in the third row has no superscript; H’s editorial claim that each l bears one is not a source inscription.',
        'The general covariance formula has epsilon subscript dotted-rho i. The dot over rho and the dot over i are separate. No parentheses surround i; the other rho factors of the note are visibly undotted.',
        'The author says the current epsilon_i are inverses of the earlier ones and proposes epsilon-prime_i. The visible prime is preserved on the epsilon, with i below.',
        'The extension label is script E with superscript plus. The de E+ phrase is inserted after relations and crossed out after the generator rho.',
        'The relations block has unfinished placeholders: two points, then a point and a short dash. The first parenthesized count is crowded and retained as two/three uncertainty. These are placeholders, with no algebraic interpretation supplied to the dash.',
        'In the product derivation and (9), the current post-rho factors l0, l0, l1 and l-infinity are readable despite overwriting. The unreadable earlier layers are not assigned independent extra factors.',
    ],
    'hand':[
        'Dark retracing can combine a straight index with earlier looped forms. It leaves three live indices in (8) and the l index after the square-verification brace genuinely uncertain, even where both witnesses agree.',
        'An upper q descender from qu’il faudra passes across the cancelled baseline phrase. H conflates these writing levels and extends the cancellation too far into the next line.',
        'The live replacement faudra ends with ra and no final t. The tentative earlier faudrait remains under the strike; its letters are not all recoverable.',
        'The terminal s can be a small hooked continuation after a tall t or a compressed word body. The forms support produits and relations against H’s singular readings.',
        'The curved insertion guide for de E+ descends into the gap after relations; the same phrase is separately struck later in the generator line. These are two occurrences with different states.',
        'Both NB labels have separate underlines. The parenthetic NB also has an opening parenthesis omitted by H.',
        'The compact mark over the final capital E is dark and aligned with that letter. It supports Éliminant; faint paper texture is not treated as an accent elsewhere.',
        'The rho loop and long descending stem are distinct from the looped upright l in the final formulas. Earlier extra strokes remain visible beneath the current letters; exact revision chronology is not recoverable.',
    ],
    'abbreviations':[
        {'form':'NB','expansion':'nota bene','place':'underlined right-margin label and underlined parenthetic remark'},
        {'form':'i.e','expansion':'id est','place':'after the general covariance formula; interletter point only, no terminal stop'},
        {'form':'syst.','expansion':'système','place':'Ici on voit donc qu’on a un syst. de gén. et relations'},
        {'form':'gén.','expansion':'générateurs','place':'generators-and-relations introduction and final des gén.'},
        {'form':'etc','expansion':'et cetera','place':'after epsilon0 epsilon1 in the instruction to complete the products; no terminal stop'},
    ],
    'notes':[
        'The author writes three epsilon definitions in (8), with five cancelled inverse-looking exponents. All five remain tentative minus-one readings. Three overwritten live subscripts have new local uncertainty; their expected cyclic pattern has not been used to resolve them.',
        'The right-margin NB asserts covariance under conjugation by rho and expands it in three numerical cases. The general formula’s right-hand subscript contains dotted rho acting on i. This dot is visible and was omitted by both drafts.',
        'The author evaluates the square of epsilon0, attaches a two-row calculation under the middle factor, and writes lowercase ok. These are transcribed assertions; this reader has not independently verified the algebra.',
        'The parenthetic NB states that the epsilon_i here are inverses of those used earlier, with an exclamation mark, and proposes primed notation. The earlier phrase il faudrait and word ici remain crossed and uncertain; the live insertion qu’il faudra and the live donc noter ending are retained.',
        'The following prose introduces a system of generators and relations for E+. The phrase de E+ is relocated by an insertion and a separate deletion. The author leaves three pairwise products unfinished and explicitly says their expressions must be completed as products of rho by expressions in the l_i.',
        'The source has two visible marks after the second unfinished product and a point plus a short dash after the third. Both drafts regularize them to three-dot ellipses. In the first crowded parentheses two marks are visible but another might lie beneath the cancellation, so the count is not resolved.',
        'A short product formula is crossed out between prose lines; its sigma has a visible subscript 1. A longer live derivation follows, with labels l-infinity squared and rho l0 beneath two braces, and the three cyclic product formulas are collected as (9). Four C doubts about the live factors after rho are resolved from their complete formula crops.',
        'Earlier loops and stems survive beneath the retraced rho and l factors. Their exact letters and revision order cannot be reconstructed. This material-state uncertainty is recorded separately from the readable current factors; no additional cancelled factor is invented from the remnants.',
        'The final sentence begins Éliminant, with a visible accent, and ends avec relations de followed by tentative définition. The compressed termination is not silently expanded or normalized. No terminal punctuation or continuation beyond the page is supplied.',
        'Handwritten formula numbers (8) and (9), every numerical index and exponent, and the actual lower-left page number 18 are included in complete second-pass boxes. Scan identifier 19 is editorial. No date is visible; all inscriptions appear to be in his hand.',
        'Thirty-four read units comprise 28 main/annotation/inserted lines, five right-margin label/formula lines and the handwritten footer. Whole page and both native overlapping halves were each viewed once; all agreements as well as disagreements were read. Fourteen distinct enlarged crops were saved and read without remaking a crop.',
        'No mathematical check, proof reconstruction, external research, OCR or TeX compilation was performed by this reader. Root mathematical checks are supplied separately after the ink decisions.',
    ],
    'check_events':[],
    'diff_coverage':[coverage[n] for n in sorted(coverage)],
}

# Structural checks only; no rendering or TeX compilation.
mark_ids=[r['id'] for r in csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t')]
assert [x['id'] for x in decisions]==mark_ids
assert len(changes)==18
assert all(x['c_changed'] or x['h_changed'] for x in changes)
assert len(doubts)==16
assert tex.count(r'\unsure{')==15
assert tex.count(r'\deleted{')==11
assert tex.count(r'\inserted{')==3
for obj in changes+decisions+unlisted_decisions:
    assert (OUT/obj['crop']).is_file()
for obj in inventory+changes+decisions+unlisted_decisions+second_boxes:
    b=obj.get('coords',obj.get('box'))
    assert len(b)==4
    x0,y0,x1,y1=b
    assert 0<=x0<x1<=1677 and 0<=y0<y1<=2360,(obj,b)
assert len({x['box'] for x in second_boxes})==len(second_boxes)
stack=[]
for i,ch in enumerate(tex):
    if ch not in '{}':continue
    j=i-1;n=0
    while j>=0 and tex[j]=='\\':n+=1;j-=1
    if n%2:continue
    if ch=='{':stack.append(i)
    else:
        assert stack,('unmatched closing brace',i)
        stack.pop()
assert not stack
assert tex.count('$')%2==0
assert tex.count(r'\[')==tex.count(r'\]')
assert re.findall(r'\\begin\{([^}]+)\}',tex)==re.findall(r'\\end\{([^}]+)\}',tex)
(OUT/'reader_reports/145_scan019.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({
    'scan':19,'changes':len(changes),'C_changed':sum(x['c_changed'] for x in changes),
    'H_changed':sum(x['h_changed'] for x in changes),'indexed_decisions':len(decisions),
    'resolved_indexed_decisions':sum(x['decision']!='undecided' for x in decisions),
    'unlisted_decisions':len(unlisted_decisions),'doubts':len(doubts),
    'inventory':len(inventory),'second_boxes':len(second_boxes),
    'raw_diff_rows':len(raw),'crops':len(boxes),'structure':'passed',
},indent=2))
