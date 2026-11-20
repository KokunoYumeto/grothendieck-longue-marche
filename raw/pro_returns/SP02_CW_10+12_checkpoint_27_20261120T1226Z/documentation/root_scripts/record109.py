from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-07',10,109);ch=r.change
r.edit(r'\scanpage{109}',r'\scanpage{109}'+'\n'+r'\mspage{108}')
r.edit('% archive sheet number: 108','')
r.edit("nombre fini d'objets","nombre fini d'objects")
r.edit(r'\unsure{\rightharpoonup|\longrightarrow}',r'\rightharpoonup')
r.edit('polarisations',r'po$\mathbb{l}$arisations')
r.edit(r'\inserted{de caractéristique nulle.}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.5) {de caractéristique nulle.};
\draw (.05,-.7) .. controls (.1,-.4) and (.3,.05) .. (.8,.1) -- (12,.4) .. controls (12.6,.45) and (12.9,.7) .. (12.7,.95);
\draw (.08,-.55) .. controls (.2,-.7) and (.35,-.65) .. (.38,-.5);
\end{tikzpicture}}''')
r.edit(r'\inserted{G_i\handwritten{/}}',r'''\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]
\node[anchor=base west] at (0,.5) {$G_i\handwritten{/}$};
\draw (-.2,.85) .. controls (-.5,.15) and (.35,.2) .. (.75,-.65) .. controls (.9,-.1) and (1.8,.2) .. (2.25,1.05);
\end{tikzpicture}}''')
r.edit(') est formée',r') est\rlap{\raisebox{-.9ex}{\tikz[x=1em,y=1em]{\fill (0,0)--(.12,.02)--(.08,.13)--cycle;\fill (.09,.2)--(.16,.28)--(.1,.36)--cycle;}}} formée')
r.edit("à l'occasion.",r"à l'occasion.\margin{\tikz[x=1em,y=1em]{\draw (0,0).. controls (.08,.02) and (.16,.14)..(.2,.28);}}")
ch('first tensor sign doubt',r'\unsure{\otimes|\Omega}',r'\otimes',r'\unsure{\otimes|\Omega} retained','The rounded upper arch has a crossed interior, but the lower outline terminates in foot-like ends rather than a fully separate closed oval. The matching later signs were inspected individually and use the first candidate.','tensorfirst; tensorsecond; pairing; tensorlast','misread symbol or index','medium',False,True,False,True)
ch('Pour cancellation',r'\deleted{Pour}',r'\struck{\ill{}}',r'\deleted{Pour}','The capital P bowl and the separate o, u and r bodies survive beneath typed x strokes.','Pour',r'readable ink left as \ill{}','high',False,True,True)
ch('characteristic insertion guide','omitted','omitted','curved lower guide drawn','The long line rises slightly beneath the inserted phrase, hooks upward at the right and descends next to k on the left. A small rounded terminal trace at its foot is drawn as seen, without assigning a separate punctuation character.','characteristic; kpoint','drawing or diagram','high',True,True)
ch('number of simple objects','objets','objects','objects','The seven separate typed cells read o b j e c t s, with an open c between e and t.','objets','misread word','high',True,False)
ch('cancelled de',r'\deleted{de}','omitted',r'\deleted{de}','The tall d stem and e body are visible beneath two cancelling x impressions after pleine.','de','omission','high',False,True)
ch('subcategory index','C_o','C_0','C_o','The subscript is a small round lowercase o, appreciably shorter than the main capital C.','Czero','misread symbol or index','high',False,True,False,True)
ch('quotient numerator',r'\inserted{G_i\handwritten{/}}G_i^o','G_i^{circ}',r'\inserted{G_i\handwritten{/}}G_i^o','The raised typed G and lowered i, followed by a separate handwritten slash, are enclosed by a guide pointing immediately before the baseline G_i^o.','numerator','omission','high',False,True,False,True)
ch('quotient insertion guide','omitted','omitted','curved V-like guide drawn','Two curved arms surround the raised numerator and meet in a low pointed end before the denominator.','numerator','drawing or diagram','high',True,True)
for place,cr in [('quotient denominator exponent','numerator'),('neutral-component exponent','Gzero')]:
 ch(place,'raised o','circ','raised lowercase o','The raised round character has the same typed lowercase o body as the lowered category index, not a distinct drawn small operator circle.',cr,'misread symbol or index','high',False,True,False,True)
ch('inverse-limit arrow hand','handwritten left arrow under lim','varprojlim without hand distinction','handwritten left arrow under lim','The long uneven lower shaft and two left-pointing branches are freehand beneath the typed l i m.','lim','other','high',False,True)
ch('small trace under est','omitted','omitted','two short triangular ink traces drawn','Two separate dark pointed traces descend below the word est; no letter or punctuation value is assigned.','esttrace','drawing or diagram','medium',True,True)
ch('pairing arrow doubt',r'\unsure{\rightharpoonup|\longrightarrow}',r'\to',r'\rightharpoonup','The thick rightward shaft has one short upper head stroke. Its lower edge remains flat through the endpoint with no separate lower branch visible at higher zoom.','pairing; harpoon','misread symbol or index','medium',True,True,False,True)
ch('positive-form quotes','double quotes','guillemets','double quotes','Each typed endpoint is a pair of short raised vertical impressions, with no angular guillemet strokes.','positivequote','misread symbol or index','high',False,True)
ch('polarisation quotes','handwritten double quotes','guillemets','handwritten double quotes','Two small curled pen strokes open the quotation; two descending curved strokes close it above the baseline point.','polarquote','misread symbol or index','high',False,True)
ch('polarisations repeated l','polarisations','polarisations',r'po$\mathbb{l}$arisations','Two distinct vertical l stems stand side by side, with displaced top hooks and overlapping bottom serifs. The prescribed blackboard convention records the self-overstrike.','polarquote; polarl','misread symbol or index','medium',True,True)
ch('groupesde spacing','groupesde','groupes de','groupesde','The s and d occupy successive ordinary character cells, without the extra blank that separates de from Galois.','groupesde','other','high',False,True)
ch('corps cancellation',r'\deleted{corps}','omitted',r'\deleted{corps}','The c o r p s bodies are crossed individually; the p descender is still clear beneath its x.','corps','omission','high',False,True)
ch('lower left trace','omitted','omitted','short rising trace drawn','An isolated short oblique two-part stroke lies in the blank lower-left area.','tick','drawing or diagram','medium',True,True)
ch('folio','comment only','administrative page108','mspage108','The pale lower-left handwritten figures read108.','folio','insertion or placement','high',True,True)
r.doubt('first tensor prefix',r'\otimes',r'\Omega','medium','The crossed interior supports tensor first; foot-like lower ends leave the graphic alternative open.')
r.notation('tensor category sign','crossed arch with lower feet; tensor / Omega at first instance, first candidate in remaining three','10/109','unresolved')
r.notation('round component and category indices','typed lowercase o: lowered at C, raised at both G_i','10/109')
r.notation('pairing arrow','handwritten upper right harpoon; no lower head branch visible','10/109')
r.notation('polarisations l','self-overstruck typewriter l represented by mathbb','10/109')
r.r['abbreviations']=[dict(abbreviation='resp.',expansion='respectivement',attestations='10/109')]
r.r['inventory_overrides']={'pairing arrow':{'first_words_or_objects':'upper right harpoon, resolved at enlargement'}}
extras=[('characteristic-guide','after k','long lower guide with left rounded trace and right upturn','drawing','unnamed hand'),('quotient-guide','around numerator G_i/','curved V-like insertion guide','drawing','unnamed hand'),('est-trace','below est before formée','two short pointed traces','drawing','unnamed hand'),('l-double','polarisations','two offset l impressions','text','typewriter'),('tick','lower left blank','short ascending ink trace','drawing','unnamed hand'),('folio','lower left','108','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:109',sheet_kind='typescript',hand=hand,element='109-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops109.json').read_text())
r.r['inspection_note']='Whole then both halves viewed before C/H, two C macro doubts and inventory. All34 crop recipes viewed. All agreed prose and signs read in ink, including the intermediate characteristic question, plain M and C bodies, all three round o indices, the four tensor signs, n and T(n), and the circumflex in reflête. Tensor doubt retained on graphic evidence, without contextual resolution; pairing arrow resolved to its visible upper-only head. objects corrects C to H. The repeated l, both insertion guides, small under-est traces, lower tick and folio are retained. The rounded trace adjoining k is reproduced within its guide instead of being guessed as independent punctuation. H boundary heading about pages110–112 is editorial material for the following batch and is not assigned to this sheet. No OCR, parallel transcription, context, compilation or mathematical correction.'
r.save('work/record109.json')
