import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[(r'\handwritten{\mspage{34}}',r'\mspage{\handwritten{- 34 -}}'),(r'\uline{2.}\quad \uline{Domaines d\'existence ma-ximaux.}\quad \uline{Points singuliers.}',r'\uline{\handwritten{2}}.\quad \uline{Domaines d\'existence ma\handwritten{-}ximaux}.\quad \uline{Points singuliers}.')]
# Use ordinary quoted strings for the apostrophe inside the heading.
R[1]=(r"\uline{2.}\quad \uline{Domaines d'existence ma-ximaux.}\quad \uline{Points singuliers.}",r"\uline{\handwritten{2}}.\quad \uline{Domaines d'existence ma\handwritten{-}ximaux}.\quad \uline{Points singuliers}.")
L=[]
def a(p,c,f,s,v='high',C=True,k='other'):
 L.append(dict(place=p,c=c,h='absent',final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=False,marked_in_H='not applicable'))
a('original page number','handwritten 34','handwritten - 34 -','header: two pen dashes flank the numerals.',k='omission')
a('section heading numeral','2 without handwriting mark','handwritten 2','section2: a continuous curved pen trace forms the numeral, with an irregular lower horizontal stroke.')
a('section heading internal hyphen','ma-ximaux with unmarked hyphen','ma-handwritten hyphen-ximaux','heading_hyphen: two closely aligned slanting pen segments stand between the typed a and x. The internal hyphen is retained literally.')
a('section heading underlining','periods included in the three underlines','periods outside the three underlines','section and section2: each lower rule stops before its following point, after 2, maximaux and singuliers.')
a('maximal element, first subscript','unsure 0/o','unsure 0/o retained','first0: the subscript is one small closed rounded loop; the ink does not distinguish numeral zero from lowercase o.','low',False)
a('left margin beside on dit','uncertain i','uncertain i retained','margin_i: a short purplish upright with darker lower segments and a faint upper mark is present. Its form and whether it is an intentional letter remain unresolved.','low',False)
a('immediately before on dit','uncertain point','uncertain point retained','margin_dot: a small isolated dark oval lies before on; unlike the neighbouring blue type it has no recoverable typewriter outline. Punctuation versus stray mark remains unresolved.','low',False)
I=[]
def i(k,p,t,h='typewriter and unnamed hand'):I.append(dict(kind=k,position=p,text=t,hand=h))
i('text','top centre','- 34 -','unnamed hand')
i('text','opening continuation','La fonction égale à f dans A, à g dans B … prolongement analytique … A union B')
i('text','proposition introduction','Le th.1 entraîne le résultat plus général suivant :','typewriter')
i('text','proposition 1','famille (A_alpha) … telsque … intersections … f_alpha(x)=f_beta(x) … une.fonction … big union … f(x)=f_alpha(x)')
i('text','proof paragraph','En effet … x in A … valeurs de f_alpha(x) … th.1')
i('text','section heading','2. Domaines d’existence ma-ximaux. Points singuliers.')
i('text','new section opening','Soit A … K^p … fonction holomorphe … ensemble script M')
i('text','maximal prolongation paragraph','M … g est une restriction de h … inductif … th. de Zorn … f_0/o … domaine d’existence maximal')
i('margin note','left of on dit','uncertain i','unknown')
i('text','before on dit','uncertain isolated point','unknown')
i('text','final paragraph','Si A_0 … prolongement maximal … unique … Si A_0=K^p …')
commit(15,62,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter',observations='Whole and both halves personally viewed before C. All text and formula bands enlarged, every C doubt separately enlarged, and each mathematical field/set glyph checked. The literal telsque, une.fonction and ma-ximaux remain; K and E are ordinary single-stem type impressions and M is a handwritten script capital. No H text, no cancelled text or insertion, no context consulted.'))
