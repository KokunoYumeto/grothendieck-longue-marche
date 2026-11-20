from records import commit,OUT
tex=(OUT.parents[1]/'source/SP58_CW_156-5_witnesses/codex/J156-5-05/pages/J156-5-05_156-5_scan038.tex').read_text()
for a,b in [(r'\unsure{S|I}',r'S'),(r'\unsure{indui}','indui'),(r'\unsure{données}','données'),(r'\unsure{ultra}',r'\unsure{ultr.|ultra}'),(r'\unsure{J|I}',r'J'),(r'\deleted{\unsure{S}}',r'\deleted{S}'),(r'\unsure{ultr-}','ultr-'),(r"\deleted{\unsure{'}}",r"\deleted{'}"),(r'\unsure{croissante|croiss.}','croissante'),(r"associés à $T',T$",r"associés \unsure{à|:} $T',T$")]:
 assert a in tex,a
 tex=tex.replace(a,b)
ch=[]
def add(place,c,h,f,e,k='misread word',conf='high',ac=False,ah=True,hm=False,con=''):ch.append((place,c,h,f,e,k,conf,ac,ah,hm,con))
add('first cancelled word','indui','induise','indui','038 top_delete crop (1310,75,1500,135): last small upright has its dot above; no subsequent se before the strike ends.')
add('two-source diagram, source S','S.','S','S.','038 diagram crop (1140,318,1485,410): a detached point stands after the unprimed source S.','omission')
add('two-source diagram, target sign','cancelled cup, amalg','amalg','cancelled cup, doubtful, amalg','Same diagram crop: curved U-like old stroke under two heavy live uprights.','omission','low')
add('two-source diagram, lower tip','dot / arrowhead','arrowhead','dot / arrowhead','Same diagram crop: only a short dark blob at the tip, unlike the clear two-sided head above.','drawing or diagram','low')
add('NB prefix','ultra, live and doubtful','ultra, struck','ultr. / ultra, live','038 nb_prefix crop (1130,478,1590,555): looped retracing throughout the prefix, but no separate cancellation across it; small point near the end.','misread word','low',True,True)
add('family index','i∈J / I','i∈I','i∈J','038 family crop (275,585,490,687): final capital has a left-curving foot below its stem, with no I lower bar.','misread symbol or index','high',False,True,False,'The family is indexed by J in its first occurrence, but the quantified condition below uses I; keep the mismatch.')
add('map from S_i, shaft','bare line','arrow','bare line','038 nb_map crop (1065,546,1360,630): line ends with a downward nib turn, not a two-stroke arrowhead.','drawing or diagram')
add('map from S_i, label','f_i / f dot / f′','f_i','f_i / f dot / f′','Same nb_map crop: the only detached mark is one tiny fleck to the upper right of f; its role is uncertain.','misread symbol or index','low')
add('map target overwrite','cancelled S before X','X alone','cancelled S before X','Same nb_map crop: the S loop and lower bar remain beneath the two diagonals of X.','omission','medium')
add('condition on i','pour ∀i∈I','pour tout i∈I','pour ∀i∈I','Upper half, y855–905: explicit universal-quantifier glyph before i.','expansion or normalisation')
add('end of NB prefix','ultr-','ultra-','ultr-','Upper half, y850–900: short hyphen follows the reduced ultr, with no final a.','expansion or normalisation')
add('amalgamation description','suivant le sous-espace','standard en sous-espace','suivant le sous-espace','Halves, y1090–1250: suivant ends in a tall t; next baseline begins le, not en.')
add('reversed inclusion correction','inserted prime, cancelled superset, subset, cancelled prime','S′⊂S, no corrections','C correction states retained','038 inclusion crop (728,1366,925,1450): prime added over left S, crossed old comparison, dense strike at right prime.','omission','medium')
add('pair after sous-figure de','(S,Π / T)','(S,T)','(S,Π / T)','038 pair crop (415,1540,585,1615): two distinct close stems beneath a long cap; could be Π or a retraced T.','misread symbol or index','medium')
add('criterion abbreviation','sss','ssi','sss','Lower half y1560–1590: three joined s shapes; no dotted i.','misread word')
add('Les sous figures','sous figures','sous-figures','sous figures','Lower half: whitespace between sous and figures, no hyphen.','expansion or normalisation')
add('foot S′ to S','bare line / arrow','hooked arrow','bare line / arrow','038 foot crop (273,2110,1525,2317): no hook at source, and terminal dark blob leaves arrowhead uncertain.','drawing or diagram','medium')
add('after associés','à',':','à / :','Same foot crop: raised accent/dot and a very small lower curved sign; à is plausible but colon cannot be excluded.','misread word','low',True,True)
inv=[('text','top centre','37'),('text','opening','topologie sur S∪S′'),('deletion','opening','indui'),('diagram','upper right','S. and S′ to S amalg S′'),('deletion','diagram target','cup'),('text','bracketed NB','Si on a des espaces ultr. topologiques'),('deletion','NB map target','S overwritten by X'),('insertion','NB','une'),('deletion','NB full line','La relation de préordre associée est la suivante :'),('text','NB continuation','Dans le cas d’espèce'),('text','middle','Si on a S′⊂S'),('insertion','comparison','prime on first S'),('deletion','comparison','superset; prime on right S'),('text','lower middle','Les sous figures de (S,T)'),('text','foot introduction','D’autre part, la relation'),('display','foot','(S′,T′)≪(S,T)'),('text','foot','signifie que S′⊂S')]
notes='''### 038-N1 — Assertions

Continues the gluing topology on S∪S′ and describes it as the final topology for the two inclusions; the NB identifies this with the topological amalgam over the common closed subspace. It asserts that final topologies from ultratopological spaces remain ultratopological. Subfigures correspond to closed subsets with induced topology; the relation ≪ is recast as inclusion with continuity, equivalently monotonicity for the associated preorders. Manuscript page 37, no date.

### 038-N2 — Apparent slips preserved

The NB’s family subscript is J, whereas its later universal quantifier uses I. Its maps land in X, but the next clause still says “topologie finale sur S”. It literally says A∈X for closed subsets, not A⊂X. These are all retained. The glyph in the pair after sous-figure has two stems and remains Π/T, although T is mathematically expected. The foot map has no hook; a head is uncertain.

### 038-N3 — Targeted proof check

For maps f_i from spaces whose closed sets are stable under arbitrary union, define the final closed subsets A of X by closedness of every inverse image. Inverse image commutes with arbitrary union, so the union of any family of final closed sets again has closed inverse images and is final closed. The empty set, X and finite intersections satisfy the usual closed-set axioms by the same operation. This verifies the NB’s ultratopology claim under its stated source hypothesis, interpreting the variable slips only for the check and leaving the transcription untouched.'''
doubts=r'''| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| two-source diagram old sign | cup | obscured curve | low |
| lower line tip | dot | arrowhead | low |
| NB prefix | ultr. | ultra | low |
| NB map label | f_i | f dot; f′ | low |
| overwritten comparison | superset | obscured old sign | low |
| pair after sous-figure | Π | T with retraced stem | medium |
| foot map | bare line | arrow | medium |
| foot after associés | à | colon | low |

All fifteen C doubt entries were examined. Resolved: first amalgamation subscript S; cancelled indui; données; family J; old S at X; ultr-; cancelled prime; croissante. The NB prefix receives a revised first reading; its lack of cancellation is preferred but the dense retracing is disclosed.'''
hand='''The subscript J has a compact top bar and a left-curving low foot; it must not be silently harmonised to the later I. A bare line may end in a dark nib turn or dot and should not automatically become a hooked inclusion arrow. Two close stems in a T-like glyph may reflect retracing; Π remains a visible alternative in the pair. Heavy ultr. retracing has no independent cross-out stroke.'''
commit(38,tex,ch,inv,notes,doubts,hand,notation='The gluing uses S∪S′ ≃ S amalg over S∩S′. ≪ denotes inclusion plus continuity; the comparison for subfigures is stronger. I/J and S/X variable mismatches are retained.',abbr='NB underlined; ultr- and ultr. are truncated prefixes; top. = topologie; sss retained literally.',checks=[('038-N3-final-ultratopology','targeted proof check','Verified arbitrary-union stability of final closed sets by inverse images; checked closed-set axioms. No correction of J/I, S/X or A∈X in the text.')])
