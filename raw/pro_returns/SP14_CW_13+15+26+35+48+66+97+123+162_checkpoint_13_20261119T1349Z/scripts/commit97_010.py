import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
(r'\unsure{\eta|y}',r'\eta'),
(r'i_{\handwritten{\unsure{\times|\ast}}}(i^{*}(P))',r'i_{\handwritten{\ast}}(i^{\handwritten{\ast}}(P))'),
(r'\deleted{\unsure{\mathrm{Pic}(}}\inserted{\mathrm{Pic}(\overset{\handwritten{\sim}}{X})=}',r'''\deleted{\mathrm{Pic}(}\tikz[baseline=0pt,x=1em,y=1ex,line cap=round]{
  \path[use as bounding box] (0,-.8) rectangle (.25,4.8);
  \node[overlay,anchor=base west,inner sep=0pt] at (-4.2,2.8) {$\inserted{\mathrm{Pic}(\overset{\handwritten{\sim}}{X})=}$};
  \draw[overlay] (0,-.8) .. controls (-.15,1.4) and (.35,1.6) .. (1.0,1.7)
    .. controls (2.6,1.8) and (3.6,2.0) .. (4.0,2.3)
    .. controls (4.6,2.6) and (4.8,3.2) .. (4.8,3.8);
}'''),
(r'\deleted{\unsure{Lorsque}}',r'\deleted{Lorsque}'),
(r'\underline F_{\bar{\deleted{\unsure{y}}\handwritten{y}}\deleted{\unsure{*}}}',r'\underline F_{\bar{\deleted{y}\handwritten{y}}^{\deleted{\unsure{*}}}}'),
(r'\deleted{\unsure{tc}}',r'\deleted{tc}'),
(r'\deleted{\unsure{sig}}',r'\deleted{sig}'),
(r'\deleted{est nul \unsure{également}}',r'\deleted{est nul également}')]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('opening formula, alphabets',r'\underline G_m, \underline{\mathrm Q}/\underline{\mathrm Z}',r'\underline{\mathbb G}_m, \underline{\mathbb Q}/\underline{\mathbb Z}',r'\underline G_m, \underline{\mathrm Q}/\underline{\mathrm Z}','top4x: G has one curved left contour; Q one oval and descending tail; Z one diagonal. The horizontal lower strokes are separate underlines, not doubling of the letter strokes.','high',False,True,'misread symbol or index')
a('cancelled token after Soit',r'\deleted{\unsure{$i$:}}',r'\struck{\ill{}}',r'\deleted{\unsure{$i$:}}','oldi20x: portions of a typed upright and raised point survive under x and hand cancellation, with a small right-hand punctuation trace. These support i and colon provisionally but not securely.','medium',False,True,'readable ink left as \\ill{}','yes')
a('generic-point inclusion',r'\unsure{\eta|y}',r'\eta',r'\eta','eta8x: short left stem enters a low turn and rounded right shoulder; the right stroke descends well below the body. Comparison with the enlarged eta forms in picsub10x and BrEta14x supports eta.','medium',True,False)
a('(4.8), lower mark on i',r'\unsure{\times|\ast}',r'\ast',r'\ast','istar24x: in addition to the four long diagonal rays, short lateral strokes protrude at left and right of the centre; this is an asterisk rather than a simple two-stroke cross.','medium',True,False,cons='The lower mark of i in (4.8) is an asterisk.')
a('(4.8), upper asterisk on second i','asterisk, not marked as handwritten','asterisk',r'\handwritten{\ast}','Bformula7x: the upper mark has dark uneven hand strokes distinct from the lighter typed i and parentheses; its star shape remains unchanged.','high',True,False)
a('faisceaux gratte-ciel quotation marks','``faisceaux gratte-ciel\'\'','« faisceaux gratte-ciel »','``faisceaux gratte-ciel\'\'','EFquotes4x: the opening and closing marks are pairs of small raised vertical/sloping strokes, not angled guillemets.','high',False,True,'misread symbol or index')
a('cancelled beginning of Pic display',r'\deleted{\unsure{\mathrm{Pic}(}}',r'\struck{\mathrm{Pic}}',r'\deleted{\mathrm{Pic}(}','picinsert8x: P stem/bowl, dotted i, open c and a full curved opening parenthesis remain through the typed x and hand cancellation. The parenthesis omitted in H is visible.','high',True,True,'omission')
a('raised Pic(X tilde)= addition and leader','inline addition after cancelled Pic(','inline addition before cancelled Pic','raised addition with curved leader ending after cancelled Pic(','picinsert8x: the new expression sits above the cancelled token; its lower rule bends down into the gap immediately before the surviving Pic(X tilde/Y tilde), then sweeps upward at its right end. The text and stroke are retained in that arrangement.','high',True,True,'insertion or placement')
a('cancelled word before Compte tenu',r'\deleted{\unsure{Lorsque}}',r'\struck{\ill{}}',r'\deleted{Lorsque}','oldLorsque14x: the capital L foot, o/r, low s, descending q and final u/e traces remain distinct beneath the row of typed x marks.','medium',True,True,'readable ink left as \\ill{}','yes')
a('Le corrected to le',r'\deleted{L}\handwritten{l}e','le',r'\deleted{L}\handwritten{l}e','Le18x: a typed capital L with rightward lower foot remains under the darker narrow handwritten l loop; the following typed e is unchanged.','high',False,True,'omission')
a('(4.11), cancelled initial term',r'\deleted{\underline{\unsure{E|F}}_{\bar y}}',r'\struck{\ill{}}',r'\deleted{\underline{\unsure{E|F}}_{\bar y}}','eq11old18x: underline, upper/middle letter bars and barred lower y can be distinguished under the oblique cancellation. The lower letter arm is covered, so E/F remains unresolved.','low',False,True,'misread symbol or index','yes')
a('(4.11), overwritten y',r'\deleted{\unsure{y}}\handwritten y','y',r'\deleted{y}\handwritten y','eq11F14x: typed upper fork/serifs and a light lower remnant remain behind the heavy handwritten loop and descender. These identify the old letter as y.','medium',True,True,'omission')
a('(4.11), cancelled upper mark beside barred y','cancelled doubtful star following y at subscript level','absent','cancelled doubtful star raised to the right of barred y','eq11F14x: the heavily cancelled mark lies beside the horizontal bar, above the body of y. Several short outward strokes survive, supporting a star provisionally; its precise form stays marked. The transcription now retains its raised position.','medium',True,True,'insertion or placement',cons='The cancelled mark beside barred y in (4.11) is raised, rather than an additional ordinary subscript.')
a('(4.12), cancelled extra subscript',r'\deleted{\unsure{\delta_y|y}}','absent',r'\deleted{\unsure{\delta_y|y}}','eq12old18x: a loop at upper left and lower descender/loop survive beneath dense diagonal hatching, but the full delta-plus-y structure cannot be separated securely from a single y.','low',False,True,'omission')
a('correction within caractéristique',r'cara\deleted{\unsure{tc}}\handwritten{ct}éristique','caractéristique',r'cara\deleted{tc}\handwritten{ct}éristique','char8x: the old t ascender/cross protrudes behind the live c, and a faint open curved c remains below/left of the live t. The two transposed underlying letters can be retained without doubt.','medium',True,True,'omission')
a('punctuation before Désignant','parfait, Désignant','parfait. Désignant','parfait, Désignant','punct8x: the low round point has a continuous descending hooked tail; this is a comma.','high',False,True,'misread symbol or index')
a('cancelled fragment after déjà',r'\deleted{\unsure{sig}}',r'\struck{\ill{}}',r'\deleted{sig}','oldSig18x: the s curves, separate dot above i and the g lower bowl are visible around the typed x and heavy horizontal cancellation.','medium',True,True,'readable ink left as \\ill{}','yes')
a('cancelled est nul également',r'\deleted{est nul \unsure{également}}',r'\struck{est nul également}',r'\deleted{est nul également}','oldest8x: the acute accent, g descender, a curve, tall l and the remaining e/m/e/n/t stems and bowls remain distinguishable beneath the row of x marks and horizontal hand stroke.','medium',True,False)
a('right edge after admet un',r'un\unsure{e}','une',r'un\unsure{e}','eedge12x: un is clear; the next letter meets the black scan border, leaving only a rounded protruding left contour. The e is retained with doubt because its internal bar and right side cannot be seen.','medium',False,True,'misread word')
I=[]
def i(kind,pos,text,hand='typewriter'):I.append(dict(kind=kind,position=pos,text=text,hand=hand))
i('text','upper right','17','his hand')
i('display','opening line','H3(Y, underlined Gm) ≃ underlined Q/underlined Z,','typewriter and his hand')
i('text','opening line after formula','d’où le corollaire.')
i('text','above inclusion','Soit')
i('deletion','after Soit','uncertain i:','typewriter and his hand')
i('display','generic-point inclusion','i: η → Y','typewriter and his hand')
i('text','before (4.8)','l’inclusion du point générique, et posons')
i('display','(4.8)','underlined B = i lower-star (i upper-star(P)),','typewriter and his hand')
i('text','before (4.9)','de sorte qu’on a un homomorphisme canonique')
i('display','(4.9)','P → underlined B,','typewriter and his hand')
i('text','before (4.10)','et on posera')
i('display','(4.10)','underlined E=Ker(P→B), underlined F=Coker(P→B).','typewriter and his hand')
i('text','paragraph below (4.10)','Les faisceaux E et F sont des ``faisceaux gratte-ciel\'\' ... noyaux et conoyau de l’homomorphisme','typewriter and his hand')
i('insertion','Leur and fibre endings','two live added s letters','his hand')
i('insertion','above Pic display','Pic(X tilde)=','typewriter and his hand')
i('drawing','below raised Pic addition','curved lower rule with downward left leader ending before surviving Pic','his hand')
i('deletion','start of Pic display','Pic(','typewriter and his hand')
i('display','Pic display','Pic(X tilde/Y tilde) → Pic(X tilde with eta tilde index / eta tilde),','typewriter and his hand')
i('text','paragraph below Pic display','où les ~ dénotent ... point géométrique y barred au dessus de y.','typewriter and his hand')
i('deletion','before Compte tenu','Lorsque','typewriter and his hand')
i('text','middle paragraph','Compte tenu que ... morphisme précédent ... régulier, on trouve','typewriter and his hand')
i('deletion','start of le morphisme','old capital L','typewriter')
i('insertion','over old L','lowercase l','his hand')
i('display','embedded in middle paragraph','Pic(X tilde with plain eta index); Pic(X tilde) → Pic(X tilde with eta tilde index); X tilde','typewriter and his hand')
i('deletion','before (4.11)','underlined E/F with barred y index, uncertain','typewriter and his hand')
i('display','(4.11)','underlined F at corrected barred y = Pic(X tilde eta / eta tilde) / Pic(X tilde eta tilde)','typewriter and his hand')
i('deletion','F index in (4.11)','old y and cancelled raised uncertain star','typewriter and his hand')
i('insertion','F index in (4.11)','handwritten y','his hand')
i('display','(4.12)','underlined E at barred y = Ker(Pic(X tilde) → Pic(X tilde eta tilde)).','typewriter and his hand')
i('deletion','left side of (4.12)','uncertain delta_y / y','his hand')
i('text','last paragraph opening','Compte tenu que Br(eta tilde)=0 ... nul si k(y) est parfait,','typewriter and his hand')
i('deletion','within caractéristique','old tc','typewriter')
i('insertion','within caractéristique','ct','his hand')
i('text','last paragraph continuation','Désignant par ... entiers analogues ... situation localisée ... un argument déjà','typewriter and his hand')
i('display','within last paragraph','δy, δ′y, δ″y; δ, δ′, δ″; X tilde → Y tilde','typewriter and his hand')
i('deletion','after déjà','sig','typewriter and his hand')
i('text','last lines','fait plus haut nous montre que F at barred y ... est nul également si δy=1 ... une section sur Y tilde.','typewriter and his hand')
i('deletion','before live est nul également','est nul également','typewriter and his hand')
i('text','final sentence, unfinished on this page','Nous allons supposer pour simplifier, par la suite, que')
commit(97,10,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter and his hand',observations='Whole page and both supplied halves personally viewed before C/H; all 36 base crops and two adaptive letter crops personally read. Initial multi-image response for eq11R/eq12old/eq12R/BrEta was truncated and was not counted as viewed; each was subsequently displayed and read in a smaller call. Entire prose, accents and punctuation, including literal conoyau and unaccented connait, read in ink. Every formula, index, bar, tilde, star, letter alphabet, arrow and parenthesis checked. All cancellations and the raised Pic insertion/leader checked. E/F and top G/Q/Z have single typed stems/contours with separate underlines. Live plural s additions retained. Archive 9 remains comment only; manuscript 17 retained. No readable watermark established. This is first-pass collation, not the later audit or a mathematical check.'))
with open('out/notation.tsv','a') as f:
 f.write('Asterisk on i\t97/10 (4.8)\tLower mark has diagonal rays plus short lateral strokes; upper mark also handwritten\ti_{\\ast}(i^{\\ast}(P))\tnone\n')
 f.write('Raised cancelled mark beside barred y\t97/10 (4.11)\tBeside the bar, above the y body; heavily cancelled\t\\bar y^{\\deleted{\\unsure{*}}}\tstar shape remains uncertain\n')
